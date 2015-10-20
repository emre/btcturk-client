# -*- coding: utf-8 -*-

import urlparse
import requests
import urllib
import time
import hashlib
import hmac
import base64

from tools import authenticated_method


class Btcturk(object):

    API_BASE_URL = "https://www.btcturk.com/api/"

    def __init__(self, api_key=None, private_key=None):
        self.api_key = api_key
        self.private_key = private_key

    def _generate_url(self, action, query_string=None):

        if query_string:
            if not isinstance(query_string, dict):
                raise TypeError("query_string variable should be a dictionary.")

        if query_string:
            action = "{}/?{}".format(action, urllib.urlencode(query_string))

        abs_url = urlparse.urljoin(self.API_BASE_URL, action)

        return abs_url

    def _get_auth_headers(self):

        if not self.api_key or not self.private_key:
            raise ValueError("api key and private key are both required.")

        # api key (public key)
        headers = {
            "X-PCK": self.api_key,
        }

        # timestamp
        stamp = str(int(time.time()))
        headers["X-Stamp"] = stamp

        # concat the public key and timestamp.
        data = "{}{}".format(
            self.api_key,
            stamp,
        )

        # private_key - convert from base64
        private_key = base64.b64decode(self.private_key)

        # get the signature
        signature = hmac.new(private_key, data, hashlib.sha256).digest()
        headers["X-Signature"] = base64.b64encode(signature)

        return headers

    def ticker(self):
        response = requests.get(self._generate_url("ticker"), verify=False)

        return response.json()

    def trades(self, since_id=None):
        if since_id:
            response = requests.get(self._generate_url("trades", {"sinceid": since_id}), verify=False)
        else:
            response = requests.get(self._generate_url("trades"), verify=False)

        return response.json()

    def orderbook(self):
        response = requests.get(self._generate_url("orderbook"), verify=False)

        return response.json()

    @authenticated_method
    def balance(self):
        response = requests.get(
            self._generate_url("balance"),
            headers=self._get_auth_headers(),
            verify=False
        )

        return response

    @authenticated_method
    def transactions(self, offset=0, limit=100, sort="desc"):
        # this method doesn't work atm.
        # btcturk responses with "{u'Message': u'An error has occurred.'})"

        response = requests.get(
            self._generate_url("userTransactions", {"offset": offset, "limit": limit, "sort": sort}),
            headers=self._get_auth_headers(),
            verify=False,
        )

        return response

    @authenticated_method
    def open_orders(self):
        response = requests.get(
            self._generate_url("openOrders"),
            headers=self._get_auth_headers(),
            verify=False,
        )

        return response

    @authenticated_method
    def cancel_order(self, order_id):
        response = requests.post(
            self._generate_url("cancelOrder"),
            data={"id": order_id},
            headers=self._get_auth_headers(),
            verify=False,
        )

        return response

    def buy(self, market_order=True, price=None, amount=None, total=None):
        if market_order:
            data = {"IsMarketOrder": 1, "Total": total}
        else:
            data = {"IsMarketOrder": 0, "Price": price, "Amount": amount}

        response = requests.post(
            self._generate_url("buy"),
            data=data,
            headers=self._get_auth_headers(),
            verify=False,
        )

        return response

    def sell(self, market_order=True, price=None, amount=None, total=None):

        if market_order:
            data = {"IsMarketOrder": 1, "Amount": amount}
        else:
            data = {"IsMarketOrder": 0, "Price": price, "Amount": amount}

        response = requests.post(
            self._generate_url("sell"),
            data=data,
            headers=self._get_auth_headers(),
            verify=False,
        )

        return response

    @authenticated_method
    def buy_with_market_order(self, total):
        return self.buy(market_order=True, total=total)

    @authenticated_method
    def buy_with_limit_order(self, price, amount):
        return self.buy(market_order=False, price=price, amount=amount)

    @authenticated_method
    def sell_with_market_order(self, amount):
        return self.sell(market_order=True, amount=amount)

    @authenticated_method
    def sell_with_limit_order(self, price, amount):
        return self.sell(market_order=False, price=price, amount=amount)
