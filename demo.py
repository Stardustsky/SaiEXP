#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-25 11:50
# @Author  : Stardustsky
# @File    : demo.py
# @Software: PyCharm

import optparse


def center(opt):
    pass


if __name__ == '__main__':
    print '''
    =============================================
                      XXXXX漏洞
                Author：Stardustsky
    =============================================
        EG:该exp为反弹shell的EXP，请修改payload中地址
    Python CNVD-C-2019-48814.py -u 10.10.10.10:7001 
    '''
    parser = optparse.OptionParser()
    parser.add_option("-u", "--url", dest="url", help="Target URL (e.g. -u 10.10.10.1:7001)")
    parser.add_option("-e", dest="command", help="Execute command (e.g -e whoami)")
    options, _ = parser.parse_args()
    center(options)


