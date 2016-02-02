__author__ = 'ana'

import urllib
import json
import sys
from string_manipulation import string_handler


class Api_handler:
    @classmethod
    def start_call(cls):

        # API parameters
        options = {}
        options["url"] = "http://gallows.hulu.com/play"
        options["code"] = "ani.dachia@gmail.com"

        # API request URL
        REQUEST_URL = options["url"] + "?code=" + options["code"]

        try:
            r = urllib.urlopen(REQUEST_URL)
            data  = json.load(r)
            print data
            return data
        except Exception as e:
            print "Unable perform start request. %s" % e
            sys.exit(1)

    @classmethod
    def followup_call(cls, token, guess):

        # API parameters
        options = {}
        options["url"] = "http://gallows.hulu.com/play"
        options["code"] = "ani.dachia@gmail.com"
        options["token"] = token
        options["guess"] = guess

        # API request URL
        REQUEST_URL = options["url"] + "?code=" \
                      + options["code"] + "&token=" + options["token"] + "&guess=" + options["guess"]

        try:
            r = urllib.urlopen(REQUEST_URL)
            data  = json.load(r)
            return  data
        except Exception as e:
            print "Unable perform followup request. %s" % e
            sys.exit(1)