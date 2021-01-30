def fibonacci(n):
    """
    pre : le nième élément de la suite de Fibonacci
    post : retourne le nième élément de la suite de Fibonacci
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)