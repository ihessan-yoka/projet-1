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

def relancer_de(joueur):
    choix = input("Voulez vous relancez un dé pour augmenter vos points ? (Oui/Non): ").lower()
    if choix == "oui":
        indice_de = int(input("Quel dé voulez vous relancer ? (1,2 ou 3): "))
        nouveau_resultat = lancer_de()
        if nouveau_resultat > joueur[indice_de] :
            joueur[indice_de] = nouveau_resultat
            print("Dé relancer avec succès. Nouveaux dés:", joueur)
        else:
            print("Vous avez obtenu un résultat inférieur ou égal. Vous perdez des points !")
            joueur[indice_de] = nouveau_resultat
            print("Nouveaux dés:", joueur)
        print("Vous avez choisi de ne rien changer.")
            

def annoncer_gagnant(resultat, nom_joueur1, nom_joueur2):
    if resultat == 1:
        print(f"{nom_joueur1} remporte la victoire ! Félicitations !")
    elif resultat ==2:
        print(f"Bravo ! {nom_joueur2} est le grand gagnant !")
    else:
        print("C'est une égalité ! Personne ne gagne cette fois-ci")

# Code principal
nom_joueur1 = input("Joueur 1, Veuillez entrer votre nom: ")
nom_joueur2 = input("Joueur 2, Veuillez entrer votre nom: ")

joueur1 = lancer_trois_fois()
joueur2 = lancer_trois_fois()

print(f"{nom_joueur1}: {joueur1}")
print(f"{nom_joueur2}: {joueur2}")

relancer_de(joueur1)
relancer_de(joueur2)

resultats_joueur = comparaison(joueur1, joueur2)
annoncer_gagnant(resultats_joueur, nom_joueur1, nom_joueur2)
