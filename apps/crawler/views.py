# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from bs4 import BeautifulSoup
from urllib2 import urlopen

def index(request):
    url = 'http://www.codingdojo.com'
    # ask beutifuk soup to open the below url and parse all html
    soup = BeautifulSoup(urlopen(url), "html.parser")
    # and print the results!
    print soup
    def makeUrlList():
        urlArr = []
        for i in range(len(soup('a'))):
            urlArr.append(soup('a')[i]['href'])
        return urlArr
    list = makeUrlList()
    print list
    def makeUrlDictionary():
        urlDict = {}
        for i in range(len(soup('a'))):
            if urlDict.has_key(soup('a')[i]['href']):
                urlDict[soup('a')[i]['href']] += 1
            else:
                urlDict[soup('a')[i]['href']] = 1
        return urlDict
    print makeUrlDictionary()
    return render(request, 'crawler/index.html')
# Create your views here.
