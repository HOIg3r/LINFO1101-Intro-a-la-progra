def fact(n):
    """
    pre : n > 0
    post: retourne le factoriel de n
    """
    count = 1
    for i in range(1, n+1):
        count *= i
    return count