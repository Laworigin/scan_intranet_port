# !/bin/usr/
#　coding:utf-8
# author:Wisdom_Tree
# using telnetlib to search the port which is open

from telnetlib import Telnet
from threading import Thread,activeCount
import requests

def touch_port(dst,port):
	try:
		Telnet(dst,port,timeout=1)
		port=str(port)
		print(port+' is open')
		require=requests.get('http://'+dst+':'+port,timeout=0.5)
		status=require.status_code
		print(status)
		if status!=404:
			print(require.url+'   Maybe the camera')
	except BaseException:
		port=str(port)



def touch_all(ip,thread,port_max):
	port=0
	while port<=port_max:
		if activeCount()<thread:
			Thread(target=touch_port,args=(ip,port)).start()  #多线程
			port=port+1


