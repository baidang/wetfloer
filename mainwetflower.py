#!/usr/bin/python
# -*- coding:utf8 -*-

import datetime
from weibodata import *
from readdata import *

def get_data():
	#get the bluetooth data
	data = read_data()
	if data is not None:
		temp = data.split('/')
		return temp

def send_weibo_text(text):
	client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
	code = get_code()
	r = client.request_access_token(code)
	access_token = r.access_token
	expires_in = r.expires_in
	client.set_access_token(access_token, expires_in)
	r = client.statuses.update.post(status=text)

def send_weibo_text_img(text, img_url):
	client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
	code = get_code()
	r = client.request_access_token(code)
	access_token = r.access_token
	expires_in = r.expires_in
	client.set_access_token(access_token, expires_in)
	#open the img and send as binary data
	img = open('goodnight.jpg','rb')
	r = client.statuses.upload.post(status=text,pic=img)
	img.close()

if __name__ == '__main__':
	datebegin = datetime.datetime(2014,8,12,0,0,0)
	while True:
		# send weibo evryday at 10 o'clock
		dateend = datetime.datetime.now()
		days = (dateend - datebegin).days + 1
		# get the hour now
		strTime = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())
		strHour = strTime.split('-')
		if strHour[3]== '10' :
			text=u'Hi, 小xu测试第%d天，今天在老友科技里, 温度: %s*C, 空气湿度: %s%%, 我的土壤湿度: %s%%, 很舒服! @candys @Rouzai_2010-TB_百当 @靖小仇' % (days, temperature, humidity, moisture)
			send_weibo_text(text)
		
		# get the envirment data from sensors
		tmp_data = get_data()
		temperature = tmp_data[0]
		humidity = tmp_data[1]
		moisture = tmp_data[2]
		
		# adjust if the plant needs water
		if temperature < 50 and moisture <= 5 and humidit < 40:
			text = u'I think I need some water, master! @Rouzai_2010-TB_百当'
			send_weibo_text(text)
		
		#img_url = 'goodnight.jpg'
		#send_weibo_text_img(text, img_url)
