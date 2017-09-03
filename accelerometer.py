from machine import I2C, Pin
from time import sleep
import struct

i2c = I2C(scl=Pin('B6'), sda=Pin('B7'), freq=400000)


i2c.writeto_mem(28, 0x80|0x2A, b'\01')
#data = i2c.readfrom_mem(28, 0x80 | 0x01, 6)
sleep(1)


while True:
  data = i2c.readfrom_mem(28, 0x80 | 0x02, 8)
  
  value = struct.unpack('<hhh', data)
  
  print('accelerometer value: ', value)
  
  
  sleep(0.05)

