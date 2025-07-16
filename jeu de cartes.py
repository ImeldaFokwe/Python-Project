# Jeu de cartes.

# L'ordinateur est le donneur des cartes.

# Une carte est une chaine de 2 caractères. 
# Le premier caractère représente une valeur et le deuxième une couleur.
# Les valeurs sont des caractères comme '2','3','4','5','6','7','8','9','10','J','Q','K', et 'A'.
# Les couleurs sont des caractères comme : ♠, ♡, ♣, et ♢.
# j'utilise 4 symboles Unicode pour représenter les 4 couleurs: pique, coeur, trèfle et carreau.
# Pour les cartes de 10 j'utilise 3 caractères, parce que la valeur '10' utilise deux caractères.

import random

def attend_le_joueur():
    '''()->None
    Pause le programme jusqu'a ce que l'usager appuie Enter
    '''
    try:
         input("Appuyez Enter pour continuer. ")
    except SyntaxError:
         pass


def prepare_paquet():
    '''()->list of str
        Retourne une liste des chaines de caractères qui représente toutes les cartes,
        sauf le valet noir.
    '''
    paquet=[]
    couleurs = ['\u2660', '\u2661', '\u2662', '\u2663']
    valeurs = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for val in valeurs:
        for couleur in couleurs:
            paquet.append(val+couleur)
    paquet.remove('J\u2663') # élimine le valet noir (le valet de trèfle)
    return paquet

def melange_paquet(p):
    '''(list of str)->None
       Melange la liste des chaines des caractères qui représente le paquet des cartes    
    '''
    random.shuffle(p)
   
#######################################################################################
    
def donne_cartes(p):
     '''(list of str)-> tuple of (list of str,list of str)

     Retournes deux listes qui représentent les deux mains des cartes.  
     Le donneur donne une carte à l'autre joueur, une à lui-même,
     et ça continue jusqu'à la fin du paquet p.
     '''
     
     donneur=[]
     autre=[]
     for i in range(0,len(p),2):
         donneur.append(p[i])
     for i in range(1,len(p),2):
         autre.append(p[i])
     return (donneur, autre)



def elimine_paires(l):
    l.sort()
    liste=[]
    resultat=[]
    for i in l:
        valeur=i[0]
        liste.append(valeur)
    if len(liste)==0:
        random.shuffle(l)
    elif len(liste)==1:
        random.shuffle(l)
    else:
        i=0
        while i<len(l)-1:
            if len(l[i])!=len(l[i+1]):
                i=i+1
            if len(l[i])==len(l[i+1]):
                a=l[i]
                b=l[i+1]
                x=a[0]
                y=b[0]
                if str(x)==str(y):
                    l.remove(a)
                    l.remove(b)
                else:
                    i=i+1

        random.shuffle(l)
    return l
    
    


    

def affiche_cartes(p):
    '''
    (list)-None
    Affiche les éléments de la liste p séparées par d'espaces
    '''
    s=[]
    for i in range(0,len(p)):
      s.append(p[i])
      print(s[i],end=' ')
    

def entrez_position_valide(n):
    p=prepare_paquet()
    melange_paquet(p)
    tmp=donne_cartes(p)
    donneur=tmp[0]
    humain=tmp[1]
    while n>len(donneur)-1:
        n=int(input("entrer une position valide: "))
    if n<=len(donneur)-1:
        y=str(donneur[n-1])
        donneur.append(y)
    return donneur
    '''
     (int)->int
     Retourne un entier lu au clavier, de 1 à n (1 et n inclus).
     Continue à demander si l'usager entre un entier qui n'est pas entre 1 et n
     
     Précondition: n>=1
     '''


