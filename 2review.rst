===============
Requests 0.14.0
===============

by Kenneth Reitz
----------------

Reviewed by William John Bert

Some of my life's profound, memorable experiences have been identification with
another human: bridging the physical gap between us. Because I'm a reader, this
can occur across the distance of space and time. It's happened with minor Chekov
characters, and at the end of Kate Mansfield stories. It happens over and again
with Salinger and with George Saunders. The author has pushed a character or an
emotion through the page and connected with me on a deep level: identification.

This happens with computer programming, too.

I say this as a reader, writer, and programmer: I experience identification when
reading and programming, and I strive to create it when writing and programming.

The two disciplines have several techniques in common that contribute to
achieving this mental intimacy: clearly communicating, navigating complexity,
harnessing expressive power, and inhabing other minds. They take different
apporaches to dealing with the messiness of reality: denial vs embracing. In the
right hands, they can produce great works that allow identification.

The Requests library, a work of computer programming by Kenneth Reitz,
illustrates some of these. I'll do my best to explain what I'm talking about,
using Requests as an example, without getting overly technical or bogged down in
details.

Prerequisites
-------------

Misunderstandings and garbled messages kill identification before it can
begin. Grammar, punctuation, and even typing mistakes divert attention from what
the writer is trying to say before anything meaningful can happen. Layout and
space matter, too: linebreaks are essential to poetry, and visual flow to long
narrative. Communication can be achieved without them, but immersion comes more
easily when nothing gets in the way.

