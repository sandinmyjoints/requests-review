===============
Requests 0.14.0
===============

by Kenneth Reitz
----------------

Reviewed by William John Bert

This is a review of "Requests" by Kenneth Reitz. Requests is not a novel or
memoir or book of poetry. It is a work of computer programming.

This may not be what you signed up for when you subscribed to Diagram, or
visited Diagram's website and clicked on this link. You may be thinking, "I'm
not a programmer. Why would I care?" 

I'm a programmer, and a writer, and I think that there are interesting
affinities between programming and creative writing. A lot of people think
programming is about as far from creativity as you can get. Typing away at a
machine without a soul. Obeying rules. Math. Nerds.

I think it's more complicated than that. More interesting. (Of course, I'm
biased.) So I'm going to try to find out what those affinities, but I won't shy
away from difference. I'll do my best to explain what I'm talking about without
getting too technical or bogged down in details. I hope that, in the spirit of
experiment, you'll join me.

Requests
========

Requests is a tool that Reitz made for other programmers. He thinks could make
other people's lives easier, could enable other people to their work better,
faster, easier, and therefore do better work.

So right away, we see that a tool is different from a work of art. Requests is
both a work and a way to make more work better.

But let's step back. What is a tool for programming? What does that mean? How
could it bear resemblance to creative writing?

The Problem
===========

Programmers (or software engineers, coders, or hackers--we call ourselves lots
of things) are in a constant battle against complexity. Computers always do
precisely and only just what you tell them (take my word for it, despite the
frustrations Microsoft Word cause you!), you must often spell in excruciating
detail exactly what you want them to do. There are millions and millions of
possibilities of what to do. As humans, evolved beings, we filter out all these
possibilities. Computers don't do that. We have to do tell them exactly what to
do, which choices to make. If we choose wrong, they do what we told them to do:
the wrong thing.

Infinite possibilities--now there's an affinity with natural language. The
difference is, with natural language, we've had lots of time to deal with
it. Our brains have evolved pockets that just do languagey stuff.

When it comes to programming, we're just getting started. Our brains need help.

What's an API?
==============

To help others use Requests, Reitz did a lot of programming and put together an
API ("application program interface," but everyone just says "API"). APIs are
how programmers tell other programmers how to use what they've made[#]_. It describes
what Requests can do for me, and how I can make it do those things.

An API is inherently textual. It's something people read. Like a manual or a
specification, but more than that: we also use the term as metonymy for the
functionality it allows access to, whether an internet service like Twitter or a
programming library like Requests. It's a description of what the artifact of
programming can do and how to tell it to do that.

Without APIs, there would be no mashups, no posting your Instagram photos to
your Twitter feed or what have you.

Without APIs, without a way to share units of functionality with each
other, each programmer or programming team would be on its own. Everything would
take much, much longer; each programmer would have to reinvent the wheel.

Here are some points of comparison between writing and programming: writers
almost universally work alone. Programmers usually do, too. Writers share their
writing with each other--but not to be reused. Though influence is OK. Writers
don't do mashups. Many programmers share their work with other programmers, like
what Reitz is doing. Essentially, Reitz is saying, I solved this problem in a
way I think could be useful for you, too, so here you go, have at it.

That is releasing an API. Releasing an API is an act of communication,
connection, reaching out, offering something one made to the world at large.

Here's an interesting bit of jargon: programmers say that somebody is "exposing
an API." It's an act of confidence, and also vulnerability.

APIs for Humans
===============

