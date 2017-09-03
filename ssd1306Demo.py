#hardware platform: Brainpad
#Testing the onboard Oled
import pyb
import ssd1306

i2c=pyb.I2C(1,pyb.I2C.MASTER,baudrate=100000)
lcd=ssd1306.SSD1306_I2C(128,64,i2c)
lcd.text("The BrainPad",0,0)
lcd.text("From ",0,16)
lcd.text("GHI Electronics",0,32)
lcd.show()
