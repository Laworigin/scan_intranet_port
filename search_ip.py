# ！/bin/sur/
# coding:utf-8
# author:Wisdom_Tree
# search alive ip address through threading

from threading import Thread,activeCount
import os

def cmd(ip,ip_live):
	cmd=os.popen("ping "+ip+' -n 1 -w 10')
	re=cmd.read()
	re=re.find('TTL')
	if re!=(-1):
		ip_live.append(ip)
		print(ip+"      alive")


def search_all_ip(ip,ip_live):
	if activeCount()<200:
		Thread(target=cmd,args=(ip,ip_live)).start()

