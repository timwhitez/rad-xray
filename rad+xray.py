#!/usr/bin/python3
# coding: utf-8
import subprocess

def main(data1):
	target = data1
	cmd = ["./rad.exe","-t",target,"-http-proxy","127.0.0.1:7777"]
	rsp=subprocess.check_output(cmd)
	print(rsp)


if __name__=='__main__':
	file = open("url.txt")
	for text in file.readlines():
		data1=text.strip('\n')
		main(data1)