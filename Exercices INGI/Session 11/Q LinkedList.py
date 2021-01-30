class Node:
    def __init__(self,cargo, next=None):
        self.__cargo = cargo
        self.__next = next
    
    def get_value(self):
        return self.__cargo
    def get_next(self):
        return self.__next
    
class LinkedList:
    
    def __init__(self):
        self.__length = 0
        self.__head = None
        
    def add(self, string):
        node = Node(string, self.__head)
        self.__head = node
        self.__length += 1
        
    def get_reverse(self):
        current = self.__head
        reverse = current.get_value()
        while current.get_next() is not None:
            current = current.get_next()
            reverse += current.get_value()
        return reverse