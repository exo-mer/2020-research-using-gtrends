#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pytrends.pyGTrends import pyGTrends
import time
from random import randint

google_username = "yourname@gmail.com"
google_password = "secretpass"
path = ""

# connect to Google
connector = pyGTrends(google_username, google_password)

# Search string
#search_string = "Innovation Entrepreneurship"
search_string = raw_input('Search String: ')

# make request
connector.request_report(search_string, hl='de-DE')

# wait a random amount of time between requests to avoid bot detection
time.sleep(randint(5,10))

filename = "-".join(search_string.split(" "))
print('filename: ', filename)

# download file
connector.save_csv(path, filename)
# get suggestions for keywords
keyword = "Innovation Entrepreneurship"
data = connector.get_suggestions(search_string)
print(data)