The stuff that programmers write, called code, can likewise be correct or
incorrect, beautiful or ugly. Requests is written in a programming language
called Python [#]_ that's known for being easy to read. Unusually for
programming languages, Python requires a certain amount of space between bits of
code, and its style guide encourages using even more space than required. Clear
and consistent names for the elements of the language that are built-in and
cannot be changed by the programmer contribute to comprehension--not the case in
every language. Reitz embraces Python's style.

Programs and writings rely on structure and sequence for understanding and
comprehension. Options abound: writers structure narrative chronologically, in
media res, or in other ways. Chapters can be short, long, or ommitted. Structure
applies at the gross, high level of Volumes, Parts, as well as in the small with
paragraphs and sentences.

Requests has a parallel overall structure, typical for libraries that are
shared: the code itself, and a document that explains how to use the code. Reitz
lays out the code in modules, roughly akin to chapters, some a few lines long,
some hundreds, each one following a theme: dealing with security, sessions,
cookies. This is one of the ways he manages the library's underlying complexity
(more on that in a moment).

Documentation is inherently textual, sort of like a manual or a
specification. Reitz provides both a narrative version that starts with easy
things and advances to more difficult material, and a reference document that
explains particulars in detail, with examples.

This bundle of code plus documentation is known as an *application programming
interface*, or simply *API*. Making an API is an act of communication,
connection, reaching out, offering something one made to the world at
large.

APIs are what make it possible to post your Instagram photos to your Facebook
timeline, checkin on Foursquare from your iPhone, book a flight on United from
Kayak, etc. Without APIs, without a way to share units of functionality with
each other, each programmer or programming team would be on its own. Everything
would take much, much longer; each programmer would have to reinvent the wheel.

Here's an interesting bit of jargon: programmers say that somebody is
"exposing an API." It's an act of confidence, but also vulnerability.

Navigating Complexity
---------------------

As humans, we have evolved to unconsciously filter the staggering possibilities
available to us at each moment. To manage that complexity, we have rules. Humans
come with some built in rules (eat when hungry), and easily learn more (don't
touch hot stoves) and more (don't lie, especially to those you love). When I'm
writing, my stories might examine how these rules come into conflict with each
other: a doctor is sent by his government to a doomed, forgotten village, and
comes to value its people more than his duty to the government.

Computers don't come with built in rules. When I'm programming, if I make a
mistake, the computer makes a mistake. Programmers constantly battle
complexity. Computers do precisely and only what you tell them (frustrations
with Microsoft Word notwithstanding). There are a staggering number of things
they can do, though, which means that programmers must spell out in excruciating
detail exactly what we want them to do. Programming is an effort to build up
sets of rules that direct the computer to do something helpful.

Staggering possibilities managed by rules are also available to us in another
way: natural language. The difference is, with natural language, we've had lots
of time to deal with it. Our brains have evolved pockets that just do languagey
stuff. When I write, I benefit from this history.

When it comes to programming, we're just getting started. Our brains need help.

Expressive Power
----------------

The number of books to read is huge. Why would you choose one over another?
Well, why would you read literary novels over, say, detective novels, or an
author you love over one you hate? One reason might be that while a thoughtful
reader can eke meaning from even the flimsiest of pulp novels (and great
satisfaction and enjoyment, too), we tend to find more significance in novels
and poetry that pack their sentences and stanzas with meaning, allusion,
emotion, and impact. We might call this *expressive power*.

The collection of programming libraries available is also huge. Programming
libraries also vary in expressive power. To show that, I need to introduce a bit
of programming code.

>>> import urllib2
>>> req = urllib2.Request('http://www.goodreads.com')
>>> response = urllib2.urlopen(req)
>>> response.read()

This snippet [#]_ is the standard way to retrieve a webpage (specifically,
Goodreads' homepage) using a Python library called urllib2. Requests does the
same thing this way:

>>> import requests
>>> response = requests.get("http://www.goodreads.com")

Requests' code is two lines instead of four. That might not seem like a big
difference from urllib2, but note it, and bear with me just a bit longer. Both
these snippets store the webpage they've retrieved in a variable called
``response``. When I'm programming, I will want to do something with
``response``: save it to a file, show it to a user, parse it to see what books
are popular: do something useful with it. If I ask Python to describe the
``response`` returned by urllib2, I get something like [#]_ this:

>>> response
<addinfourl at 4338521656 whose fp = <socket._fileobject object at 0x10297ce50>>

The ``response`` that Requests gives me, on the other hand, looks like:

>>> response
<Response [200]>

Again, Requests is smaller, and it turns out its two lines of code give me
something much more useable than urllib2. ``Response [200]`` is meaningful; one
of the first things every web programmer learns is that 200 means, simply,
"OK". Requests lets me know my code succeeded.

The thing that urllib2 gave me, ``<addinfourl at 4338521656 whose fp =
<socket._fileobject object at 0x10297ce50>>``, is clear as mud. I can make some
guesses about it, but to really understand I'd have to spend some time spent
looking around in documentation. I just wanted to get a web page.

This difference between the two libraries plays out over and over with the rest
of their functionality (getting a webpage is just scratching the surface). The
difference is their expressive power.

``requests.get`` is Hemingway, or Strunk and White. Declarative. Terse. Say what
you mean as plainly as possible. Behind the scenes, its two lines are doing more
work than they seem, the way a good writer's sentences accomplish multiple
things at once: moving plot forward, imparting character, setting tone, painting
a scene.

urllib2's jumble is verbose jargon, like legalese: heretofore, whereas, the
party of the first part. Its API is a menagerie of abstractions with names
such as ``OpenerDirector`` and ``HTTPPasswordMgrWithDefaultRealm`` [#]_ that
have to be looked up to be understood, and are often underwhelming in their
capability.

High expressive power matches more closely the inner workings of my mind, where
my thoughts flow in a continuous stream. It's internal. I do not achieve
identification with a legal briefing. But with a novel, or a good API, the pace
of meaning accelerates, more closely matching my inner monologue, setting the
stage for identification.



Writing and programming aren't all alike; they differ in how they deal with
reality. One denies it, the other embraces it. No, that's too simple: one
filters it, the other splats it all over the place. Good code captures the
essentials in a way that is both surprising and inevitable.

Dealing with Reality
--------------------

Programmers strive to be subtext-free. The code is tricky enough. Miss a comma
or closing brace, and spend hours trying to find your mistake. The computer
forgives nothing. Good programmers deal with this by making their own reality as
clean as possible.

For example, take an app that tracks the books you've read. Within it, you've
either read a book or not, or perhaps you're currently reading it. There's no
"I read a third of it, then put it down for a while," or "It's sitting in the
bathroom and I pick it up now and then," or "I stole it from a friend and now
Vanessa's borrowing it, I think." A system that tried to encode every possible
state of any person's relationship to their book would never be finished. This
is how programmers deal with reality: by cleaning it up.

What I said above about Requests being like Hemingway isn't entirely accurate:
Hemingway's meanings are unstated. Likewise, when Austen begins, "It is a truth
universally acknowledged, that a single man in possession of a good fortune must
be in want of a wife," she is not simply stating a universal truth that she has
identified. The sentence comes with subtext: the truth is universal in the minds
of some people, but not others, an oxymoron, reinforced by the sentence's lack
of an active subject. There is also commentary on the relative power of men and
women in her time. Here is a richness that demands and rewards repeated
reading, offering interpretations as varied as the number of people who read it.

When I write a story, I thrive on subtext, on creating shades of meaning and
multiple readings. Ambiguity and ellision and irony are my techniques for
dealing with the messiness of reality. But when I type:

.. code-block::

  import requests, config
  user = config.user
  host = config.host
  url = "/api/login"
  data = {
    "email": user['email'],
    "password": user['password']
  }
  session = requests.Session()
  session.post(host+url, data=data)

I'm trying to banish ambiguity. I'm naming my variables clearly, according to
what data they hold. I'm structuring the code to indicate the flow of
execution. Requests helps me here: the last two lines that create a new session
correspond to how I intuitively think of creating a session. The equivalent in
urllib2 would be much messier and more verbose.

I want future readers--myself and others--to understand exactly what that code
is doing. Future readers are as sure a thing with code as with literature. I'll
be re-reading this in six months when I want to add a new feature in another
part of the program and it breaks something here and I have to figure out
why.

What it's like to work with a bad API
-------------------------------------

You get annoyed. You say of whoever created it, What were they thinking?  You
feel bogged down. Nothing comes easy. You have to keep taking breaks. You feel
forgetful. You wonder if it's your fault, if you're missing something everyone
else sees. You get a headache. You curse. You may bite or click your nails, or
maniacally tap your foot. You want to be doing something else.

Grok
----

Programmers so highly value understanding something with intimate and exhaustive
knowledge that traditional programmer slang has its own word for it: *grok*
[#]_. It's from the language of the Martians in Robert Heinlein's *Stranger in a
Strange Land*, in which it means literally "to drink" and metaphorically "to be
one with."

In a novel or poem, you've been led to understanding and impression by a
succession of images and literary devices and experiences and revelations. In
programming, you are led to understanding by encountering problems, ways of
thinking about those problems and organizing them and grokking them and
devising a solution.

Reitz groks Python and the internet well, better than I ever will, as Austen
grokked marriage and power dynamics better than I ever will. Through exposure to
their works, I benefit from their experience of the world. In my own work of
programming and writing, I strive to match the understanding that they achieved.

Theory of Mind
--------------

Writers and programmers inhabit other minds.

Writers inhabit the minds of their characters, and of an implicit reader of
their work.

Programmers inhabit the minds of users. In Reitz's case, these are other
programmers (as opposed to, say, the programmers of Google Chrome, which is used
by non-programmers). Programmers might also be said to inhabit mind of the
computer itself.

This habitation of minds outside my own is part of what draws me to both these
pursuits. It is a challenge. It broadens my world. Thinking of others, as others
think, anticipating their needs and wants and questions, helps me escape myself
and gain perspective. It's invigorating!

What it's like to work with a great API
---------------------------------------

It's more than if Lori Moore or John Ashbery published a notebook of exercises
and prompts; it's as if they published part of their brain, so that you too can
run your thoughts through it, and have them upgraded. As you figure out how to
do what you set out to do, you realize other things that would also be cool to
do, and you find that the API has ways to do them, too! You think the way
someone else thought, and understand their thinking on a deep level. You have a
sense that we are all in this together, we're not so different.

Identification
--------------

Successfully inhabiting other minds, when combined with clear communication, an
atmosphere of complexity, dealing with reality, and high expressive power, leads
to identification.

When I am programming or reading something extraordinary, I experience a feeling
of communing, of knowing what someone else, another human being, thought or
thinks or will think, felt or feels or will feel, on a deep level. I feel part
of something larger than myself. This is identification.

If I can ever achieve it in my own work, which would be a huge accomplishment,
it will be through studying works like *Pride and Prejudice*, and *Requests*.




Footnotes
---------

.. [#] Though they used to be; see: http://en.wikipedia.org/wiki/Human_computer

.. [#] It's a miracle to me that they do; imagine trying to sync up millions of
   people, some smart, some not so smart, some opinionated, some
   indifferent. HTTP is successful where many, many other attempts at protocols
   have failed.

.. [#] As in Monty Python, not the snake genus.

.. [#] What does this all mean?

   Three greater-than signs (>>>) is called a prompt, as in Python is prompting
   me to give it something to do. The rest of the line after it is what I
   type. So this:

   >>> requests.get("www.goodreads.com")
   <Result [200]>

   is really this little dialog:

   Python: I'm ready! Give me something to do.

   Me: Retrieve this webpage, www.goodreads.com, for me.

   Python: OK, did that, here's what I got.

   Writing out prompt/command/result is a common way for programmers to give
   each other examples: this is what I did; this is what I got; if you do the
   same, you should get the same result.

.. [#] You would see the same code if you view source in your browser. In most
   browsers, that's something you can do by looking under the "View" menu.

.. [#] These names are strikingly similar to the kinds of names that are common
   in another programming language you may have heard of, Java. Why that is is a
   whole other discussion that gets into very different philosophies about
   programming languages.

.. [#] I say "something like" because the exact numbers will vary on different
   computers and at different times of execution.

.. [#] The definition is from The Jargon File, a reference of programming jargon
   and lore: http://www.catb.org/jargon/html/G/grok.html
