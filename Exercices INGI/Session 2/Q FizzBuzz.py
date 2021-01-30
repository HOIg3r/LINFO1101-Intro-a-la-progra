if i%3 == 0:
    temp = "fizz"
    if i%5 == 0:
        temp = "fizzbuzz"
elif i%5 == 0 and i%3 != 0:
    temp = "buzz"
else:
    temp = "no"