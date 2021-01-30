def marks_from_file(filename):
    student_list = []
    try:
        file = open(filename,'r')
        for line in file:
            words = line.split()
            student_list.append(Student(words[0],words[1],int(words[2])))
        return student_list
    except:
        raise OSError