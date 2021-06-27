"""Exercice 1.1 : Moyenne de trois nombres

Question 1
Donner une définition de la fonction moyenne_trois_nb qui effectue la moyenne arithmétique
de trois nombres."""

def moyenne_trois_nb(a : float, b : float, c : float) -> float:
    """Retourne la moyenne arithmétique de trois nombres a, b et c.
    """
    return (a + b + c)/3.0 #Division flottante

# Jeu de tests
assert moyenne_trois_nb(3, 6, -3) == 2.0
assert moyenne_trois_nb(1.5, 2.5, 1.0) == 5.0 / 3.0
assert moyenne_trois_nb(3, 6, 3) == 4.0
assert moyenne_trois_nb(1, 1, 1) == 1.0

"""Question 2 : moyenne pondérée
Écrire une définition de la fonction moyenne_ponderee qui effectue la moyenne de trois nombres
a, b, c avec des coefficients de pondération, respectivement pa (pondération en a), pb et pc.
Proposer un jeu de tests comprenant au moins trois tests."""

def moyenne_ponderee(a : float, b : float, c : float, pa : float, pb : float, pc : float) -> float:
    """Précondition : pa + pb + pc != 0
    Retourne la moyenne des trois nombres a, b, c, pondérés respectivement par pa (pondération pour a), pb et pc.
    """
    return ((a * pa) + (b * pb) + (c * pc)) / (pa + pb + pc)

# Jeu de tests
assert moyenne_ponderee(1, 1, 1, 3, 6, -3) == 1.0
assert moyenne_ponderee(2, 3, 4, 1, 1, 1) == 3.0
assert moyenne_ponderee(1, 0, 4, 2, 1, 2) == 2.0


"""Exercice 1.2 : Calcul d’un prix TTC 

Question 1
Ecrire une définition de la fonction prix_ttc qui calcule le prix toutes taxes comprises (TTC)
à partir d’un prix hors taxe (HT) et d’un taux de TVA exprimé en pourcentage, par exemple
20.0 pour une TVA de 20%."""

def prix_ttc(prix : float, taux : float) -> float:
    """Précondition : prix >= 0
    Retourne le prix TTC correspondant au prix HT 'prix'
    avec un taux de TVA 'taux'
    """
    return prix * (1 + taux / 100.0)

# Jeu de tests
assert prix_ttc(100.0, 20.0) == 120.0
assert prix_ttc(100, 0.0) == 100.0
assert prix_ttc(100, 100.0) == 200.0
assert prix_ttc(0, 20) == 0.0
assert prix_ttc(200, 5.5) == 211.0

"""Question 2
Donner une définition de la fonction prix_ht qui calcule le prix hors taxe à partir du prix toutes
taxes comprises et du taux de TVA."""

def prix_ht(prix : float, taux : float) -> float:
    """Précondition : prix >= 0
    Retourne le prix HT correspondant au prix TTC 'prix'
    avec un taux de TVA 'taux'"""
    return prix / (1 + taux / 100.0)

# Jeu de tests
assert prix_ht(120, 20) == 100.0
assert prix_ht(100, 0) == 100.0
assert prix_ht(200, 100) == 100.0
assert prix_ht(0, 20) == 0.0
assert prix_ht(211, 5.5) == 200.0

"""Exercice 1.3 : Calcul de fonctions polynômiales 

Question 1
Après avoir spécifié le problème, écrire un jeu de tests et donner une définition de la fonction
polynomiale telle que polynomiale(a, b, c, d, x) évalue le polynôme ax3 + bx2 + cx + d
(à coefficients flottants)."""

def polynomiale(a : float, b : float, c : float, d : float, x : float) -> float:
    """Retourne la valeur de a*x^3 + b*x^2 + c*x + d
    """
    return (a*x*x*x + b*x*x + c*x + d)
# remarque : on peut aussi utiliser la fonction puissance :
# return (a*x**3 + b*x**2 + c*x + d)
# mais en considèrant que l'opérateur x**3 effectue lui-même x*x*x
# cela revient à faire le même nombre de multiplications.

# Jeu de tests
assert polynomiale(1,1,1,1,2) == 15
assert polynomiale(1,1,1,1,3) == 40
assert polynomiale(2,0,0,0,1) == 2
assert polynomiale(0,3,0,0,1) == 3
assert polynomiale(0,0,4,0,1) == 4
assert polynomiale(1,2,3,4,0) == 4
assert polynomiale(2,3,4,5,1) == 14

# Plus efficace :
def polynomiale_2(a : float, b : float, c : float, d : float, x : float) -> float:
    """Retourne la valeur de a*x^3 + b*x^2 + c*x + d
    """
    return (((((a*x + b) * x) + c) * x) + d)

# Jeu de tests
assert polynomiale_2(1,1,1,1,2) == 15
assert polynomiale_2(1,1,1,1,3) == 40
assert polynomiale_2(2,0,0,0,1) == 2
assert polynomiale_2(0,3,0,0,1) == 3
assert polynomiale_2(0,0,4,0,1) == 4
assert polynomiale_2(1,2,3,4,0) == 4
assert polynomiale_2(2,3,4,5,1) == 14

"""Question 2
Après avoir spécifié le problème, écrire un jeu de tests et donner une définition de la fonction
polynomiale_carre qui rend la valeur de ax^4 + bx^2 + c."""

def polynomiale_carre(a : float, b : float, c : float, x : float) -> float:
    """Retourne la valeur de ax^4 + bx^2 + c
    """
    return (a*x*x*x*x + b*x*x + c)
# ou
# return (a*x**4 + b*x**2 + c)

# Jeu de tests
assert polynomiale_carre(1,1,1,2) == 21
assert polynomiale_carre(1,1,1,3) == 91
assert polynomiale_carre(2,0,0,1) == 2
assert polynomiale_carre(0,3,0,1) == 3
assert polynomiale_carre(2,3,4,0) == 4
assert polynomiale_carre(2,3,4,1) == 9

# Plus efficace (schéma de Hörner) :
def polynomiale_carre(a : float, b : float, c : float, x : float) -> float:
    """Retourne la valeur de ax^4 + bx^2 + c
    """
    return (((a*x*x + b) * x*x) + c)

# Jeu de tests
assert polynomiale_carre(1,1,1,2) == 21
assert polynomiale_carre(1,1,1,3) == 91
assert polynomiale_carre(2,0,0,1) == 2
assert polynomiale_carre(0,3,0,1) == 3
assert polynomiale_carre(2,3,4,0) == 4
assert polynomiale_carre(2,3,4,1) == 9


