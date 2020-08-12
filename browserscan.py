#!/usr/bin/python3
# coding: utf-8
import subprocess

def main(data1):
	target = data1
	cmd = ["./xray.exe","webscan","--browser-crawler",target,"--html-output" ,"report__datetime__.html"]
	rsp=subprocess.Popen(cmd)
	output, error = rsp.communicate()
	print(output)

if __name__=='__main__':
	file = open("url.txt")
	for text in file.readlines():
		data1=text.strip('\n')
		main(data1)