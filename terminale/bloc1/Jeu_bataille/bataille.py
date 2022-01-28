from carte_eleve import * 

def tour(f1,f2) :
    """
    Fonction qui simule un tour de bataille
    param f1: (File) File contenant le jeu n°1
    param f2: (File) File contenant le jeu n°2
    return : Aucun retour, la fonction modifie les files
    """
    # On prend la première carte des joueurs
    c1 = 
    c2 = #Completer
    res = comp(c1,c2)
    if res == -1 :
        #Completer
        #Completer
        print('Joueur 2 a gagné le tour')
    elif res == 1 :
        #Completer
        #Completer
        print('Joueur 1 a gagné le tour')
    else :
        print('Bataille')
        if ... >=3 and  ... >=3 : #A compléter
            bataille(i,j,f1,f2)
        else :
            # Si un des deux paquet ne peut pas faire la bataille 
            # alors on le vide pour faire gagner l'autre joueur
            if ... < 3 : # A compléter
                while not #A completer :
                    #A completer
            else :
                while not #A completer :
                    #A completer

def bataille(c1,c2,f1,f2) :
    """
    Fonction simulant un tour de bataille
    param c1 : (tuple) Carte n°1 égale a c2
    param c2 : (tuple) Carte n°1 égale a c1
    param f1: (File) File contenant le jeu n°1
    param f2: (File) File contenant le jeu n°2
    return : Aucun retour, la fonction modifie les files
    """
    bataille_tab= []
    while comp(c1,c2) == 0:
        bataille_tab.append(c1)
        bataille_tab.append(c2)
        bataille_tab.append(f1)
        bataille_tab.append(f2)
        c1 = 
        c2 = 
    if comp(c1,c2) == 1 :
        for carte in bataille_tab :
            #Completer
        #Completer
        #Completer
        print('Joueur 1 a gagné le tour')
    if comp(c1,c2) == -1 :
        for carte in bataille_tab :
            
        print('Joueur 2 a gagné le tour')     

def est_fini(f1,f2):
    """
    Fonction qui détermine si le jeu est fini
    param f1: (File) File contenant le jeu n°1
    param f2: (File) File contenant le jeu n°2
    return (bool): renvoie True si le jeu est fini, False sinon.
    """
    if  f1 == 0 : #Completer
        print("JOUEUR 2 A GAGNE")
        return f2 #Completer
    elif f2 == 0 : #Completer
        print("JOUEUR 1 A GAGNE")
        return f1 #Completer
    else :
        return None #Completer


def game(f1,f2):
    """
    Fonction simulant le jeu de la bataille
    param f1: (File) File contenant le jeu n°1
    param f2: (File) File contenant le jeu n°2
    """
    while not est_fini(creer_jeu[0],creer_jeu[1]) :
        tour(creer_jeu[0],creer_jeu[1])
