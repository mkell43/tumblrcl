import pytumblr

from auth import auth_tokens

tokens = auth_tokens()

client = pytumblr.TumblrRestClient(
    tokens['consumer_key'],
    tokens['consumer_secret'],
    tokens['oauth_token'],
    tokens['oauth_token_secret']
)


def info(blog):

    print client.blog_info(blog)


def posts(blog):

    print client.posts(blog)


def avatar(blog):

    print client.avatar(blog)


def likes(blog):

    print client.blog_likes(blog)


def followers(blog):

    print client.followers(blog)


def queue(blog):

    print client.queue(blog)


def submission(blog):

    print client.submission(blog)