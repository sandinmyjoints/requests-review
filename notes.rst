>>> type(response)
requests.models.Response

>>> type(response)
instance

Reading and Re-reading
======================

Code is complex. There's a lot to remember, and interpret. Unlike natural
language, it's not learned from an early age, and we are not exposed to it day
in and day out for our entire lives. It did not evolve over thousands of
generations. It is a human artifact.

It shares some traits with natural languages. It is imperfect. It is
changing. You can learn it over time.

And a given piece of code, like a piece poetry and prose, is generally read
is far more than it is written. It is written, revised, rethought, edited,
reworked. At some point, it exists as an artifact.

Code has to be read much. Requests is easier to read. It stands up to
re-readings.  Its re reading value is high but for the opposite reason: there is
not more to discover.


Memory
======

It's common for programmers to look back at their own code that they wrote years
or even months ago and not recognize it. Their reactions may range from
admiration (How did I figure that out?) to disgust (What was I thinking?).

Well-written code, code written to be easily read and understood, to
assist in comprehension, has certain characteristics, some combination
of clear variable and function names, consistent style, modularization
into logical chunks that fulfill a single goal or purpose. The list
can go on, and not every programmer agrees with all of these.

Social
======

Coders can leave plain-language comments for each other in source code
that the computer will ignore entirely. These have their own style
rules, sort of.

Coding is more and more social. Computers don't program
themselves. The success of a programming language or tool or service
depends upon users: an audience of people willing to actually use it,
to adopt it; programmers call the amount of people who will use
something its "mindshare."

Load-bearing Walls
==================

Assumptions like these, called invariants, are like load-bearing walls in a
building. The system is built around them. After the fact, it's painful and
costly to change them, and the reliability of the whole suffers.



A Quote
=======

To me, there's an innate frustration in programming. It doesn't stem from having
to work out the solutions to difficult problems. That takes careful thought, but
it's the same kind of thought a novelist uses to organize a story or to write
dialog that rings true. That kind of problem-solving is satisfying, even
fun. From: http://prog21.dadgum.com/154.html


Historical Accidents
====================

The internet and web and many programming standards evolved sort of like
language, more so than they were developed by humans. The humans who developed
them couldn't predict the future, so the things they make tend to get superceded
by events. The ones that stick around are usually very loose, modular: they do
very small units of things, very well.

Why Doesn't Everyone Use Requests
=================================


Why do any Python programmers even use urllib2? You might wonder why anyone
would use urllib2 instead of requests. The main reason is that it's standard,
guaranteed to be in every installation of Python. I had to take extra steps to
install requests.


Translation?
====================

HTTP 1.1 as the original work. Is requests as translation of that?


Is it a work of Art?
====================

API as a work of art. Is it a work of art? Its entirely functional. Art is not
supposed to have an overt purpose.

Empathy is not a word commonly associated with software engineering.

The most basic function of the internet is the request/response
cycle. A client such as a web browser makes a request using the HTTP
protocol, and a web server, such as google.com, returns a response. 

Doing this by hand was tedious, exaggerated, overly verbose, not worth
the return on. curl -X -I etc etc

Contrast that with requests: request.get()


Concision, precision, saying only what one needs to see and no
more. Vivid, accurate, precise. Verbs, not adjectives. -X and -I are
the equivalent of adjectives. 

The value is on the developer's time and , not the 

Code is for humans. 

Feelings
========

I had to make myself do this one. It doesn't come naturally.

What feelings does reading evoke? Everything under the sun. 

What feelings does Requests evoke?  Empowered, excited, streamlined, smart, able to
get something done, cared for, a peer who is really superior, who is helping me
out, smoothing the way. Resentment? Not from me. Curiosity. A sense of this is
how things should work. Appreciation. Hope. Optimism. Connection.

Anger, frustration, incompetence, doubt, sanity-questioning, contempt.

Requests
========

For example, if I want to get a get webpage, I can call Requests' `get`
function, and give it the address of the webpage. Requests will do the work of
making a connection and downloading the webpage, and give me the result.

Sharing
=======

Why do programmers tell other programmers how to use their code? Programming is
hard, and because programmers (a lot of them, anyway) are helpful souls. We
share our work with each other, to a surprising degree. This dates back to a
tradition and culture of sharing. If I solve a problem for myself, I figure I
might as well help out others out there. It's no extra work. It shows how good
we are as programmers. And we think it's cool to see what other people do with
our work. It's a grand project that we're all part of.


Curl
====

Curl is also a tool programmers use to retrieve information over the
internet. It's very common, coming included with many types of operating
systems. (If you're using OS X, it's on your computer.) It's not part of Python.

It looks like this:

`$ curl -L -X GET -i -H "Accept: application/xml"
http://www.goodreads.com/author/list?id=6410\&key=FCeXl2vCxU22dmoVkGub4A`

This is difficult poetry of a sort: cryptic. Terse and verbose at the same
time. It requires reference and outside knowledge. But lacking natural language
sound beauty. It is not for humans.

Concision, precision, saying only what one needs to see and no
more. Vivid, accurate, precise. Verbs, not adjectives. -X and -I are
the equivalent of adjectives.

What do -L, -X, -i, and -H mean? These are not as cryptic as they may seem:
each one is what's called a command line argument, and they're in a standard
format. But remembering what each one actually means is likely to get harder
over time, unless one continually uses curl.

Doing this by hand over and over again can feel tedious, exaggerated, overly
verbose, not worth the return on effort. The value is the developer's time.




Idea: make the review Python runnable

from functools import partial
raw = partial(raw_input, "Press Enter for Next Paragraph.")
raw()
# how to run it online?
# ideone.com


Idea: distribute a tiny VM for VirtualBox for something like that 
