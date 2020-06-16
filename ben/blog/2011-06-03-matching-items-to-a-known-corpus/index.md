% Matching Items to a Known Corpus
---
As part of [MTG Card Prices](http://mtg.throwingbones.com), I want to be able to identify what cards are part of an auction. If you could only list a single card on eBay, this would be relatively simple, but it is complicated by the fact that you can list

 * Multiple different cards together
 * Different editions of the card (10th ed, M11, M10, etc)
 * Foil versions of some card
 * Foreign editions
 * Altered cards

And so on. For some of the more difficult cases (multiple cards together, altered cards, foreign cards), I am just excluding them. If a person is buy 2 Jaces and a Tezzeret, it's hard to get an idea how that person is valuing those cards individually.

For the other cases, I have a database of cards I've created using the Gatherer search engine and some Internet digging. That database is used as my "corpus" and auctions have to be matched to it.

Every day, there are about 10k auctions that are listed that we need to try and match to our corpus. Also, as the matching logic evolves or new cards become available, we need to be able to rematch days or even weeks of cards historically.

I started by breaking up the card and cardset name into their keywords, so a card like "Tezzeret, Agent of Bolas" from "Mirrodin Besieged" would become "tezzeret agent bolas mirrodin besieged". These words were then put into a hash table, specifying the card # that they were a part of. Something like this:

    {
        mirrodin => [ 1, 2, 3 ],
        besieged => [ 1, 2, 3 ],
        tezzeret => [ 1 ],
        bolas => [ 1 ],
    }

Then, you would break the auction into keywords and add a point for each card that has that keyword. (ex. you have the auction "Tezzeret from Mirrodin, like NEW!!!!", this would break into "tezzeret from mirrodin like new", and when you add up the keywords, card 1 would have 2 points, while card 2 and 3 would only have 1 point).

Then, you would order the cards by score, and if you met some threshold, you'd match the auction to the card with the most points.

This was a fine solution to the problem and generated good "guesses" if a card couldn't be matched.

Unfortunately, it was too slow for my needs (5 auctions/sec), requiring n hash lookups for each auction (where n is the # of keywords in an auction), and it took up a fair amount of memory.

Doing a little research, I came across a data structure called a [Trie](https://en.wikipedia.org/wiki/Trie) that I thought would work well, and since I'm using Ruby, there's a gem for it.

After doing a little testing, I was achieving similar auto-matching %'s, but had more then doubled my performance (12 auctions/sec).

Unfortunately, the Trie was even more memory intensive then the previous solution. But, it had pointed me in the right direction.  Instead of storing the a character at a time, I built a Trie to store a word at a time. That and I used hashes to store the data, instead of creating a Trie-node each time.

With a little monkey-patching to the Hash class, the result was much improved memory and incredibly fast matching (170+ auctions/sec)!
