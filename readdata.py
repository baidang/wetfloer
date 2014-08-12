#! /usr/bin/python
# _*_ coding: utf8 _*_

import serial
import time

port = '/dev/rfcomm0'

def read_data():
	try:
		bluetooth = serial.Serial(port, 9600)
		print("Port Ready!")
		time.sleep(5)
		bluetooth.write('r');
		data = bluetooth.readline();
		if data is not None:
			return data
		else: 
			return ''
	except serial.SerialException, ex:
		print ex

if __name__ == '__main__':
	num = read_data()
	print(num) 	
	temp = num.split('/')
	print len(temp)
	print 'Moisture: %s \nTempereture: %s \nHumidity: %s \n' % (temp[0], temp[1], temp[2])
