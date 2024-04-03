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


def relancer_de(nom_joueur, joueur):
    indice_de = int(input(nom_joueur+" quel dé voulez vous relancer ? (1,2 ou 3): "))
    nouveau_resultat = lancer_de()
    if nouveau_resultat > joueur[indice_de-1] :
        joueur[indice_de-1] = nouveau_resultat
        print("Dé relancer avec succès. Nouveaux dés:", joueur)
    else:
        print("Vous avez obtenu un résultat inférieur ou égal. Vous perdez des points !")
        joueur[indice_de-1] = nouveau_resultat
        print("Nouveaux dés:", joueur)
    
            
def annoncer_gagnant_manche(resultat, nom_joueur1, nom_joueur2):
    if resultat == 1:
        print(f"{nom_joueur1} remporte la manche !")
    elif resultat == 2:
        print(f"Bravo ! {nom_joueur2} remporte la manche !")
    else:
        print("C'est une égalité ! Personne ne remporte cette manche.")
        
def annoncer_gagnant_partie(points_joueur1, points_joueur2, nom_joueur1, nom_joueur2):
    if points_joueur1 > points_joueur2:
        print(f"{nom_joueur1} remporte la partie avec{points_joueur1} manches gagnées !")
    elif points_joueur2 > points_joueur1:
        print("f{nom_joueur2} remporte la partie avec manches {points_joueur2} gagnées !")
        
def jouer_manche(nom_joueur1, nom_joueur2):
    joueur1 = lancer_trois_fois()
    joueur2 = lancer_trois_fois()
    
    print(f"{nom_joueur1}: {joueur1}")
    print(f"{nom_joueur2}: {joueur2}")
    
    relancer_de(nom_joueur1, joueur1)
    relancer_de(nom_joueur2, joueur2)
    
    resultats_manche = comparaison(joueur1, joueur2)
    annoncer_gagnant_manche(resultats_manche, nom_joueur1, nom_joueur2)
    
    return resultats_manche
       
# Code principal

nom_joueur1 = input("Joueur 1, Veuillez entrer votre nom: ")
nom_joueur2 = input("Joueur 2, Veuillez entrer votre nom: ")

points_joueur1 = 0
points_joueur2 = 0


for manche in range(3):
  print(f"\nDébut de la manche {manche + 1}:")
  resultats_manche = jouer_manche(nom_joueur1, nom_joueur2)

if resultats_manche == 1:
    points_joueur1 += 1
elif resultats_manche == 2:
    points_joueur2 += 1
    
print("\n----- Résultats Partiels -----")
print(f"{nom_joueur1}: {points_joueur1} manches gagnées")
print(f"{nom_joueur2}: {points_joueur2} manches gagnées")
print("----------------------")

abandon = input("Voulez-vous abandonner la partie ? (Oui/Non): ")
if abandon.lower() == "oui":
    print("Partie abandonnée.")
    

annoncer_gagnant_partie(points_joueur1, points_joueur2, nom_joueur1, nom_joueur2)


