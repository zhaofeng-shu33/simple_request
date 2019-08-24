# -*- coding: utf-8 -*-
# simple request library which support python2.7 and python3.x
import sys
import urllib
if(sys.version[0] == '3'):
    import urllib.parse
    import urllib.request
    
def request(request_url, method='GET', request_data={}):
    # support post form and get query string
    # return http.client.HTTPResponse
    if(sys.version[0] == '3'):
        request_data = urllib.parse.urlencode(request_data)
        if(method == 'GET'):
            return urllib.request.urlopen(request_url + '?' + request_data)
        else:
            post_data = request_data.encode('utf-8')
            return urllib.request.urlopen(request_url, post_data)        
    else:
        request_data = urllib.urlencode(request_data)
        if(method == 'GET'):
            return urllib.urlopen(request_url + '?' + request_data)
        else:
            return urllib.urlopen(request_url, request_data)        
        
if __name__ == '__main__':
    # get
    r1 = request('https://github.com/search', request_data = {'utf8':'✓','q':'srun'}).read()
    # post
    r2 = request('https://www.mediawiki.org/w/api.php', method='POST', request_data 
    = {'action':'query','titles':'Main page', 'format':'json'}).read()
    print(r1)
    print(r2)