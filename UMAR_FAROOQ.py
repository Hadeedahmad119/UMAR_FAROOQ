#!/usr/bin/python2

# -*- coding: utf-8

#CODING BY : UMAR FAROOQ HERE )

#DON'T FORGET TO GIVE CREDIT TO AFRIDI

P = "\033[97;1m" 

M = "\033[91;1m" 

H = "\033[92;1m" 

K = "\033[93;1m" 

B = "\033[94;1m" 

U = "\033[95;1m" 

O = "\033[93;1m" 

N = "\033[0m"

try:

	import os,sys,time,platform,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib,requests,uuid,string,subprocess	from multiprocessing.pool import ThreadPool

	from requests.exceptions import ConnectionError

except ImportError:

	os.system("pip2 install requests")

	os.system("python2 UMAR.py")

from os import system

from time import sleep

def xox(z):

    for e in z + "\n":

        sys.stdout.write(e)

        sys.stdout.flush()

        time.sleep(0.04)

      

agents = [

					"Mozilla/5.0 (Linux; Android 10; Redmi Note 8 Pro Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/275.0.0.49.127;]",

					"[FBAN/FB4A;FBAV/246.0.0.49.121;FBBV/181448449;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBRV/183119516;FBCR/TM;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1606;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",

					"Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J320F Build/LMY47V) [FBAN/FB4A;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/14274161;FBCR/Tele2 LT;FBMF/samsung;FBBD/samsung;FBDV/SM-J320F;FBSV/5.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]",

					"Mozilla/5.0 
