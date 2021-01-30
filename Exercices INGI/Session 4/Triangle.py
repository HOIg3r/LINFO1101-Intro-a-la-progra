def triangle(n): 
    triangle = []
    for i in range(1,n+2):
        l = []
        for x in range(i):
            l.append(x)
        triangle.append(l)
    return triangle