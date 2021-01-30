while s0 != 1:
    print(int(s0))
    if s0 %2 == 0:
        s0 =s0/2
    else:
        s0 = 3*s0+1
print(int(s0))