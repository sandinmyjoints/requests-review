===============
Requests 0.14.0
===============

by Kenneth Reitz
----------------

Reviewed by William John Bert

Identification with another is addictive: some of my life's profound, memorable
experiences have come when something has bridged the physical gap between me and
another human. Because I'm a reader, this occurs across the distance of space
and time. It's happened with minor Chekov characters, and at the end of Kate
Mansfield stories. It happens over and again with Salinger and with George
Saunders. The author has pushed a character or an emotion through the page and
connected with me on a deep level: identification.

Identification happens with computer programming, too.

I say this as a reader, writer, and programmer: I experience identification when
reading and programming, and I strive to create it when writing and programming.

Though they deal with the messiness of reality differently, several techniques
common to both disciplines enable them to achieve this mental intimacy:
navigating complexity; avoiding pitfalls that inhibit communication; choosing
structure wisely; harness expressive power; and inhabiting other minds, The
Requests library, a work of computer programming by Kenneth Reitz, illustrates
this.

Navigating Complexity
---------------------

As humans, we've evolved to unconsciously filter the staggering possibilities
available to us at each moment. To manage that complexity, we have rules. Humans
come with some built in rules (eat when hungry), and easily learn more (don't
touch hot stoves) and more (don't lie, especially to those you love). When I'm
writing, my stories might examine how these rules come into conflict with each
other: a government doctor is ordered to a remote, neglected village, and comes
to value its people more than his duty to the government.

Computers don't come with built-in rules. When I'm programming, if I make a
mistake, the computer faithfully marches into it head-on. Computers do precisely
and only what you tell them (frustrations with Microsoft Word notwithstanding),
and because there are a staggering number of things they can do, programmers
constantly battle complexity, sometimes spelling out in excruciating detail
exactly what it is we want them to do. Programming is an effort to build up sets
of rules that direct the computer to do something helpful.

Staggering possibilities managed by rules: that's also a description of natural
language. The difference is, when it comes to natural language, we've had lots
of time to deal with it. Our brains have evolved pockets that just do languagey
stuff. When I write, I benefit from this history.

When it comes to programming, we're just getting started. Our brains need help.

Avoiding Pitfalls
-----------------

Misunderstandings and garbled messages kill identification before it can
begin. Grammar, punctuation, and even typing mistakes fatally divert attention
from what the writer is trying to say. Layout and space matter, too: linebreaks
are essential to poetry, and visual flow to longer narrative. Communication can
happen without them, but immersion comes more easily when nothing gets in the
way.

The stuff that programmers write, called code, can likewise be correct or
incorrect, beautiful or ugly. Requests is written in a programming language
called Python [#]_ that's known for being easy to read. Unusually for
programming languages, Python requires a certain amount of space between bits of
code, and its style guide encourages using even more space than required. Clear
and consistent names for built-in elements of the language that programmers
cannot change aid comprehension--not the case in every language. Reitz embraces
Python's style.

Structure
---------

Options for structure and sequence abound: writers order narrative
chronologically, *in media res*, or in more complex ways. Chapters can be short,
long, or ommitted. From Volumes and Parts to paragraphs and sentences, structure
matters.

Requests's parallel structure is typical of programming libraries: the code
itself, and a document that explains how to use the code. Within the code, there
are structures that are rough analogs of sentences, paragraphs, chapters, and
volumes, while the documentation is narrative, starting with easy things and
advancing to difficult material.

This bundle of code plus documentation is known as an *application programming
interface*, or simply *API*.

APIs are what make it possible to post your Instagram photos to your Facebook
timeline, checkin on Foursquare from your iPhone, book a flight on United from
Kayak, etc. Without APIs, without a way to share units of functionality with
each other, each programmer or programming team would be on its own. Everything
would take much, much longer; each programmer would have to reinvent the wheel.

Here's an interesting bit of jargon: programmers say that somebody is
"exposing an API." It's an act of confidence, but also vulnerability.

Expressive Power
----------------

The number of books to read is huge. Why would you choose one over another?  Why
might you read a literary novel over, say, a detective novel, or an author you
love over one you don't? One reason might be that while a thoughtful reader can
eke meaning from even the flimsiest of genre novels (sometimes even with great
satisfaction and enjoyment), we tend to find more significance in novels and
poetry that pack their sentences and stanzas with meaning, allusion, emotion,
and impact. We might call this *expressive power*.

The collection of programming libraries is also huge. To show how they vary in
expressive power, I need to introduce a bit of programming code.

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
``response``. When I'm programming, I'll want to do something useful with
``response``: save it to a file, show it to a user, parse it to see what books
are popular. If I ask Python to describe the
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
guesses about it, but to really understand it, I'd have to spend time rooting
around in documentation. I just wanted to get a web page.

This difference between the two libraries--their expressive power--plays out
over and over with the rest of their functionality (getting a webpage is just
scratching the surface).

``requests.get`` is Hemingway, or Strunk and White. Declarative. Terse. Say what
you mean as plainly as possible. Behind the scenes, its two lines are doing more
work than they seem, the way a good writer's sentences accomplish multiple
things at once: moving plot forward, imparting character, setting tone, painting
a scene.

urllib2's jumble is verbose jargon, like legalese: heretofore, whereas, the
party of the first part. Its API is a menagerie of abstractions with names
such as ``OpenerDirector`` and ``HTTPPasswordMgrWithDefaultRealm`` [#]_ that
have to be looked up to be understood, and are often underwhelming in their
capabilities.

Greater expressive power matches more closely the workings of my mind, where my
thoughts flow in a continuous stream. It's internal. I can't achieve
identification with a legal briefing. But with a novel or a good API, the pace
of meaning accelerates, syncing with my inner monologue, setting the stage for
identification.

Dealing with Reality
--------------------

Programmers strive to be subtext-free. The code is tricky enough. Miss a comma
or closing brace, and spend hours trying to find your mistake. The computer
forgives nothing. Good programmers deal with this by making reality as clean as
possible.

For example, within an app that tracks the books you've read, you've either read
a book or not, or perhaps you're currently reading it. There's no "I read a
third of it, then put it down for a while," or "I stole it from a friend and
almost finished it but now Vanessa's borrowing it, I think." A system that tried
to encode every possible state of any person's relationship to their books would
never be finished. This is how programmers deal with reality: by cleaning it up.

What I said above about Requests being like Hemingway isn't entirely accurate:
his clean prose belies a messy reality that is always present; meaning is often
unstated. Likewise, when Austen begins, "It is a truth universally acknowledged,
that a single man in possession of a good fortune must be in want of a wife,"
she is not simply stating a universal truth that she has identified. The
sentence comes with subtext: the truth is universal in the minds of some people,
but not others, an oxymoron, emphasized by the sentence's lack of an active
subject. There is also commentary on the relative power of men and women in her
time. Here is a richness that demands and rewards repeated reading, offering
interpretations as varied as the number of people who read it.

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

I aim to banish ambiguity. I name my variables clearly, according to what
data they hold. I structure the code to indicate the flow of execution. Requests
helps me here: the last two lines that create a new session correspond to how I
intuitively think of creating a session. The equivalent in urllib2 would be
messier and more verbose.

I want future readers--myself and others--to understand exactly what that code
is doing. Future readers are as sure a thing with code as with literature. [#]_
I'll be re-reading my code in six months when I add a new feature in another
part of the program and it suddenly breaks something here and I have to figure
out how they are connected.

What it's like to work with a bad API
-------------------------------------

You get annoyed. You say of whoever created it, What were they thinking?  You
feel bogged down. Nothing comes easy. You have to keep taking breaks. You feel
forgetful. You wonder if it's your fault, if you're missing something everyone
else sees. You get a headache. You curse. You may bite or click your nails, or
maniacally tap your foot. You want to be doing something else.

Grok
----

Programmers put so much value on understanding something with intimate and
exhaustive knowledge that traditional programmer slang has its own word for it:
*grok* [#]_. It's from the language of the Martians in Robert Heinlein's
*Stranger in a Strange Land*, in which it means literally "to drink" and
metaphorically "to be one with."

In a novel or poem, you've been led to understanding and impression by a
succession of images and literary devices and experiences and revelations. In
programming, you are led to understanding by encountering problems, ways of
thinking about those problems, organizing them, and finally grokking them well
enoguh to devise a solution.

Reitz groks Python and the internet well, better than I ever will, as Austen
grokked relationships and power dynamics better than I ever will. Through
exposure to their works, I benefit from their experience of the world. In my own
work of programming and writing, I strive to match the understanding that they
achieved.

Theory of Mind
--------------

Writers and programmers inhabit other minds.

Writers inhabit the minds of their characters and of readers of their work.

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

Identification is addictive. I seek it out, and I have an urge to spark it in
others. The difficulties of navigating complexity while avoid communication
pitfalls, of harnessing expressive power, and inhabiting other minds, make it
difficult to find and create. If I can ever achieve it in my own work--whether
writing or programming--it will be through studying--grokking--works like *Pride
and Prejudice*, and *Requests*.


Footnotes
---------

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

.. [#] I say "something like" because the exact numbers will vary on different
   computers and at different times of execution.

.. [#] These names are strikingly similar to the kinds of names that are common
   in another programming language you may have heard of, Java. Why that is is a
   whole other discussion that gets into very different philosophies about
   programming languages.

.. [#] An experience I've noticed that's common to writers and programmers is
   looking back at their own work and not recognizing it, with reactions ranging
   from admiration (How did I do that?) to disgust (What was I thinking?).

.. [#] This definition is taken from The Jargon File, a reference of programming
   jargon and lore: http://www.catb.org/jargon/html/G/grok.html
