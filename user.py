import pytumblr

from auth import auth_tokens

tokens = auth_tokens()

client = pytumblr.TumblrRestClient(
    tokens['consumer_key'],
    tokens['consumer_secret'],
    tokens['oauth_token'],
    tokens['oauth_token_secret']
)


def info():

    print client.info()


def dashboard():

    print client.dashboard()


def likes():

    print client.likes()


def following():

    print client.following()


def follow(blog):

    print client.follow(blog)


def unfollow(blog):

    print client.unfollow(blog)


def like(id, reblogkey):

    print client.like(id, reblogkey)


def unlike(id, reblogkey):

    print client.unlike(id, reblogkey)