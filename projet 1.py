import random

def comparaison(j1,j2):
    joueur1 = sum(j1)
    joueur2 = sum(j2)
    if joueur1 > joueur2:
        #print("Joueur 1 gagne avec un total de" , joueur1)
        return 1
    elif joueur2 > joueur1:
        #print("Joueur 2 gagne avec un total de" , joueur2)
        return 2
    else:
        #print ("Egalité ! les deux jouers ont un total de" , joueur1)
        return 0

def lancer_de():
    return random.randint(1, 6)

def lancer_trois_fois():
    return [lancer_de() for _ in range(3)]

joueur1 = lancer_trois_fois()
joueur2 = lancer_trois_fois()

resultats_joueur = comparaison(joueur1, joueur2)
print(joueur1, joueur2, resultats_joueur)

