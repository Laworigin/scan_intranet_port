# coding:utf-8
# ! /bin/usr/
# author:feiyanhahaha
# batch_ping  range:192.168.X.X


import os
import threading
from search_port import touch_all
from search_ip import search_all_ip
import time


def ip_list():   #生成ip列表
	start_list=str(input("Please enter the start of ip:")).split(".")
	end_list=str(input("Please enter the end of ip:")).split(".")
	ip_add=''
	start_ip=''
	ip_list=[]
	fourth=''
	for i,j,flag in zip(start_list,end_list,range(1,5)):
		i=int(i)
		j=int(j)
		if flag==4:
			if i<j:
				for tmp in range(i,(j+1)):
					tmp=str(tmp)
					tmp_ip=ip_add
					fourth=str(fourth)
					ip_add=ip_add+fourth+tmp
					ip_list.append(ip_add)
					ip_add=tmp_ip    #重置ip初始地址
			else:
				i=str(i)
				ip_add=ip_add+i+'.'
		else:
			if i<j:
				i=int(i)
				fourth=j=int(j)
				for thrid in range(i,j):
					thrid=str(thrid)
					for last in range(1,255):
						last=str(last)
						tmp=ip_add
						ip_add=ip_add+thrid+'.'+last
						ip_list.append(ip_add)
						ip_add=tmp
			else:
				i=str(i)
				ip_add=ip_add+i+'.'
	return ip_list



if __name__ == '__main__':
	ip_live=[]
	ip_list=ip_list()
	for ip in ip_list:
		search_all_ip(ip,ip_live)
	time.sleep(1)
	thread=int(input("Please enter the number of thread:"))
	port_max=int(input("Please enter range of port(enter the max):"))
	for ip in ip_live:
		print("\n"+ip+' port info:')
		touch_all(ip,thread,port_max)
	print("\nPort scan end")
