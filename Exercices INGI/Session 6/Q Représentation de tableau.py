def table(filename_in, filename_out, width):
    with open(filename_in,'r') as file_in:
        file_in_line = []
        for line in file_in:
            file_in_line.append(line.strip())
    with open(filename_out,'w') as file_out:
        file_out.write("+" + "-"*(width+2) + "+\n")
        for line in file_in_line:
            file_out.write("| {:{}} |\n".format(line[:width], width))
        file_out.write("+" + "-"*(width+2) + "+")
        
  