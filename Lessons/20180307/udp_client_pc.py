from socket import *
import time

r = 'CMD_Red'
g = 'CMD_Green'
b = 'CMD_Blue'

l = [r,g,b]
  
s = socket(AF_INET, SOCK_DGRAM)  
  
while True:  
    for i in l:
        data = i
        s.sendto(data,('192.168.4.1',9000))
        time.sleep(1)

