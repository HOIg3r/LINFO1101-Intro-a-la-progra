def remove(self):
    if self.first() is not None:
        self.__length -= 1
        self.__head = self.__head.next()