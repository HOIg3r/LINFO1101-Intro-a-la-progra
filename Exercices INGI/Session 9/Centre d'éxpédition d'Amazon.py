class Command:
    
    __tot_price = 0
    __tot_command = 0
    
    @classmethod
    def get_total_price(cls):
        return cls.__tot_price
    
    @classmethod
    def get_number_total_command(cls):
        return cls.__tot_command
    
    @classmethod
    def new_command(cls):
        cls.__tot_command += 1
    
    @classmethod
    def set_new_total_price(cls, price):
        cls.__tot_price += price
    
    
    def __init__(self, id_buyer, id_item, quantity, price):
        self.id_buyer = id_buyer
        self.id_item = id_item
        self.quantity = quantity
        self.price = price
        Command.new_command()
        Command.set_new_total_price(price*quantity)
        
        
    def get_price(self):
        return self.price
        
        
    
        
    def __str__(self):
        return "{}, {} : {} * {} = {}".format(self.id_buyer, self.id_item, self.price, self.quantity, (self.price * self.quantity))