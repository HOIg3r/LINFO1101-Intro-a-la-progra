class Node:
    
    def __init__(self, cargo, previous=None, next=None):
        self.__cargo = cargo
        self.__previous = previous
        self.__next = next
    
    def get_text(self):
        return self.__cargo
    
    def set_text(self, s):
        self.__cargo = s
        
class Tape:
    
    def __init__(self):
        self.__head = None
        self.__length = 0
        
    def next(self):
        if self.__head is not None: 
            return self.__head.self.next
    
    def add(self, s):
        self.length += 1
        node = Node(s, self.__head)
        self.__head = node
        