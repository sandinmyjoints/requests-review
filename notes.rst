=============================

The only thing DIAGRAM readers *might* care about is how programming is like
this thing they love, writing.

=============================

Writing and programming aren't all alike; they differ in how they deal with
reality. One denies it, the other embraces it. No, that's too simple: one
filters it, the other splats it all over the place. Good code captures the
essentials in a way that is both surprising and inevitable.

>>> type(response)
requests.models.Response

>>> type(response)
instance

Bugs
====

What is a bug? From a programmer's perspective, it is when the programmer's
mental model diverges from reality, from the way the program actually
works. If I know that x is a kind of integer, but I have made a mistake and
at some point x is actually a list of integers, then when I try to add 5 to
x, I will get a result that is not only not what I expected, it's
qualitatively different from what I expected; it's not the *kind* of result I
expected, and therefore my code from that point written for a single integer
is all going to be wrong for a list of integers. Until I figure out that bug,
I will be writing code that diverges from reality.

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

Expressive Power
================

Abstraction. Trading detailed knowledge at lower levels for greater
comprehension at higher levels.

Expressive power as compared to richness of language, ability to convey in fewest
words necessary, nothing wasted.

urllib2: need to do urlopen, then read each time. I may do this many times as I
try to get something right. Then figure out what the hell the response is.



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

curl is cryptic dense poetry. Not sure who. Thought of GMH but not sure about
that. Open to ideas.




Here's a terrible analogy, but it's the best I can do: this is kind of like if,
in a world where no one spoke English, a book was written that explained in detail
all the rules of English (in some other language, but really the analogy would
be better if it existed in another medium entirely, like if the rules of English
could be described by a system of smells): a few people would labor to
understand the book, and reduce it to smaller more useful themed bits that the
rest of us could use.



It strives to be explicit, complete, clear. The goal is to express oneself in
completion of a task. I want coherence, consistency, low friction between my
mind and the computer. I want to think in the way that I think naturally. I
don't think in terms of urlopeners and urlencoding. I think, I want to look at a
webpage, or get some data. Maybe I'll send some parameters.



I think this is what it comes down to. When I write or program, I know I'm
communicating with other minds. I inhabit them; I bridge the gap between
them. It makes me feel strongly. It makes me feel not alone.

I can feel my mind stretching when I consume a well put-together API or book--it
broadens the scope of what I know about the universe, about what it
possible.





Requests is
successful because it makes something quite messy in the details look simple and
easy.



Done well, writing and programming can produce works of minds mixing, sharing,
letting each other in. Of making sense of the world, existence. This is too
grandiose, but that is because I'm talking about the effect in sum. In parts it
is not always that way, but then at specific moments sometimes it is. When I use
Requests, a fine library with a well thought-out API that Reitz clearly put
thought and effort into. He has crafted an experience that an author could be
proud of.


Reading, writing, programming: solitary experiences that can lead to intense
feelings of other-knowledge, by virtue of shared mind-experience.





When Facebook gets your Instagram photos, the two computers are
   communicating thanks to APIs that were understood by human programmers who
   used that understanding to program the computers to talk to each other.

Skipping Over
=============

I'm skipping over oauth, which is the way programs prove to other programs that
they're allowed to do what they want to do. It's too technical. Requests is
flexible malleable pliant enough to allow a plugin that neatly abstracts oauth,
which is kind of a pain to deal with. I have no idea what the equivalent of that
is in literary terms; fan fiction comes to mind but that connotes totally the
wrong things and just really isn't a good equivalent at all.

Metaphor
========

We use metaphor all the time. The device you're reading this on is almost
certainly using metaphor, whether the desktop and files of a computer or the
buttons of a smartphone. If the metaphor is especially tied to a real life
object--like wood panelling--it's said to be skeumorphic. There's an entire
subculture of designers dedicated to ridiculing poorly though through instances
of this.

Time
====

My time is limited; the more time it takes me to tell the computer exactly how
to do what I want it to do, the less I can accomplish.



Utility, the Value of
=====================

Writing a novel for people to use, for those who will use it. Thinking ahead and
planning what they will see and experience. No one path through an API like a
novel. But not choose your own adventure either. Exponentially many ways of
using. More like multiverse.

An "improving book" like Jeeves is always reading. Horatio Alger.





Idea: make the review Python runnable

from functools import partial
raw = partial(raw_input, "Press Enter for Next Paragraph.")
raw()
# how to run it online?
# ideone.com


Idea: distribute a tiny VM for VirtualBox for something like that 
