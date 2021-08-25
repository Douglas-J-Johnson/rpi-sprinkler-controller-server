#!/usr/bin/python
# -*- coding:UTF-8 -*-

from bottle import *
import RPi.GPIO as GPIO
import socket

#GPIO Pins (BCM Numbering)
Relay = [5, 6, 13, 16, 19, 20, 21, 26]
GPIO.setmode(GPIO.BCM)

# ------------------------------
# |Channel | RPI pin | BCM     |
# ------------------------------
# |CH1     | 29      | 5       |
# |CH2     | 31      | 6       |
# |CH3     | 33      | 13      |
# |CH4     | 36      | 16      |
# |CH5     | 35      | 19      |
# |CH6     | 38      | 20      |
# |CH7     | 40      | 21      |
# |CH8     | 37      | 26      |
# ------------------------------

#All the relays
Relay1 = 1
Relay2 = 1
Relay3 = 1
Relay4 = 1
Relay5 = 1
Relay6 = 1
Relay7 = 1
Relay8 = 1

for i in range(8):
  GPIO.setup(Relay[i], GPIO.OUT)
  GPIO.output(Relay[i], GPIO.HIGH)

#@get("/")
#def index():
#  global Relay1,Relay2,Relay3,Relay4,Relay5,Relay6,Relay7,Relay8

#  Relay1 = 1
#  Relay2 = 1
#  Relay3 = 1
#  Relay4 = 1
#  Relay5 = 1
#  Relay6 = 1
#  Relay7 = 1
#  Relay8 = 1

#  return static_file('index.html', './')

#@route('/<filename>')
#def server_Static(filename):
#  return static_file(filename, root='./')

@route('/relays/set', method="POST")
def Relay_Control():
  global Relay1,Relay2,Relay3,Relay4,Relay5,Relay6,Relay7,Relay8

  Relay1 = request.POST.get('Relay1')
  Relay2 = request.POST.get('Relay2')
  Relay3 = request.POST.get('Relay3')
  Relay4 = request.POST.get('Relay4')
  Relay5 = request.POST.get('Relay5')
  Relay6 = request.POST.get('Relay6')
  Relay7 = request.POST.get('Relay7')
  Relay8 = request.POST.get('Relay8')
#  print(Relay1)
#  print(Relay2)
#  print(Relay3)
#  print(Relay4)
#  print(Relay5)
#  print(Relay6)
#  print(Relay7)
#  print(Relay8)
  GPIO.output(Relay[0], int(Relay1))
  GPIO.output(Relay[1], int(Relay2))
  GPIO.output(Relay[2], int(Relay3))
  GPIO.output(Relay[3], int(Relay4))
  GPIO.output(Relay[4], int(Relay5))
  GPIO.output(Relay[5], int(Relay6))
  GPIO.output(Relay[6], int(Relay7))
  GPIO.output(Relay[7], int(Relay8))

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('8.8.8.8', 80))
localhost = s.getsockname()[0]

run(host=localhost, port="8000")
