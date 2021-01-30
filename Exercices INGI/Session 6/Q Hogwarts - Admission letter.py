def write(letter_template, name):
   
        with open(letter_template, "r") as from_read:
            lines = from_read.readlines()
            index = 0
            for line in lines:
                index += 1
                if "#" in line:
                    new_line = line.strip().replace("#", str(name))
                    lines[index] = new_line
                    break
        with open(letter_template,"w") as from_write:
            from_write.writelines(lines)
   
        