import requests
import threading
import time
import os

def start():
    print ("[+] Subdomain Finder v1.0.0")
    print ("[-] Coded By RealSalehn ")
    print ("[-] https://github.com/Realsaleh/ ")

def Desc():
	time.sleep(0.4)
	global url
	url = str(input("Website Address:"))

def find():
	payload = 'https://api.hackertarget.com/hostsearch/?q=%s' % (url,)
	print (" [*] Please Wait...\n")
	result = requests.get(payload)
	print (" --------------------------------")
	print (result.text)
	print (" --------------------------------")

if __name__ == '__main__':
	start()
	Desc()
	print ("\n*************** [ Subdomains ] ***************\n")
	find()