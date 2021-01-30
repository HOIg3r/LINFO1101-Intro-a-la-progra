class Animal:
    
    def __init__(self, name):
        self.name = name
        self.diurnal = None
        self.nb_legs = None
        self.asleep = False
        
    def typ(self):
        return 'Animal'
    
    def sleep(self):
        if self.asleep == False:
            self.asleep = True
        else:
            raise RuntimeError
    def wake_up(self):
        if self.asleep == True:
            self.asleep = False
        else:
            raise RuntimeError
        
        
class Lion(Animal):
    
    def __init__(self,name):
        super().__init__(name)
        self.nb_legs = 4
        self.diurnal = True
    def roar(self):
        print("ROARRR!!!")
        
class Owl(Animal):
    
    def __init__(self,name):
        super().__init__(name)
        self.nb_legs = 2
        self.diurnal = False
        
    def fly(self):
        pass
    
class Giraffe(Animal):
    
    def __init__(self, name, neck_length):
        super().__init__(name)
        self.nb_legs = 4
        self.diurnal = True
        if not isinstance(neck_length, (int, float)) or neck_length < 0:
            raise ValueError
        else:
            self.neck_length = neck_length
class Zoo:
    
    def __init__(self):
        self.animals = []
    
    def add_animal(self, animal):
        if animal.typ() == 'Animal':
            self.animals.append(animal)
        else:
            raise ValueError

def create_my_zoo():
    Prince = Lion('Thomas')
    Tocard = Owl('Romain')
    Ich_ich = Giraffe('Pierre', 42)
    Aristocrate = Giraffe('Dylan', 96)
    
    elite = Zoo()
    elite.add_animal(Prince)
    elite.add_animal(Tocard)
    elite.add_animal(Ich_ich)
    elite.add_animal(Aristocrate)
    
    return elite

create_my_zoo()