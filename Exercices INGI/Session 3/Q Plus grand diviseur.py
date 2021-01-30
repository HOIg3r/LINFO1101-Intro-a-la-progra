if a == 0 or a == 1:
    return None
PGD = 0
for i in range(1, a):
    if a%i == 0:
        PGD = i
return PGD

    