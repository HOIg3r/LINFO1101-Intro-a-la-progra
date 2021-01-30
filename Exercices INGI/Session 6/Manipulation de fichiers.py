def line_count(filename):
    with open(filename) as file:
        count = 0
        for line in file:
            count += 1
        return count
    
def char_count(filename):
    with open(filename) as file:
        count = 0
        for line in file:
            for char in line:
                count += 1
        return count

def space(filename, n):
    file = open(filename, "w")
    file.write(' '*n)
    file.close()
        
def capitalize(filename_in,filename_out):
    file_in = open(filename_in,'r')
    file_out = open(filename_out, 'w')
    for line in file_in:
        line = line.upper()
        file_out.write(line)
    file_in.close()
    file_out.close()