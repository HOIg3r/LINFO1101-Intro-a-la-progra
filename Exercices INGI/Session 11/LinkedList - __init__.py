def __init__(self, lst=[]):
    self.__length = 0
    self.__head = None
    lst_copy = lst.copy()
    lst_copy.reverse()
    for element in lst_copy:
        self.add(element)