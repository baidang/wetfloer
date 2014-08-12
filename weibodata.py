#!/usr/bin/python
# -*- coding:utf-8 -*-

from weibo import APIClient
import sys
import urllib
import urllib2

APP_KEY = '4028810232'
APP_SECRET = '0881800972bb933cc2a037618081a8d3'
CALLBACK_URL = 'https://api.weibo.com/oauth2/default.html'
USERID = 'yaojun.ch@xuxu.in'
PASSWD = 'cyj0501'

def get_code():
	client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
	url = client.get_authorize_url()
	#print "referer url is : %s" % url

	cookies = urllib2.HTTPCookieProcessor()
	opener = urllib2.build_opener(cookies)
	urllib2.install_opener(opener)
	postdata = {"client_id": APP_KEY,
	            "redirect_uri": CALLBACK_URL,
                    "userId": USERID,
                    "passwd": PASSWD,
                    "isLoginSina": "0",
                    "action": "submit",
                    "response_type": "code"
                   }
	headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:11.0) Gecko/20100101 Firefox/11.0",
        	   "Host": "api.weibo.com",
        	   "Referer": url
        	   }
	req = urllib2.Request( url = url,
           		       data = urllib.urlencode(postdata),
           		       headers = headers
                             )	
	resp = urllib2.urlopen(req)
	#print "callback url is : %s" % resp.geturl()
	#print "code is : %s" % resp.geturl()[-32:]
	code=resp.geturl()[-32:]
	return code	

if __name__ == '__main__':
	client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
	code = get_code()
	r = client.request_access_token(code)
	access_token = r.access_token
	expires_in = r.expires_in
	client.set_access_token(access_token, expires_in)

	r = client.statuses.update.post(status=u'Test weibo, 我是肉肉!')	
#	r = client.statuses.update.post(status=u'test weibo2!')
