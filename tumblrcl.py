#!/usr/bin/env python

import argparse
import argh

from auth import auth_create
import user
import blog


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    argh.add_commands(parser, [auth_create])
    argh.add_commands(parser,
                      [user.info, user.dashboard, user.likes, user.following, user.follow, user.unfollow, user.like,
                       user.unlike],
                      namespace='user',
                      title='Query user related information.')
    argh.add_commands(parser,
                      [blog.info, blog.posts, blog.avatar, blog.likes, blog.followers, blog.queue, blog.submission],
                      namespace='blog',
                      title='Query information from a specific Tumblr blog.')
    argh.dispatch(parser)