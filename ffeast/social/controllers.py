#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright © 2013 Gabriel Falcão <gabriel@weedlabs.io>
#
from __future__ import unicode_literals
from flask import Blueprint, session, url_for, request, redirect
from flask_oauth import OAuth

from ffeast import settings

module = Blueprint('social', __name__)

oauth = OAuth()

twitter = oauth.remote_app(
    'twitter',
    base_url='https://api.twitter.com/1/',
    request_token_url='https://api.twitter.com/oauth/request_token',
    access_token_url='https://api.twitter.com/oauth/access_token',
    authorize_url='https://api.twitter.com/oauth/authenticate',
    consumer_key=settings.TWITTER_CONSUMER_KEY,
    consumer_secret=settings.TWITTER_CONSUMER_SECRET,
)


@twitter.tokengetter
def get_twitter_token(token=None):
    return session.get('twitter_token')


@module.route('/social/login')
def login():
    kw = {
        'next': request.args.get('next') or request.referrer or None
    }
    url = url_for('.oauth_authorized', **kw)
    absolute_url = settings.absurl(url)
    return twitter.authorize(callback=absolute_url)


@module.route('/social/handshake')
@twitter.authorized_handler
def oauth_authorized(resp):
    next_url = request.args.get('next') or url_for('web.index')
    if resp is None:
        print u'You denied the request to sign in.'
        return redirect(next_url)

    session['twitter_token'] = (
        resp['oauth_token'],
        resp['oauth_token_secret']
    )
    session['twitter_user'] = resp['screen_name']

    print 'You were signed in as %s' % resp['screen_name']
    return redirect(next_url)
