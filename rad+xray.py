#!/usr/bin/python3
# coding: utf-8
import subprocess
import platform
import os
import argparse
import time


def get_args():
    parser = argparse.ArgumentParser(description="for setting targets")
    parser.add_argument("-f", "--file", default="url.txt")
    args = parser.parse_args()
    return args

def main(data1):
	target = data1
	print(target + " Start Crawling")
	cmd = ["./rad_linux_amd64","-t",target,"--auto-index", "--http-proxy", "127.0.0.1:7777", "--no-banner"]
	try:
		output = subprocess.check_output(cmd, timeout=3600)
		print(output.decode("utf-8"))
	except Exception as e:
		#print(e)
		return

if __name__=='__main__':
    sysstr = platform.system()
    args = get_args()
    filename = args.file
    with open(filename, 'r') as f:
        for text in f.readlines():
            data1=text.strip('\n')
            main(data1)
            print(data1 + " Finish")
            time.sleep(10)
		    #清除多余浏览器进程
            try:
                if(sysstr =="Windows"):
                    os.system("taskkill /f /IM chrome*")
                elif(sysstr =="Linux"):
                    os.system("ps aux | awk '/chrome/ { print $2 } ' | xargs kill -9")
            except:
                pass
