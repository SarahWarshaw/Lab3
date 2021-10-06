from ADC import PCF8591
from joystick import Joystick
from time import sleep

myJoystick = Joystick(0x48)

while True:
  try:
    X = myJoystick.getX
    Y = myJoystick.getY
  except KeyboardInterrupt:
    print('Ending')
  for X,Y in zip(X,Y):
    print('{:3}, {:3}'.format(X,Y))
  sleep(0.1)
