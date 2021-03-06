#hardware platform: pyboard V1.1

from pyb import Pin
import time

down = Pin('B10', Pin.IN, Pin.PULL_UP)
up = Pin('A5', Pin.IN, Pin.PULL_UP)
left = Pin('A15', Pin.IN, Pin.PULL_UP)
right = Pin('C13', Pin.IN, Pin.PULL_UP)

red = Pin('C9',Pin.OUT)
green = Pin('C8',Pin.OUT)
blue = Pin('C6',Pin.OUT)
red.on()

while True:
  
  print(down.value())
  if(down.value()==0):
    red.on()
  elif(up.value()==0):
    green.on()
  elif(left.value()==0):
    blue.on()
  elif(right.value()==0):
    red.on()
  else:
    red.off()
    green.off()
    blue.off()
  time.sleep(0.05)


