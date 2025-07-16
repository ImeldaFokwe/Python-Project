def sequenceMax(x):
     '''(list)-> int
     cette fonction prend une liste de nombres et retourne
     la longueur de la plus longue séquence d'éléments consécutifs égaux 
      '''
     '''if int(x[i])==int(x[i+1]):
             count=count+1
             if max_compteur<count:
                  max_compteur=count'''
     x=list(eval(x))
     max_compteur=0
     count=1
     for i in range(0,len(x)-1):
        if int(x[i])==int(x[i+1]):
             count=count+1
        else: 
          
             if int(max_compteur)<=int(count):
                  max_compteur=count
             count=1
     if int(max_compteur)<=int(count):
        max_compteur=count
     return max_compteur

x=input('Veuillez entrer une liste de valeurs séparées par des virgules: ')
print(sequenceMax(x))