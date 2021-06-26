def prix_ttc(prix : float, taux : float) -> float:
    """Précondition : prix >= 0
    Retourne le prix TTC correspondant au prix HT 'prix'
    avec un taux de TVA 'taux'.
    """
    return prix * (1 + taux / 100.0)

# Jeu de tests
assert prix_ttc(100.0, 20.0) == 120.0
assert prix_ttc(100, 0.0) == 100.0
assert prix_ttc(100, 100.0) == 200.0
assert prix_ttc(0, 20) == 0.0
assert prix_ttc(200, 5.5) == 211.0