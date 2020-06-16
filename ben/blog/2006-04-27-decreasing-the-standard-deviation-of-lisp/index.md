% Decreasing the Standard Deviation of Lisp
---

Recently, there was an (apparently cyclic) thread on comp.lang.lisp the
other day about how lisp sucks and why new developers aren\'t flocking
to bask in its glory.\
\
And, while it started out with a few broad points, the thread quickly
moved into several small points, and the various merits of those
points.\
\
One of them, in an example used by Rob Garret, discussed the merits of
deprecating nth in favor of elt, since elt is a superset of nth.\
\
However, when I think about the existence of nth and elt more, I don\'t
think that it really matters to newbies whether or not both nth and elt
exist, since either:\

1.  They don\'t know about the existence of both
2.  They know about the existence of both, but they don\'t really care

And, as I thought about it more, I came to the conclusion that it is
actually better to have both nth and elt in common lisp. This follows my
thinking that the biggest barriers of entry to learning a new language
are focused on a few main things:\

1.  New syntax
2.  New libraries and their various available functions/methods
3.  Various new concepts presented within the language (C: pointers,
    ruby: blocks, lisp: macros,functional style, Java:mostly-OO)

Note: not meant to be a complete list of new concepts from various
languages, just a few examples.\
\
There are many reasons why languages do well and others don\'t, but I
think one of main reasons a language does well is that it has
similarities to the current collection of popular languages.\
\
New concepts can be difficult to learn, but if you look at Ruby, Perl
and Python, all languages that are slower then lisp, yet have concepts
not commonly used in C/C++/Java that are similar to lisp (blocks,
functional style), they tend to do better, IMHO, because they have
strong syntax and library similarities to C/C++/Java.\
\
I think that the difference in the 3 main points up above constitutes
what I call a languages \"standard deviation\" to the current most
popular languages. The corollary is; a language that offers a low
standard deviation will have a higher appeal then a similar language
with a higher standard deviation. (Note: I\'m doing some
pseudo-statistics at work; well, the statistics are real, but I\'m not
an real statistician, hence the \"pseudo\" part)\
\
For example, why did Matz write Ruby? It has a lot of concepts that lisp
employs, but its significantly slower. Between inventing ruby and just
using lisp, [why didn\'t Matz just use lisp, or
smalltalk?](http://blade.nagaokaut.ac.jp/cgi-bin/scat.rb/ruby/ruby-talk/179642)\
\
I think one of the big reasons (perhaps unconsciously), is that Matz
recognized the \"standard deviation\" between both lisp and smalltalk,
and set about designing a language that was closer to most programmers
current expectation of a language.\
\
I think that lisp would gain broader appeal as well by reducing its
\"standard deviation\". Since I like the current syntax of lisp, and I
suspect a lot of other people do, that only leaves standard
functions/libraries and concepts.\
\
Also, since I happen to think that lisp\'s concepts (macros) are some of
the best ever invented, I\'ll nix that idea as well.\
\
This leaves:\

1.  standard functions / libraries / objects

I think lisp would do well to add extra library functions that are very
similar to the existing favorite languages. Not only would this not
break any existing code, but it would help ease the learning curve that
new programmers face when learning a new language, especially one with a
much different syntax, such as lisp.\
\
I\'ll readily accept that whatever is currently popular may not be the
best way to do something, but by not giving programmers a sense of
familiarity, you force them to basically start from scratch. Once people
give lisp a chance, they\'ll come to understand the power that it
conveys, but most people already don\'t have enough time to spend
learning new concepts they can use in their existing language, much less
spend time learning new concepts, a radically different syntax, and a
whole new set of libraries/functions!\
\
I think that we (the lisp community) should imitate some functions of
the more popular languages to increase membership. As an example, I was
thinking it would be fairly easy to add things like \"while\", \"for\",
\"foreach\", \"var\", etc.\
\
They could even be interned into a new package (maybe
\'new-lisp-user\'), so someone could just import that package, and be
greeted with functions that more closely mirrored their expectations.\
\
Here\'s some sample code:\
\
(defmacro var (&rest all)\
\`(let ,\@all))\
\
See, that\'s all I\'m talking about. Just creating new methods that look
an awful lot like existing lisp methods, but have function and name that
are more familiar to new programmers. Now, as a new programmer, I can
focus on learning the different syntax, those funky macro things, etc,
all while having the familiarity of my favorite language ;)\
\
Note, I think my arguments are implicitly supported by SteveY\'s [blog
post about why lisp in an unacceptable
lisp](http://steve-yegge.blogspot.com/2006/04/lisp-is-not-acceptable-lisp.html).
Its not that the points brought up were technically sound, but rather
that they represent the kind of problem I\'m talking about; things
behaved differently then he had come to expect from most \"mainstream\"
languages.\
\
It\'s all about minimizing standard deviation.
