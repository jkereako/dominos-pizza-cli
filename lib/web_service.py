#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import urllib2

# @see: https://github.com/kdamage/IndividualCode/blob/master/CloudStack%20API%20Signing%20Class/SignedAPICall.py
dominos_api_base_url = "https://order.dominos.com/power/"
dominos_tracker_base_url = "https://trkweb.dominos.com/orderstorage/GetTrackerData?"

# self.locator = DOMINOS_API_BASE_URL + "store-locator?s={street_name}&c={zip_code}"
# self.profile = DOMINOS_API_BASE_URL + "store/{store_id}/profile"
# self.menu = DOMINOS_API_BASE_URL + "store/{store_id}/menu?lang={lang}&structured=true"
# self.validate_order = DOMINOS_API_BASE_URL + "validate-order"
# self.price_order = DOMINOS_API_BASE_URL + "price-order"
# self.place_order = DOMINOS_API_BASE_URL + "place-order"
class WebService(object):
    def __init__(self, url, args):
        query_string = urllib.urlencode(args)
        self.request = urllib2.Request(url + '?' + query_string)

    def _json_request(self):
        self.request.add_header('Accept', 'application/json')
        self.request.add_header('Content-Type', 'application/json')

    def _soap_request(self):
        self.request.add_header('Accept', 'application/soap+xml')
        self.request.add_header('Content-Type', 'application/soap+xml')

    def make_request(self):
        self._json_request()
        print self.request.get_method()
        print self.request.get_full_url()

        try:
            self.response = urllib2.urlopen(self.request)
            print self.response.read()
        except Exception as e:
            print e.reason


#api = DominosPizza(api_url)

#request = {'s': 'BIRCH ST', 'c':'01945'}
#result = api.fetchAllStores(request)
#print "count", result['count']
#print "api url", api.value