import random
def joue():
    
    p=prepare_paquet()
    melange_paquet(p)
    tmp=donne_cartes(p)
    donneur=tmp[0]
    humain=tmp[1]

    print("Bonjour. Je m'appelle Robot et je distribue les cartes.")
    print("Votre main est:")
    
    print(affiche_cartes(humain))
    
    print("Ne vous inquiétez pas, je ne peux pas voir vos cartes ni leur ordre.")
    print("Maintenant défaussez toutes les paires de votre main. Je vais le faire moi aussi.")
    
    donneur=elimine_paires(donneur)
    humain=elimine_paires(humain)
    print(attend_le_joueur())
    a=1

    if len(donneur)==0:
        print("J'ai terminé toutes les cartes.")
        print("Vous avez perdu! Moi, Robot, j'ai gagné.")
        a=3
                
    elif len(humain)==0:
        print("J'ai terminé toutes les cartes.")
        print("Felicitations! Vous, Humain, vous avez gagné.")
        a=4
    
    
    while a<=1:
        
        if a==1:
            
            print("votre tour")
            print("Votre main est:")
            
            print(humain)
            
            print("j'ai "+ str(len(donneur))+"cartes. Si 1 est la position de ma première carte et" + str(len(donneur)) + " est la position de ma dernière carte, laquelle de mes cartes vous voulez?")
            n=int(input("SVP entrer un entier de 1 à " + str(len(donneur)) + ": "))
            
            b=entrez_position_valide(n)
            
            print("Vous avez demande ma " + str(n) + "ème carte.")
            
            x=donneur[n-1]
            
            print("La voila. C'est un ",x)
            print("Avec "+str(x)+"ajouté, votre main est:")
            
            humain.append(x)
            donneur.remove(x)
            print(humain)
            
            print("Après défaussé toutes les paires et mélanger les cartes, votre main est:")
            
            humain=elimine_paires(humain)
            donneur=elimine_paires(donneur)
            print(humain)
            print(attend_le_joueur())

            if len(donneur)==0:
                print("J'ai terminé toutes les cartes.")
                print("Vous avez perdu! Moi, Robot, j'ai gagné.")
                a=3
                
            elif len(humain)==0:
                print("J'ai terminé toutes les cartes.")
                print("Felicitations! Vous, Humain, vous avez gagné.")
                a=4
                
            else:
                a=a-1
            
        
        if a==0:
            
            print("Mon tour.")
            r=random.randint(0,len(humain)-1)         
            print("J'ai pris votre" + str(r+1)+"ème carte.")
            
            donneur.append(humain[r])
            humain.remove(humain[r])
            print(attend_le_joueur())

            if len(donneur)==0:
                print("J'ai terminé toutes les cartes.")
                print("Felicitations! Vous, Humain, vous avez gagné.")
                a=3
                
            elif len(humain)==0:
                print("J'ai terminé toutes les cartes.")
                print("Felicitations! Vous, Humain, vous avez gagné.")
                a=4
                
            else:
                a=a+1
            

            
    donneur=elimine_paires(donneur)
    humain=elimine_paires(humain)
    
 
	 
# programme principale deja completé
joue()



##################################################################################################################
'''
Un exemple de partie gagnee par Humain:
---------------------------------------

Bonjour. Je m'appelle Robot et je distribue les cartes.
Votre main est:
7♡ 4♠ 9♣ 5♣ 9♠ Q♡ A♠ 10♢ J♠ 5♡ 7♢ 6♢ 10♠ Q♢ 4♡ Q♣ J♡ 7♠ 6♡ 6♠ 3♠ 3♢ 8♠ 10♣ K♢ 6♣ 
Ne vous inquiétez pas, je ne peux pas voir vos cartes ni leur ordre.
Maintenant défaussez toutes les paires de votre main. Je vais le faire moi aussi.
Appuyez Enter pour continuer. 
***********************************************************
Votre tour.
Votre main est:
A♠ 7♢ Q♣ K♢ 10♣ 8♠ 
J'ai 7 cartes. Si 1 est la position de ma première carte et
7 est la position de ma dernière carte, laquelle de mes cartes vous voulez?
SVP entrer un entier de 1 à 7: 6
Vous avez demande ma 6ème carte.
La voila. C'est un A♣
Avec A♣ ajouté, votre main est:
A♠ 7♢ Q♣ K♢ 10♣ 8♠ A♣ 
Après défaussé toutes les paires et mélanger les cartes, votre main est:
8♠ Q♣ 10♣ 7♢ K♢ 
Appuyez Enter pour continuer. 
***********************************************************
Mon tour.
J'ai pris votre 2ème carte.
Appuyez Enter pour continuer. 
***********************************************************
Votre tour.
Votre main est:
8♠ 10♣ 7♢ K♢ 
J'ai 5 cartes. Si 1 est la position de ma première carte et
5 est la position de ma dernière carte, laquelle de mes cartes vous voulez?
SVP entrer un entier de 1 à 5: 3
Vous avez demande ma 3ème carte.
La voila. C'est un 10♡
Avec 10♡ ajouté, votre main est:
8♠ 10♣ 7♢ K♢ 10♡ 
Après défaussé toutes les paires et mélanger les cartes, votre main est:
7♢ 8♠ K♢ 
Appuyez Enter pour continuer. 
***********************************************************
Mon tour.
J'ai pris votre 1ère carte.
Appuyez Enter pour continuer. 
***********************************************************
Votre tour.
Votre main est:
8♠ K♢ 
J'ai 3 cartes. Si 1 est la position de ma première carte et
3 est la position de ma dernière carte, laquelle de mes cartes vous voulez?
SVP entrer un entier de 1 à 3: 1
Vous avez demande ma 1ère carte.
La voila. C'est un K♣
Avec K♣ ajouté, votre main est:
8♠ K♢ K♣ 
Après défaussé toutes les paires et mélanger les cartes, votre main est:
8♠ 
Appuyez Enter pour continuer. 
***********************************************************
Mon tour.
J'ai pris votre 1ère carte.
Appuyez Enter pour continuer. 
***********************************************************
J'ai terminé toutes les cartes.
Felicitations! Vous, Humain, vous avez gagné.
>>> 
'''

