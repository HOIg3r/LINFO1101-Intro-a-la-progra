def get_max(filename):
    try:
        count = -1
        with open(filename) as file:
            for line in file.readlines():
                try:
                    line = float(line)
                    if line >= 0 and line > count:
                        count = line
                except:
                    pass
        return count
    except:
        return -1
                    
        