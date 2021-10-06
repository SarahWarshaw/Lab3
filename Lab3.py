from ADC import PCF8591
from joystick import Joystick
from time import sleep

myJoystick = Joystick(0x48)

while True:
  try:
    X = myJoystick.getX()
    Y = myJoystick.getY()
  except KeyboardInterrupt:
    print('Ending')
  print("{:d},{:d}".format(X,Y))
  sleep(0.1)
