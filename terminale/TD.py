def coupe (liste):
    """
    Description de la fonction : coupe la liste en 2 listes de taille égale (à 1 élément prés)
    liste (list) : liste à couper
    return (tuple(list)) : tuple contenant les 2 sous-listes
    """
    moitie = len(liste)//2
    return (liste[0:moitie], liste[moitie:])

#fusion itérative
def fusion(liste1, liste2):
    i,j = 0, 0 # i est l'indice des éléments de la liste1 et j les indices des éléments de la liste2
    liste = []
    while i < len(liste1) and j < liste2: # Tant qu'on est pas arrivé au bout d'une des listes
        # On ajoute à liste le plus petit élément de liste1 ou de liste2
        if liste1[i] < liste2[j]:
            liste.append(liste1[i])
            i = i + 1
        else :
            liste.append(liste2[j])
            j = j + 1
    # Puis on ajoute les éventuels éléments restant de liste1 et de liste2
    while i< len(liste1):
        liste.append(liste1[i])
        i = i + 1
    while j< len(liste2):
        liste.append(liste2[j])
        j = j + 1
    return liste

#fusion recursive
def fusion(liste1, liste2):
    """
    Description de la fonction : Fusionne 2 listes triées en un e liste triée
    liste1 (list) : liste à fusionner
    liste2 (list) : liste a fusionner
    return (list) : liste fusionnée
    précondition : liste1 et liste2 sont triées
    """
    if liste1 == []:
      return liste2
   elif liste2==[]:
      return liste1
   else:
      if liste1[0]<liste2[0]:
         return [liste1[0]] + fusion(liste1[1:],liste3)
      else:
         return [liste2[0]] + fusion(liste1,liste2[1:])