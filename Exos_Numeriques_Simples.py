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
def polynomial_carre(a : float, b : float, c : float, x : float) -> float:
    """Retourne la valeur de ax^4 + bx^2 + c
    """
    return (((a*x*x + b) * x*x) + c)

# Jeu de tests
assert polynomial_carre(1,1,1,2) == 21
assert polynomial_carre(1,1,1,3) == 91
assert polynomial_carre(2,0,0,1) == 2
assert polynomial_carre(0,3,0,1) == 3
assert polynomial_carre(2,3,4,0) == 4
assert polynomial_carre(2,3,4,1) == 9

"""Exercice 1.4 : Aire d’une couronne
Cet exercice a pour but de calculer l’aire d’une couronne (c’est-à-dire l’aire comprise entre 2
disques de même centre mais de rayons différents), et de travailler sur la notion d’hypothèse.

Question 1
Donner une définition ainsi qu’un jeu de tests de la fonction aire_disque qui calcule l’aire πr2
d’un disque de rayon r
Remarque : En python, la constante π est déjà définie dans le module math. Pour l’utiliser, il
faut déclarer l’utilisation de ce module en tête du programme avec l’instruction suivante :
"""
import math

def aire_disque(r : float) -> float:
    """Précondition : r>0
    Retourne l’aire πr2 d’un disque de rayon r
    """
    return math.pi * r*r

# Jeu de tests :
assert 3.14 < aire_disque(1.0) < 3.15
assert 12.4 < aire_disque(2.0) < 12.7
assert 314.15 < aire_disque(10.0) < 314.16

"""Question 2
Donner une définition ainsi qu’un jeu de tests de la fonction aire_couronne qui, étant donné
deux nombres r1 et r2, calcule l’aire de la couronne de rayon intérieur r1 et de rayon extérieur
r2.
Par hypothèse, on considère que le rayon intérieur est inférieur ou égal au rayon extérieur."""

def aire_couronne(r1 : float, r2 : float) -> float:
    """Précondition : 0 < r1 <= r2
    Retourne l’aire de la couronne de rayon intérieur r1 et de rayon extérieur r2.
    """
    return math.pi * (r2*r2 - r1*r1)

# Jeu de tests :
assert 3.14 < aire_couronne(0.0, 1.0) < 3.15
assert 9.42 < aire_couronne(1.0, 2.0) < 9.45
assert 311.00 < aire_couronne(1.0, 10.0) < 311.03

"""Exercice 1.5 : Conversion Degrés Fahrenheit-Celsius
Cet exercice a pour but de définir des fonctions de conversion de températures données en degrés
Celsius en leur équivalent en degrés Fahrenheit et réciproquement.
On rappelle que pour mesurer une température, on utilise en France l’échelle des degrés Celsius
alors que, aux USA par exemple, c’est l’échelle des degrés Fahrenheit qui est utilisée.

Question 1
Écrire une définition de la fonction fahrenheit_vers_celsius qui convertit une température t
exprimée en degrés Fahrenheit en son équivalent en degrés Celsius.
Rappel : la température t en degrés Fahrenheit équivaut à la température (t − 32) ∗ 5/9 en degrés Celsius.
"""

def fahrenheit_vers_celsius(t : float) -> float:
    """convertit une température t exprimée en degrés Fahrenheit en son équivalent en degrés Celsius
    """
    return (t - 32) * 5/9

# Jeu de tests :
assert fahrenheit_vers_celsius(212) == 100.0
assert fahrenheit_vers_celsius(32) == 0.0
assert fahrenheit_vers_celsius(41) == 5.0


