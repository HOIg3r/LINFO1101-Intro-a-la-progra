def moveforward(self, distance):
    self.addHistory(("forward", distance))
    self.r1.moveforward(distance)
    self.r2.movebackward(distance)
    
    
def movebackward(self, distance):
    self.addHistory(("backward", distance))
    self.r1.movebackward(distance)
    self.r2.moveforward(distance)
    

def turnleft(self):
    self.addHistory(("left",90))
    self.r1.turnleft()
    self.r2.turnright()

def turnright(self):
    self.addHistory(("right",90))
    self.r1.turnright()
    self.r2.turnleft()
    
def __undoAction(self,action) :
    # le paramètre action est un tuple comme ("right",90), etc.
    operation = action[0]
    parameter = action[1]
    if operation == "forward" :
        self.movebackward(parameter)
    elif operation == "backward" :
        self.moveforward(parameter)
    elif operation == "right" :
        self.turnleft()
    elif operation == "left" :
        self.turnright()
    
def unplay(self) :
    history = self.getHistory()
    for i in range(len(history), 0, -1) : # parcours la liste dans l'ordre inverse
        self.__undoAction(history[i-1])
    self.clearHistory() # vide l'historique après avoir annulé les actions
    self.r1.clearHistory()
    self.r2.clearHistory()