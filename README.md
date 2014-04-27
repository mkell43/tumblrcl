tumblrcl
========

Tool for interacting with Tumblr from the command line.

It really doesn't add any pretty printing of information, and is just a wrapper around
[pytumblr](https://github.com/tumblr/pytumblr).

Installation
------------

First clone or download the repo.  Then you will need to use PIP to first install my tumblrtokens package
found at https://github.com/mkell43/tumblrtokens.

Then you can run the following to install the rest of the requirements.

`pip install -r requirements.txt`

Using
-----

First you will need to register the application with Tumblr at
[http://www.tumblr.com/oauth/apps](http://www.tumblr.com/oauth/apps).

Then you'll need to run with tumblrcl is `./tumblrcl.py auth-create`, which will guide you through creating
the authentication file used by tumblrcl for connecting to Tumblr.

I may add a `first-run` option that will guide through the process of creating an application on Tumblr as well.

For right now all the data output is json.  I don't think I'll change that, so if you would like prettier output please
fork and just shoot me back a message so I can check it out.  If you'd like to send a pull request please feel free as
well.  If someone can find a way of nicely printing the output I'd reallyt like to see it.

TODO
----

1.  Need to add the post and tagged methods from pytumblr still.

2.  Add support for the additional params on the client.posts method.