##################################################################################################################
'''
Un exemple de partie gagnee par Robot:
---------------------------------------

Bonjour. Je m'appele Robot et je donne les cartes.
Votre main de cartes est:
3♣ 6♣ 2♢ 10♡ 10♠ 8♢ 5♣ Q♣ 4♡ 8♠ 5♠ J♢ 3♢ A♠ 7♡ 3♠ A♣ 9♡ 3♡ 9♣ 8♣ 6♠ 7♣ 6♢ K♠ Q♠ 
Ne vous inquitez pas, je ne peux pas voir votres cartes ou leur ordre.
Maintenant defaussez toutes les paires de votre main. Je vais faire ca aussi.
Appuyez Enter pour continuer. 
***********************************************************
Votre tour.
Votre main est:
4♡ 2♢ J♢ 6♣ 8♣ K♠ 
J'ai 5 cartes. Si 1 est la position de ma premiere carte et
5 est la position de ma derniere carte, laquelle de mes cartes vous voulez?
SVP entrer un entier de 1 a 5: 5
Vous avez demande ma 5-eme carte.
La voila. C'est un K♣
Avec K♣ ajoute, votre main est:
4♡ 2♢ J♢ 6♣ 8♣ K♠ K♣ 
Apres defausser toutes les paires et melanger les cartes, votre main est:
J♢ 6♣ 8♣ 4♡ 2♢ 
Appuyez Enter pour continuer. 
***********************************************************
Mon tour.
J'ai pris votre 2-eme carte.
Appuyez Enter pour continuer. 
***********************************************************
Votre tour.
Votre main est:
J♢ 8♣ 4♡ 2♢ 
J'ai 3 cartes. Si 1 est la position de ma premiere carte et
3 est la position de ma derniere carte, laquelle de mes cartes vous voulez?
SVP entrer un entier de 1 a 3: 3
Vous avez demande ma 3-eme carte.
La voila. C'est un 8♡
Avec 8♡ ajoute, votre main est:
J♢ 8♣ 4♡ 2♢ 8♡ 
Apres defausser toutes les paires et melanger les cartes, votre main est:
4♡ 2♢ J♢ 
Appuyez Enter pour continuer. 
***********************************************************
Mon tour.
J'ai pris votre 2-eme carte.
Appuyez Enter pour continuer. 
***********************************************************
Votre tour.
Votre main est:
4♡ J♢ 
J'ai 1 cartes. Si 1 est la position de ma premiere carte et
1 est la position de ma derniere carte, laquelle de mes cartes vous voulez?
SVP entrer un entier de 1 a 1: 1
Vous avez demande ma 1-ere carte.
La voila. C'est un 4♣
Avec 4♣ ajoute, votre main est:
4♡ J♢ 4♣ 
Apres defausser toutes les paires et melanger les cartes, votre main est:
J♢ 
Appuyez Enter pour continuer. 
J'ai terminé toutes les cartes.
Vous avez perdu! Moi, Robot, j'ai gagné.
>>> 
'''
##################################################################################################################
