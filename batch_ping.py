# coding:utf-8
# ! /bin/usr/
# author:feiyanhahaha
# batch_ping  range:192.168.X.X


import os
import threading
from search_port import touch_all
from search_ip import cmd
import time


def ip_list():   #生成ip列表
	start_list=str(input("Please enter the start of ip:")).split(".")   #将ip地址分隔为列表
	end_list=str(input("Please enter the end of ip:")).split(".")
	# for i in end_list:
	# 	print(i)
	ip=''
	first=''
	second=''
	third=[]
	all_ips=[]
	for i,j,flag in zip(start_list,end_list,range(1,5)):  #对ip列表的每一位进行操作
		if flag==1:
			first+=i
		elif flag==2:
			second+=i
		elif flag==3:  #遍历第三位
			for ip_three in range(int(i),int(j)+1):
				#print(ip_three)
				third.append(ip_three)
		elif flag==4:  
			third_len=len(third)
			third_last=third[-1]
			if third_len>1:
				for pre_third in third:   #遍历第三位
					if pre_third==third_last:  #判断是否为最后一个ip段
						for ip_last in range(1,int(j)+1):   #遍历第四位
							ip_1=first+'.'+second+'.'+str(pre_third)+'.'+str(ip_last)
							all_ips.append(ip_1)
					else:
						for ip_last_domain in range(1,256):
							ip_2=first+'.'+second+'.'+str(pre_third)+'.'+str(ip_last_domain)
							all_ips.append(ip_2)
	return all_ips



if __name__ == '__main__':
	ip_live=[]
	url_list=[]
	ip_list=ip_list()
	# for i in ip_list:
	# 	print(i)
	all_url=open('url_list.txt','w')
	for ip in ip_list:
		#print(ip)
		ping=threading.Thread(target=cmd,args=(ip,ip_live))
		ping.start()
		ping.join()
	#time.sleep(5)
	port_max=int(input("Please enter range of port(enter the max):"))
	for ip in ip_live:
		print("\n"+ip+' port info:')
		touch_all(ip,port_max,url_list)
	for url in url_list:
		all_url.write(url+'\n')
	print("\nPort scan end")
