#la on est un peu perdu
import turtle

class TurtleBot:
    
    def __init__(self, n):
        self.name = n
        
    def SetUp(self):
        self.name = tutle.Turtle()
        
    def moveforward(self, distance):
        self.name.forward(distance)
    
    def Turnleft(self):
        self.name.turnleft()
    
    def getangle(self):
        """returns the angle in degrees"""
        return (self.__angle * 180 / math.pi) % 360