"""
pre : base = le montant sur le compte
      x = le nombre d'année
      y = le taux d'interet
post : retourne le solde du compte a la fin des années
"""
return (base*(1+(y/100))**x)