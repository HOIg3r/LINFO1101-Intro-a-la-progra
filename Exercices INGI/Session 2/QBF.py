for i in range(1, n+1):
    count=0
    for x in range(1, i):
        if i%x== 0:
            count += 1
    print(i, ":", count)