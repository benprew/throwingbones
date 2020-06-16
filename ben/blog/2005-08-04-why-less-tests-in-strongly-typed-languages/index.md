% Do Strongly Typed Languages Have Less Tests?
---

This isn\'t meant to be an answer, or even truthful, more just something
to think about, again, its just me ruminating on various floaties in my
head. Maybe its true, maybe its not, I don\'t have the visual landscape
to know for certain, and should not be taken as such. Think of it more
as dinner conversation, in a one-sided sorta way.\
\
Anyway, I was thinking about testing in loosly-typed languages, and how
at the last company I worked for, where I only wrote in loosly-typed
languages (Perl), that having tests written for our software was not
only a Good Thing, but a necessity. There were many, many problems we
caught via tests that we would not have caught until they bit us in a
production environment.\
\
However, most of C++ and Java code I\'ve seen recently doesn\'t have any
tests, nor with the complexity of the system could you test everything.
Even without testing, the software runs, perhaps better then I expected.
Although high quality software has been written without tests, so having
tests is not a requirement for high-quality software, but that\'s not
the point\...\
\
The point is more a comparison between strongly-typed an loosely-typed
languages. In strong typing, the compiler does a lot of the checking
work for you, even though in languages like C++ and Java, you have to be
explicit about the type (which I find revulting, personally), so many of
the tests you might write are already covered by the compiler.\
\
In comparison, with Perl, you won\'t find out if you can call a method
until run-time. This forces you to create tests that confirm that your
code, can indeed, call the methods you want to call, on the objects you
want to call them on.\
\
So, in effect, part of your test suite becomes a simple-compiler,
checking for certain things that strongly-typed languages have already
checked. This poses a strange question, are you coders writing tests, or
fixing a \"broken\" compiler? Is the compiler that broken to begin
with?\
\
Apparently, I\'m not the first person to have thoughts like this
(http://www.artima.com/intv/strongweak.html), but I\'m no Guido Van
Rossum, even on my better days.
