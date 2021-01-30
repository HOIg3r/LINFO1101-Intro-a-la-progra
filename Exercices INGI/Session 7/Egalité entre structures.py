def equal(l,d):
    lst = True
    dis = True
    
    for x,y in d:
        try:
            if l[x][y] != d[(x,y)]:
                dis = False
        except:
            None
            
    for i in range(len(l)):
        for j in range(len(l[i])):
            try:
                if l[i][j] != d[(i,j)]:
                    lst = False
            except:
                if l[i][j] != 0:
                    lst = False
                    
    return (lst and dis)
                
        