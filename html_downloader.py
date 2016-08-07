# _*_ coding:utf-8 _*_
'''
Created on 2016年8月6日

@author: 姜文强
'''
import urllib.request as urllib2

class HtmlDownloader(object):
    
    
    def download(self, url):
        if url is None:
            return None
        
        response = urllib2.urlopen(url)
#         request = urllib2.Request(url)
#         request.add_header('user-agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36')
#         response = urllib2.urlopen(request)
        print(response.getcode())
        
        if response.getcode() != 200:
            return None
        
        return response.read()
    
    



