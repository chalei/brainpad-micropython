
#hardware platform: Brainpad
#read the light value with the onboard light sensor
from pyb import ADC,Pin
import time

adc0 = ADC(Pin('B1'))

while True:
  
  print("light value =", adc0.read()//10)
  time.sleep(0.1)
