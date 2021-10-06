from ADC import PCF8591
class Joystick:
  def __init__(self, address):
    self.myPCF8591 = PCF8591(address)

  def getX(self):
    return self.myPCF8591.read(0)
    
  def getY(self):  
    return self.myPCF8591.read(1)