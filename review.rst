===============
Requests 0.14.0
===============

by Kenneth Reitz
----------------

A Review for Curious Readers of DIAGRAM
=======================================

Reviewed by William John Bert

This is a review of Requests by Kenneth Reitz. Requests is not a novel or
memoir or book of poetry. It is a work of computer programming.

This may not be what you signed up for when you subscribed to DIAGRAM, or
visited DIAGRAM's website and clicked on this link. You may be thinking, "I'm
not a programmer. Why would I care?"

I'm a programmer, and a writer, and I think that there are interesting
affinities between programming and creative writing. Some people think
programming is pretty far from creativity. Typing away at a machine without a
soul. Obeying rules. Math. Logic. Nerds. [#]_

I think it's more complicated than that, and more interesting. (Of course, I'm
biased.) I'm going to look for those affinities while analyzing a piece of
software I use frequently. I'll do my best to explain what I'm talking about
without getting overly technical or bogged down in details. I hope that, in the
spirit of experiment, you'll join me.

Requests
--------

Requests is a tool for programming. It is designed to solve a problem.

So right away, we see that a tool is different from a work of art: functional,
purposeful, goal-driven. No one calls a poem or novel a tool. And I can't define
what art is, but I think it's fair to say that art doesn't set out to solve
problems. It's supposed to exist in and of itself, to provide an experience.

Requests is both a work and a way to make more work better.

But let's step back. What is a tool for programming? What does that mean? How
could it bear resemblance to creative writing?

The Problem
-----------

Programmers (or software engineers, coders, or hackers--we call ourselves lots
of things) are in a constant battle against complexity. Computers always do
precisely and only just what you tell them (frustrations with Microsoft Word
notwithstanding), and there are a staggering number of things they can do, which
means that we programmers must spell out in excruciating detail exactly what we
want them to do.

To manage that kind of complexity, we have rules.

