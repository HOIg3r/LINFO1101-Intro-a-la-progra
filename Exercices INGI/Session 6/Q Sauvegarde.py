def save_data(filename, life, mana, position_x, position_y):
    with open(filename,'w') as file_save:
        for data in life, mana, position_x, position_y:
            file_save.write(str(data)+ "\n")
            
def load_data(filename):
    with open(filename) as file_load:
        data = []
        for line in file_load.readlines():
            data.append(int(line.strip()))
        return tuple(data)