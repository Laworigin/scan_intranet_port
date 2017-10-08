# !/bin/usr/
#　coding:utf-8
# author:Wisdom_Tree
# using telnetlib to search the port which is open

from telnetlib import Telnet
from threading import Thread,activeCount
import requests

def touch_port(dst,port,url_list):
	try:
		Telnet(dst,port,timeout=1)
		port=str(port)
		print(port+' is open')
		require=requests.get('http://'+dst+':'+port,timeout=1)
		status=require.status_code
		# print(status)
		if status!=404:
			print(require.url+'   Maybe the camera')
			url_list.append(require.url)
	except BaseException:
		port=str(port)



def touch_all(ip,port_max,url_list):
	port=1
	while port<=port_max:
		#if activeCount()<thread:
		test_port=Thread(target=touch_port,args=(ip,port,url_list))  #多线程
		test_port.start()
		port=port+1
	test_port.join()


