
class Linkedlist:

    def __init__(self, lst=[]):
        """
        initialisation de la liste chainée
        lst est une liste vide ou remplie de se que on veut
        """
        self.__length = 0
        self.__head = None
        self.__last = None
        lst_bis = lst.copy()
        lst_bis.reverse()
        for e in lst_bis:
            self.add(e)

    def size(self):
        """
        retourne la taille de la liste
        """
        return self.__length

    def moins_size(self):
        """
        diminue la taille de la liste  de 1
        """
        if self.__length >= 1:
            self.__length -= 1
        else:
            self.__length = 0

    def plus_size(self):
        """
        augmente  la taille de la liste de 1
        """
        self.__length += 1

    def first(self):
        """
        retourne la tete de liste
        """
        return self.__head

    def set_first(self, n):
        """
        initialise la tete de liste
        n = Node
        """
        self.__head = n

    def add(self, cargo):
        """
        ajoute un objet dans la liste et le lie avec Node
        """
        node = self.Node(cargo, self.first())
        if self.first() == None:  # when this is the first element being added,
            self.__last = node  # set the last pointer to this new node
        self.set_first(node)
        self.plus_size()

    def print(self):
        """
        print
        """
        self.print_avec_separateur()

    def print_avec_separateur(self, separateur=" "):
        """
        print avec séparateur
        """
        print("[", end=" ")
        if self.first() is not None:
            self.first().print_list_avec_separateur(separateur)
        print("]")

    def print_avec_virgule(self):
        """
        print avec virgule entre
        """
        self.print_avec_separateur(", ")

    def print_backward(self):
        """
        print a l'envers
        """
        print("[", end=" ")
        if self.first() is not None:
            self.first().print_backward()
        print("]")

    def remove(self):
        """
        retire un objet  de la liste
        """
        if self.first() is not None:
            self.moins_size()
            self.set_first(self.first().next())
        if self.size() == 0:  # when there are no more elements in the list,
            self.__last = None  # remove the pointer to the last element

    def add_to_end(self, cargo):
        """
        ajoute un objet a la fin
        """
        if self.size() == 0:  # si la liste est encore vide,
            self.add(cargo)  # ajouter Ã  la fin correspond au ajouter au dÃ©but
        else:  # si la liste contient dÃ©jÃ  au moins un noeud (et donc une dernier noeud)
            node = self.Node(cargo)
            self.__last.set_next(node)  # make the current last node point to this new node
            self.__last = node  # set the last node reference to this new node
            self.plus_size()  # increment list size by one

    class Node:

        def __init__(self, cargo=None, next=None):
            """
            initialise le noeud
            cargo = le contenu
            next = le futur objet
            """
            self.__cargo = cargo
            self.__next = next

        def value(self):
            """
            retourne la valeur du cargo
            """
            return self.__cargo

        def next(self):
            """
            retourne la valeur de next
            """
            return self.__next

        def set_next(self, node):
            """
            initialise le next d'un objet
            """
            self.__next = node

        def __str__(self):
            """
            retourne le print
            """
            return str(self.value())

        def __eq__(self, other):
            """
            verifie si 2 objet sont les memes
            """
            if other is not None:
                return self.value() == other.value()
            else:
                return False

        def print_list(self):
            head = self
            tail = self.__next  # go to my next node
            if tail is not None:  # as long as the end of the list has not been reached
                print(head, end=" ")  # print my head
                tail.print_list()  # recursively print remainder of the list
            else:  # print the last element
                print(head, end=" ")

        def print_backward(self):
            head = self
            tail = self.__next  # go to my next node
            if tail is not None:  # as long as the end of the list has not been reached
                tail.print_backward()  # recursively print remainder of the list backwards
            print(head, end=" ")  # print my head

        def print_avec_separateur(self, separateur):
            print("[", end=" ")
            if self.first() is not None:
                self.head.print_list_avec_separateur(separateur)
            print("]")

        def print_list_avec_separateur(self, separateur):
            head = self
            tail = self.__next  # go to my next node
            if tail is not None:  # as long as the end of the list has not been reached
                print(head, end=separateur)  # print my head, with separateur
                tail.print_list_avec_separateur(separateur)  # recursively print remainder of the list
            else:  # print the last element
                print(head, end=" ")  # print my head, with a space


class Orderedlinkedlist(Linkedlist):

    def __init__(self, lst=[]):
        super().__init__(lst)

    def get_position(self, c):
        posi = 1
        first = self.first()
        if first == None:
            return None
        else:
            ON = True
            while first != None and ON:
                if first.value().coureur() == posi:
                    ON = False
                    return posi
                posi += 1
                first = first.next()
        return None

    def add(self, cargo):
        first = self.first()

        if self.first == None:
            self.__last = self.Node(cargo, self.first())
            self.set_first(self.Node(cargo, self.first()))
        else:
            while first.value() > cargo:
                first = first.next()
            first.set_next(self.Node(cargo, first.next()))

        self.plus_size()

    def get(self, c):
        first = self.first()
        if first == None:
            return None
        else:
            while first.value().coureur() != c and first.next != None:
                first = first.next()
            if first.value().coureur() == c:
                return first.value()
        return None

    def pop(self, c):
        first = self.first()
        if first == None:
            return False
        else:

            # first element is c
            if first.value().coureur() == c:
                if first.next() == None:
                    self.set_first(None)
                else:
                    self.set_first(first.next())
                    return c

            else:
                # c is not in the list or c is further than index 0

                parent = first
                while first.value().coureur() != c and first.next() != None:
                    parent = first
                    elm = first.next()

                if first.value().coureur() == c:
                    parent.set_next(first.next())
                    return c
                else:
                    return False

        return False

    def liste(self):
        lst = []
        first = self.first()
        if first != None:
            while first.next != None:
                lst.append(first.value())
                first = first.next()
        return lst
