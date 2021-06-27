"""Exercice 1.1 : Moyenne de trois nombres

Question 1
Donner une définition de la fonction moyenne_trois_nb qui effectue la moyenne arithmétique
de trois nombres."""

def moyenne_trois_nb(a : float, b : float, c : float) -> float:
    """Retourne la moyenne arithmétique de trois nombres a, b et c.
    """
    return (a + b + c)/3.0 #Division flottante

#Jeu de tests :
assert moyenne_trois_nb(3, 6, -3) == 2.0
assert moyenne_trois_nb(1.5, 2.5, 1.0) == 5.0 / 3.0
assert moyenne_trois_nb(3, 6, 3) == 4.0
assert moyenne_trois_nb(1, 1, 1) == 1.0
