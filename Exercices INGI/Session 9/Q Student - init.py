class Student:
    __next_number = 0
    def __init__(self, firstname, surname, birthday, email):
        self.__number = Student.__next_number
        Student.__next_number += 1
        self.firstname = firstname
        self.surname = surname
        self.birthday = birthday
        self.email = email
    def __str__(self):
        return "L'étudiant numéro {0} : {1} {2} né le {3}, peut être contacté par {4}".format(
            self.__number, self.firstname, self.surname, self.birthday, self.email
        )