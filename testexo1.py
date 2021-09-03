liste = [7,9,14,2,5]

#par element
def recherche2 (liste, valeur):
    """
    La fonction retourne oui si la valeur est bien dans la liste, sinon non.
    liste(list) : Renferme une liste d\'entiers
    valeur(int) : valeur recherché dans la liste
    return(bool) : True si valeur E liste et false si non.
    """
    for val in liste :  # pacours pas elé
        if val == valeur:
            return True
    return False
#print(recherche2(liste, 14))
        
#par indice
def recherche (liste, valeur):
    """
    La fonction retourne oui si la valeur est bien dans la liste, sinon non.
    liste(list) : Renferme une liste d\'entiers
    valeur(int) : valeur recherché dans la liste
    return(bool) : True si valeur E liste et false si non.
    """
    for i in range(len(liste)):
        if valeur == liste[i]:
            return True
    return False

#print(recherche(liste, 14))

#while
def recherche3 (liste, valeur):
    i = 0
    while i <= len(liste) - 1:
        if valeur == liste[i]:
            return True
        i += 1
    return False
        
#print(recherche3(liste, 2))
#--------------------------------------------------
#indice
liste = [7,9,14,2,5]
def moyenneind(liste):
    """
    renvoie les moyenne de elements
    liste(list) : renferme une liste d'entiers
    """
    addmoyenne = 0
    for i in range(len(liste)):
        addmoyenne += liste[i]
    
    addmoyenne /= len(liste)
    return addmoyenne

#print(moyenneind(liste))

#elements
liste = [7,9,14,2,5]
def moyenneelem(liste):
    """
    renvoie les moyenne de elements
    liste(list) : renferme une liste d'entiers
    """
    addmoyenne = 0
    for elem in liste:
        addmoyenne += elem
    
    addmoyenne /= len(liste)
    return addmoyenne

print(moyenneelem(liste))



        