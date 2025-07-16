def sequenceDesDeux(x):
     '''(list)-> bool
      Retourne true s’il y a au moins une séquence de deux
      éléments consécutifs égaux, et False sinon
      '''
     y=x.split(",")
     s=0
     for i in range(0,len(y)-1):
          if str(y[i])==str(y[i+1]):
              s=s+1
          else:
               s=s
     return s>=1
    #Debut du programme
x=str(input("Veuiller entrer une liste de valeurs séparées par des virgules: "))
resultat=sequenceDesDeux(x)
print(resultat)