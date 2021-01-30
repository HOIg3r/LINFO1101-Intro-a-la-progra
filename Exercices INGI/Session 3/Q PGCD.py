def gcd(a,b):
    """
    pre : a et b = 2 nombre naturel
    post : retourne le plus grand diviseur commun des 2 nombre
    """
    if b == 0:
        return a
    else:
        return gcd(b,a%b)