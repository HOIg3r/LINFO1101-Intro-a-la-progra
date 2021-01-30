def chiffres_pairs(n):
    """
    pre: n = un nombre
    post: retourne si le nombre de caractère du nombre est pair ou impaire
    """
    if len(str(n))%2 == 0:
        return True
    else:
        return False