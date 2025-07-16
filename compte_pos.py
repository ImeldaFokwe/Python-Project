def compte_pos(x):
     '''(list)->int
      Retourne le nombre d'elements positifs
      '''
     la=list(eval(x))
     s=0
     for i in range(0,len(la)):
        if la[i]>0:
           s=s+1
     return s

#Programme principale
x=(input('veuillez entrer une liste de valeurs separees par des virgules: '))
print('Le nombre d’éléments positifs est: ',compte_pos(x))