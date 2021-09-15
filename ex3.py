import os
t = os.listdir("/home/nsi/exercice_5")
for i in range(len(t)):
    # t[0..i[ est trié et <= à t[i..[
    # on cherche le minimum de t[i..[
    m = i
    for j in range(i + 1, len(t)):
        if os.path.getsize(t[j]) < os.path.getsize(t[m]):
             m = j
    # On permute l'élément d'indice i avec l'élément d'indice m (qui est le minimum) 
    tmp = t[i]
    t[i] =  t[m]
    t[m] = tmp

