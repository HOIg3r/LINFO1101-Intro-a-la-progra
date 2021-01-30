def read_coordinates(filename):
    file = open(filename, 'r')
    coord = []
    for line in file:
        line = line.strip("\n")
        listed = line.split(",")
        x = float(listed[0])
        y = float(listed[1])
        coord.append((x,y))
    file.close()
    return coord