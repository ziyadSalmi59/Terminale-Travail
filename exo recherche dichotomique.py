def recherche_dichotomique(liste, valeur):
    gauche = 0
    droite = len(liste) - 1
    pivot = (gauche+droite)//2
    while gauche <= droite:
        if liste[pivot] < valeur:
            gauche = pivot + 1
        if liste[pivot] > valeur:
            droite = pivot - 1
        if liste[pivot] == valeur:
            return True
        pivot = (gauche+droite)//2
    return False

print(recherche_dichotomique([-8, -2, 0, 5, 8, 12,14,15,16,17,18,19,20,21,22], 1))
        
    