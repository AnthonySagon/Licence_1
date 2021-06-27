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