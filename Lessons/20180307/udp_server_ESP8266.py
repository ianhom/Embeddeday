# Coding by Robin Chen(https://github.com/ELE-Clouds)

import socket
from machine import Pin
from time import sleep
import network

port=9000
#Wemos Dpin to GPIO

ledRed = Pin(5, Pin.OUT)  # 红色
ledGreen = Pin(4,Pin.OUT)
ledBlue = Pin(14,Pin.OUT)
# 红色亮
def redToggle():
  if ledRed() == 1:
    ledRed.off()
  elif ledRed() == 0:
    ledRed.on()

# 绿色亮
def greenToggle():
  if ledGreen() == 1:
    ledGreen.off()
  elif ledGreen() == 0:
    ledGreen.on()

# 蓝色亮
def blueToggle():
  if ledBlue() == 1:
    ledBlue.off()
  elif ledBlue() == 0:
    ledBlue.on()    

ip='192.168.4.1'
print(str(ip))
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #建立一个实例
s.bind((ip,port))
print('Waiting.........')
while True:
  print("accepting.....")
  data, addr = s.recvfrom(1024)
  print("recved:",data,'from',addr)
  data=str(data)
  onoffRed = data.find('CMD_Red')
  onoffGreen = data.find('CMD_Green')
  onoffBlue = data.find('CMD_Blue')
  print(str(onoffRed))
  print(str(onoffGreen))
  print(str(onoffBlue))
  if onoffRed >= 0: #如果此命令有效
    print('Toggle Led!!')
    redToggle() #调用点亮红灯函数
  elif onoffGreen >=0:
    print('Toggle Green!!')
    greenToggle() #调用点亮绿灯函数
  elif onoffBlue >=0:
    print('Toggle Blue!!')
    blueToggle() #调用点亮蓝灯函数
