def rho(a,b,c):
    """
    pre : a, b et c sont des nombre de l'equation ax**2 + bx + c=0
    post : retourne le Rho
    """
    return b**2 - 4*a*c

def n_solutions(a,b,c):
    """
    pre : a, b et c sont des nombre de l'equation ax**2 + bx + c=0
    post : retourne le nombre de solution
    """
    if rho(a,b,c) > 0:
        return 2
    if rho(a,b,c) == 0:
        return 1
    if rho(a,b,c) < 0:
        return 0
    
def solution(a,b,c):
    """
    pre : a, b et c sont des nombre de l'equation ax**2 + bx + c=0
    post : retourne les solution de l'equation
    """
    if n_solutions(a,b,c) == 2:
        x1 = ((-b)+racine_carree(rho(a,b,c)))/(2*a)
        x2 = ((-b)-racine_carree(rho(a,b,c)))/(2*a)
        if x1 < x2:
            return x1
        else:
            return x2
    
    if n_solutions(a,b,c) == 1:
        return -b/(2*a)
        
    if n_solutions(a,b,c) == 0:
        return 0