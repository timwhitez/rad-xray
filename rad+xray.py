#!/usr/bin/python3
# coding: utf-8
import subprocess
import platform
import os

def main(data1):
	target = data1
	print(target + "crawling")
	cmd = ["./rad","-t",target,"-http-proxy","127.0.0.1:7777"]
	try:
		output = subprocess.check_output(cmd, timeout=3600)
		#print(output)
	except:
		return


if __name__=='__main__':
	file = open("url.txt")
	for text in file.readlines():
		data1=text.strip('\n')
		main(data1)
		print(data1 + "finish")
		time.sleep(30)
		sysstr = platform.system()
		if(sysstr =="Windows"):
			os.system("taskkill /f /IM chrome.exe")
		elif(sysstr =="Linux"):
			os.system("ps aux | awk '/chrome/ { print $2 } ' | xargs kill -9")
