#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import urllib2

class WebService(object):
    def make_request(self):
        try:
            self.response = urllib2.urlopen(self.request)
            print self.response.read()
        except Exception as e:
            print e.reason

class GetRequest(WebService):
    def __init__(self, url, args):
        query_string = urllib.urlencode(args)
        self.request = urllib2.Request(url + '?' + query_string)

class PostRequest(WebService):
    def __init__(self, url, args):
        self.request = urllib2.Request(url, args)
        self.request.add_header('Content-Type', 'application/x-www-form-urlencoded')