Humans are not computers[#]_, and vice versa, yet humans want to use
computers to do some important things better and faster than they can do without
them.

Think people have trouble communicating with each other? Try communicating
with a machine. You have. You do. It gives you trouble.

Reitz's slogan is "APIs for humans." This is an ambitious, worthwhile, and
impossible goal.

A motivation that runs throughout the short history of programming is making it
easier for humans to tell computers what to do, but ultimately we still end up
with rules written by humans for humans to read describing how computers will
talk to other computers. Then humans other than the ones who wrote those rules
write programs to follow the rules, on the basis of promises that still more
programmers are doing the same, in the hopes that all will be able to
communicate to each other.

When Facebook gets your Twitter feed, the two computers are communicating thanks
to APIs that were understood by human programmers who used that understanding
to program the computers to talk to each other.

For example, one part of the HTTP 1.1 specification, the spec that defines
how computers talk to each other on the parts of the internet that you and I use
daily, says:

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

Without the full specification in minute detail, all programmers everywhere
wouldn't be able to agree on how the thing works, so they would make systems
that failed because they couldn't talk to each other[#]_; small and not-so-small
differences would crop up because of ambiguity, or unusual situations not
anticipated or addressed in the specification, or mistakes, or faulty
assumptions. (Computers make zero assumptions of their own; they have a way of
making explicit every single one of yours.)

The HTTP 1.1 specification is hundreds pages of dense imperative technical
jargon. Most people don't want to invest the time to even read it, let alone
understand it in full. Someone has to do it.

Here's a terrible analogy, but it's the best I can do: this is kind of like if
no one were born knowing English, but a book existed that explained in detail
all the rules of English (in some other language, but really the analogy would
be better if it existed in another medium entirely, like if the rules of English
could be described by a system of smells): a few people would labor to
understand the book, and reduce it to smaller more useful themed bits that the
rest of us could use.

That is the act of someone translating a spec such as HTTP into working code.

Code
====

Code is the term I will use for what programmers write. (In this sense, it's
always a collective noun: code, never codes.) Code is as varied as
other forms of human symbolic communication (like, say, writing), and it comes
in a plethora of languages, each of which brings its own stylistic choices.

A snippet of code from a language called Python[#]_ looks like this:

>>> import urllib, urllib2
>>> req = urllib2.Request('http://www.goodreads.com')
>>> response = urllib2.urlopen(req)
>>> response.read()

This retrieves Goodreads' homepage, that is, all the HTML and CSS and JavaScript
code that produces what you see when you go to www.goodreads.com in your web
browser[#]_.

Not for Human Consumption
=========================

What is `response`? It is a variable, a bit of data that looks something
like[#]_: `<addinfourl at 4338521656 whose fp = <socket._fileobject object at
0x10297ce50>>`

What the hell is that?

Expressive Power
================

Reitz exposes the same thing to us, humans, as:

>>> import requests
>>> response = requests.get("http://www.goodreads.com")

This `response` looks like: `<Response [200]>`

Maybe that doesn't look much better than urllib or curl. It's two lines of code
instead of four. Not a huge difference, perhaps. And what does 200 mean?

To know what 200 means, you have to understand a part of the HTTP 1.1 spec. It
says that 200 means, "That went OK". Out of the hundreds of pages of HTTP 1.1,
that is one of first things any programmer learns. The `<addinfourl at
4338521656 whose fp = <socket._fileobject object at 0x10297ce50>>` stuff from
above? Not nearly as clear. Probably requires some time spent looking around in
documentation.

Natural language, as you probably know, offers tremendous expressive power: we
find it hard to conceive of thoughts that we can't express in it.

`request.get` is, say, Hemingway: The fish tasted excellent. It's Strunk and
White: say what you mean as plainly as possible.

urllib2's jumble is verbose, technically correct academic English, or legalese:
heretofore, whereas, it is wanted, etc

curl is cryptic dense poetry. Not sure who. Thought of GMH but not sure about
that. Open to ideas.

We might say Requests has more expressive power than urllib2. We might not.

There is less friction between what I want to do with requests than urllib2.

What it's like to work with a bad API
=====================================

If that API is a mismatch with your way of thinking, you get frustrated,
annoyed, bitter. You keep saying, It should do this, or HOw can it not do that?
or What were they thinking? You feel bogged down. You have to look up every
little thing. Nothing comes easy. You get a headache. You curse. You may bite or
click your nails, or maniacally tap your foot. You want to be doing something
else. 

What it's like to work with a good API
==================================

It's more than if DFW or Lori Moore or John Ashbery released a notebook of
exercises and prompts. It's as if they released part of their brain, so that you
too could run your thoughts threw it.

You think the way someone else thought. You have a sense that we are all in this
together, we're not so different.

Requests exposes the four verbs of HTTP: get, post, put, and delete. Those four
actions make up the vast majority of your use of the internet. They are
responsible for creating, retrieving, updating, and deleting the representations
of your online experience. Requests makes them easier to use than urllib2.

What I have shown only scratches the surface; I'm not going to show more because
the background needed to explain what it is too much.

Dealing with Reality
====================

Programming strives to be subtext-free. We are damn earnest. The code is tricky
enough. It is always trying to trip us up, making us question ourselves, driving
us crazy. Miss a comma and spend hours trying to find it. The computer forgives
nothing.

It strives to be explicit, complete, clear. The goal is to express oneself in
completion of a task. I want coherence, consistency, low friction between my
mind and the computer. I want to think in the way that I think naturally. I
don't think in terms of urlopeners and urlencoding. I think, I want to look at a
webpage, or get some data. Maybe I'll send some parameters.

Literature, creative writing, has subtext. It strives to create an effect in an
of itself, multiple readings, shades of meaning, getting beneath what is said to
get to reality.

Programmers strive to make their own clean reality. Every program is its own
little universe, perhaps mixing in other universes to make it.

If I write an app that tracks the books, you've read, you've either read a book
or not, or perhaps you are currently reading it. In the app's universe, there's
no "I read a third of it, then put it down for a while," or "It's sitting in the
bathroom and I pick it up now and then," or "I stole it from a friend and now
Vanessa's borrowing it, I think."

This is a fundamental difference between the forms.

When Austen begins, "It is a truth universally acknowledged...", we know that
what she is saying is not simply that she has identified a universal
truth. There is subtext about how different people want different things, and a
comment on the relative power of men and women in her time.

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

I truly want future readers--myself and others--to understand exactly what that
code is doing, with no ambiguities.

Theory of Mind
==============

Programmers have to inhabit other minds: other programmers (target audience),
users, developers of the libraries and APIs they're using; the computer itself.

These are characters.

Writers have to inhabit the minds of their characters. And the audience.

A sensation, a feeling, a sense I get in common from both writing and
programming: a sense of communing, of knowing what someone else, another human
being, thought and felt on a deep level. Empathy? Sharing a brain experience.

In a novel or poem, you've been led to it by a succession of images and literary
devices and experiences and revelations.

In programming, you've encountered the same problems, the same ways of thinking
about those problems and organizing them and 'grokking' them and grokking a
solution.

Reading, writing, programming: solitary experiences that lead to intense
feelings of community, by virtue of shared mind-experience,

I think this is what it comes down to. When I write or program, I know I'm
communicating with other minds. I inhabit them; I bridge the gap between
them. It's invigorating. It makes me feel strongly. It makes me feel not alone.

Done well, it is a work of minds mixing, sharing, letting each other in. Of
making sense of the world, existence. This is too grandiose, but that is because
I'm talking about the effect in sum. In parts it is not always that way, but
then at specific moments sometimes it is. I can feel my mind stretching when I
consume a well put together API or book--it broadens the scope of what I know
about the universe, about what it possible. 

Requests is a fine library with a well thought out API that I know Reitz put
thought and effort into. It solves problems. It is not a work of creative
writing, but it has some affinities with such.

Footnotes
=========

.. [#] What does this all mean?
   >>> is Python telling me, "I'm ready for you to give me something to
       do," called a prompt. So when I write:

   >>> request.get
   <Result >

   It's this dialog:

   Python: Give me something to do (>>>)

   Me: request.get

   Python: Here's what that resulted in (<Result >)

   This is a common way for programmers to explain things to each. This is what
   I did; this is what I got; if you do the same, you should get the same
   result.



.. [#] What is a bug? From a programmer's perspective, it is when the programmer's
   mental model diverges from reality, from the way the program actually
   works. If I know that x is a kind of integer, but I have made a mistake and
   at some point x is actually a list of integers, then when I try to add 5 to
   x, I will get a result that is not only not what I expected, it's
   qualitatively different from what I expected; it's not the *kind* of result I
   expected, and therefore my code from that point written for a single integer
   is all going to be wrong for a list of integers. Until I figure out that bug,
   I will be writing code that diverges from reality.


.. [#] Though they used to be; see: http://en.wikipedia.org/wiki/Human_computer

.. [#] As in Monty Python, not the snake genus.

.. [#] You would see the same code if you view source in your browser. In most
   browsers, that's something you can do by looking under the "View" menu.

.. [#] Confusingly, API is also a term used to describe how computers talk to
   each other. It's kind of an umbrella term to express the idea of how to
   interact with a system.

.. [#] It's a miracle to me that they do; imagine trying to sync up millions of
   people, some smart, some not so smart, some opinionated, some
   indifferent. HTTP is successful where many, many other attempts at protocols
   have failed.

.. [#] I say "something like" because the exact numbers will vary on different
   computers and at different times of execution.