As humans, evolved beings, we unconsciously filter the staggering possibilities
available to us . Human beings come with some built in rules (eat when hungry),
and easily learn more (don't touch hot stoves). Computers don't. We have to do
tell them exactly what to do, which choices to make. If we choose wrong, they do
what we told them to do: the wrong thing. Programming can be viewed as an effort
to build up sets of rules so as to direct the computer's action in a useful
direction, to do something helpful.

Staggering possibilities managed by rules--there's an affinity with natural
language. The difference is, with natural language, we've had lots of time to
deal with it. Our brains have evolved pockets that just do languagey stuff.

When it comes to programming, we're just getting started. Our brains need help.

Enter the API
-------------

If programming as an enterprise can be thought of as generating rules to make
computers do useful things, then Requests is a batch of rules that Reitz put
together to do something useful. To help others use Requests, Reitz put together
an API ("application program interface," but everyone just says "API"). APIs are
how programmers tell other programmers how to use what they've made. It
describes what Requests can do for me, and how I can make it do those things.

An API is inherently textual, something people read, like a manual or a
specification, but it's also more than that: it's a metonym for the
functionality it allows access to, whether an internet service like Twitter or a
programming library like Requests. It's a description of what the artifact of
programming can do and how to tell it to do that.

APIs are what make it possible to post your Instagram photos to your Facebook
timeline, checkin on Foursquare from your iPhone, book a flight on United from
Kayak, etc. Without APIs, without a way to share units of functionality with
each other, each programmer or programming team would be on its own. Everything
would take much, much longer; each programmer would have to reinvent the wheel.

Writers almost universally work alone. Programmers usually do, too. Writers
share their writing with each other, and the world--but not to be reused (though
influence is OK). Many programmers share their work, too, like what Reitz is
doing. Essentially, Reitz is saying, I solved this problem in a way I think
could be useful for you, too, so here you go, have at it. The difference is that
other people will incorporate Requests into their own work; it is both a work,
and a way to make other works. It will be, has been, mixed in to the very core
of many other programs. Its influence, in this way, is direct.

Making an API is an act of communication, connection, reaching out, offering
something one made to the world at large.

Here's an interesting bit of jargon: programmers say that somebody is "exposing
an API." It's an act of confidence, but also vulnerability.

APIs for Humans
---------------

Reitz's slogan is "APIs for humans." This is an ambitious, worthwhile, and
impossible goal. Humans are not computers [#]_, and vice versa. Yet humans want
to use computers to do some important things better and faster than they can do
without them.

Think people of, say, different genders, or different cultures, have trouble
communicating with each other? Try communicating with a machine. You have. You
do. It gives you trouble.

A motivation that runs throughout the short history of programming is making it
easier for humans to tell computers what to do, but ultimately we still end up
with rules written by humans for humans to read that describe how computers will
talk to other computers. Then humans other than the ones who wrote those rules
write programs to follow the rules, on the basis of promises that still more
programmers are doing the same, in the hopes that all will be able to
communicate to each other.

For example, one part of an important specification called HTTP, which defines
how computers talk to each other on the parts of the internet that you and I use
daily, says:

::

  The most common form of Request-URI is that used to identify a
  resource on an origin server or gateway. In this case the absolute
  path of the URI MUST be transmitted (see section 3.2.1, abs_path) as
  the Request-URI, and the network location of the URI (authority) MUST
  be transmitted in a Host header field. For example, a client wishing
  to retrieve the resource above directly from the origin server would
  create a TCP connection to port 80 of the host "www.w3.org" and send
  the lines:

         GET /pub/WWW/TheProject.html HTTP/1.1
         Host: www.w3.org

Without a full specification in minute detail, all programmers everywhere
wouldn't be able to agree on how the thing works, so they would make systems
that failed because they couldn't talk to each other [#]_; small and
not-so-small differences would crop up because of ambiguity, or unusual
situations not anticipated or addressed in the specification, or mistakes, or
faulty assumptions. Computers make zero assumptions of their own; they have a
way of making explicit every single one of yours.

The HTTP 1.1 specification is hundreds pages of dense imperative technical
jargon. Most people don't want to invest the time to even read it, let alone
understand it in full. But someone had to do it; someone had to translate it
into working code.

Code
----

Code is the term I will use for what programmers write. (In this sense, it's
always a collective noun: code, never codes.) Code is as varied as other forms
of human symbolic communication (like, say, writing), and it comes in a plethora
of languages, each of which brings its own stylistic choices.

A snippet of code from a language called Python [#]_ looks like this:

>>> import urllib2
>>> req = urllib2.Request('http://www.goodreads.com')
>>> response = urllib2.urlopen(req)
>>> response.read()

This snippet [#]_ uses Python's standard urllib2 library to retrieve Goodreads'
homepage, that is, all the HTML and CSS and JavaScript code that produces what
you see when you go to www.goodreads.com in your web browser [#]_.

Not for Human Consumption
-------------------------

What is ``response``, in this snippet? It is a type of variable called an
object; it represents data stored in the computer's memory. If I ask Python to
describe it, I get something like [#]_ this:

>>> response
<addinfourl at 4338521656 whose fp = <socket._fileobject object at 0x10297ce50>>

What the hell is that?

Expressive Power
----------------

Through Requests, Reitz exposes the same thing as:

>>> import requests
>>> response = requests.get("http://www.goodreads.com")

This ``response`` looks like:

>>> response
<Response [200]>

Maybe that doesn't look a whole lot better than what we saw from urllib2. The
request itself is two lines of code instead of four. Not a huge difference,
numerically. And what does that 200 mean?

To know what 200 means, you have to understand a bit of the HTTP 1.1 spec, which
says that 200 is a status code meaning, "That went OK". Out of the hundreds of
pages of HTTP 1.1, that is one of first things any web programmer learns.

The ``<addinfourl at 4338521656 whose fp = <socket._fileobject object at
0x10297ce50>>`` stuff from urllib? Clear as mud. ``fp`` probably means file
pointer, and a socket is a low-level abstraction for how computers talk to each
other, but to parse and really understand this response would require me to
spend some time spent looking around in documentation. I just wanted to get a
web page.

Natural language, as you probably know, offers tremendous expressive power: we
find it hard to conceive of thoughts that we can't express in it.

``requests.get`` is, say, Hemingway, or Strunk and
White. Declarative. Terse. Say what you mean as plainly as possible. 

urllib2's jumble is verbose, jargon, like legalese: heretofore, whereas, the
party of the first part, etc. Its API is a menagerie of abstractions with names
such as ``OpenerDirector`` and ``HTTPPasswordMgrWithDefaultRealm``. [#]_

These two ways of getting a web page are equivalent in functionality, but they
operate at very different levels of abstraction. We might say that because of
its higher level of abstraction, Requests has more expressive power than
urllib2.

What it's like to work with a bad API
-------------------------------------

You type a lot. You get annoyed. You say of whoever created the API, What were
they thinking?  You feel bogged down. You have to look up every little
thing. Nothing comes easy. You get a headache. You see a lot of code on the
screen and it doesn't seem to do much. You curse. You may bite or click
your nails, or maniacally tap your foot. You want to be doing something else.

What it's like to work with a really good API
---------------------------------------------

It's more than if DFW or Lori Moore or John Ashbery published a notebook of
exercises and prompts; it's as if they published part of their brain, so that
you too can run your thoughts through it, and have them upgraded. As you figure
out how to do what you set out to do, you realize other things that would also
be cool to do, and you find that the API has ways to do them, too! You think the
way someone else thought, and understand their thinking on a deep level. You
have a sense that we are all in this together, we're not so different.

The Four Verbs
--------------

The examples I've shown so far only scratch the surface; things get more
complicated when you want to send data, authenticate to prove your identity,
maintain a session so that a website knows you're the same person as you move
from page to page--all of which are necessary to do something interesting like
share a photo, or tweet.

The four verbs defined in the HTTP spec--the four verbs of the internet--are
get, post, put, and delete. They are responsible for, respectively, retrieving,
creating, updating, and deleting the digital representations that constitute our
online experiences, whether photos or likes or tweets or blog posts or anything
else.

Requests handles all four with aplomb, exposing them through a clean interface
that maps to how my mind thinks. urllib2 does not. I don't mean to beat up on
urllib2; it's older and was designed for a time when the internet was simpler
and functioned differently. The point I want to make is this: Requests and
urllib2 were written using the same language, Python, and technically have
nearly the same capabilities, but Requests was crafted in a way that manages and
abstracts away unnecessary details, the way a sculpture removes matter until
something meaningful remains. Requests is successful because it makes something
quite messy in the details look simple and easy, the way a novelist or poet
chooses detail to bring shape to an otherwise messy and undifferentiated
reality.

Dealing with Reality
--------------------

Programmers strive to be subtext-free. We are damn earnest. The code is tricky
enough. It is always trying to trip us up, making us question ourselves, driving
us crazy. Miss a comma or closing brace, and spend hours trying to find your
mistake. The computer forgives nothing. Good programmers deal with this by
making their own reality as clean as possible. 

If I write an app that tracks the books you've read, you've either read a book
or not, or perhaps you are currently reading it. In the app's universe, there's
no "I read a third of it, then put it down for a while," or "It's sitting in the
bathroom and I pick it up now and then," or "I stole it from a friend and now
Vanessa's borrowing it, I think." If I try to come up with a system to
programmatically encode every possible state of any person's relationship to
their book, I'll never get past this work to finish the app. This is how
programmers deal with reality: by cleaning it up.

When Austen begins, "It is a truth universally acknowledged, that a single man
in possession of a good fortune must be in want of a wife," she is not simply
stating a universal truth that she has identified. The sentence comes with
subtext: the truth is universal in the minds of some people, but not others, an
oxymoron, reinforced by the sentence's lack of an active subject. There is also
commentary on the relative power of men and women in her time. There is a
richness that demands and rewards repeated reading, offering readings as varied
as the number of people who read it.

Creative writing, literature, thrives on subtext, on creating shades of meaning
and multiple readings. Ambiguity and ellision and irony are techniques for
dealing with the messiness of reality.

When I type,

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

I am naming my variables clearly, according to what data they hold. I am
structuring the code in a way that indicates the flow of execution. Requests
helps me here: the final two lines that create a new session correspond to how I
think of creating a session: create an object that represents the session, then
start the session with the remote computer via HTTP. The equivalent in urllib2
would be much messier and more verbose.

I truly want future readers--myself and others--to understand exactly what that
code is doing, with no ambiguities. And there will be future readers. I'll be
re-reading it in six months when I want to add a new feature in another part of
the program and it breaks something here and I have to figure out why. Code,
like literature, is read far more than it is written.

Grok
----

Traditional programmer jargon has a word for understanding something with
"intimate and exhaustive knowledge": grok [#]_. It's from the language of the
Martians in Robert Heinlein's *Stranger in a Strange Land*, in which it means
literally "to drink" and metaphorically "to be one with."

In a novel or poem, you've been led to understanding and impression by a
succession of images and literary devices and experiences and revelations. In
programming, you are led to understanding by encountering problems, ways of
thinking about those problems and organizing them and 'grokking' them and
devising a solution.

Reitz groks HTTP and Python well, better than I ever will, as Austen grokked
marriage and power dynamics better than I ever will. Through exposure to their
works, I benefit from their experience of the world. In my own work of
programming and writing, I strive to match the understanding that they achieved.

Theory of Mind
--------------

Writers and programmers inhabit other minds.

Writers, of course, inhabit the minds of their characters, and of an implicit
reader of their work.

Programmers inhabit the minds of users. In Reitz's case, these are other
programmers (as opposed to, say, the programmers of Google Chrome, which is used
by non-programmers). Programmers might also be said to inhabit mind of the
computer itself.

This habitation of minds outside my own is part of what draws me to both these
pursuits. It is a challenge. It broadens my world. Thinking of others, as others
think, anticipating their needs and wants and questions, helps me escape myself
and gain perspective. It's invigorating! When I am programming or writing well,
in the flow, I experience a feeling of communing, of knowing what someone else,
another human being, thought or thinks or will think, felt or feels or will
feel, on a deep level. I feel part of something larger than myself.


Footnotes
---------

.. [#] This is a gross generalization, of course; a lot of creative people think
   otherwise.

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
   browsers, that's something you can do by looking under the "View" menu, if
   you're curious.

.. [#] These names are strikingly similar to the kinds of names that are common
   in another programming language you may have heard of, Java. Why that is is a
   whole other discussion that gets into very different philosophies about
   programming languages.

.. [#] I say "something like" because the exact numbers will vary on different
   computers and at different times of execution.

.. [#] The definition is from The Jargon File, a reference of programming jargon
   and lore: http://www.catb.org/jargon/html/G/grok.html    
