#!/usr/bin/env python
# -*- coding: utf-8 -*-

from google.appengine.ext import db
from google.appengine.api import memcache

class AppKey(db.Model):
    """Consumer key and secret."""
 
    consumer_key = db.StringProperty()
    consumer_secret = db.StringProperty()

    @staticmethod
    def getAppKey():
        appkey=memcache.get("appkey" , namespace="appkey")
        if appkey is None:
            appkey = AppKey.all().get()
            if appkey is None:
                raise ValueError("have not consumer key")
            memcache.set("appkey", appkey, namespace="appkey")
        return appkey


class OAuthToken(db.Model):
    """OAuth Token."""
 
    jid = db.StringProperty()
    request_token = db.StringProperty()
    request_token_secret = db.StringProperty()
    access_token = db.StringProperty()
    access_token_secret = db.StringProperty()
    created = db.DateTimeProperty(auto_now_add=True)
    last_fetch = db.IntegerProperty()
 
    @staticmethod
    def getOAuthToken(jid):
        token=memcache.get(jid , namespace="token")
        if token is None:
            token = OAuthToken.all().filter("jid",jid).get()
            if token is None:
                token = OAuthToken(jid=jid)
                token.put()
            memcache.set(jid, token,namespace="token")
        return token

    @staticmethod
    def findby_request_token(token):
        return OAuthToken.all().filter("request_token", token).get()

    def update_request_token(self, key, secret):
        self.request_token=key
        self.request_token_secret=secret
        self.put()
        memcache.set(self.jid, self,namespace="token")

    def update_access_token(self, key, secret):
        self.access_token=key
        self.access_token_secret=secret
        self.put()
        memcache.set(self.jid, self,namespace="token")

