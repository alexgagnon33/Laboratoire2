import os

absolute_path = ("C:\Users\e2296648\Desktop\labo2\data1")
relative_path = "src/lib"
full_path = os.path.join(absolute_path, relative_path)

absolute_path = ("C:\Users\e2296648\Desktop\labo2\data2")
relative_path = "src/lib"
full_path = os.path.join(absolute_path, relative_path)

absolute_path = ("C:\Users\e2296648\Desktop\labo2\data3")
relative_path = "src/lib"
full_path = os.path.join(absolute_path, relative_path)

def etape_1():

    with open('data1.txt') as A:
        data_A = A.read
    print(data_A)

    with open('data2.txt') as B:
        data_B = B.read
    print(data_B)

    with open('data3.txt') as C:
        data_C = C.read
    print(data_C)

    return data_A, data_B, data_C

def etape_2():

    print('Voici les choix disponible: ')
    print("[1] Afficher les statistiques")
    print("[2] Afficher l'équipe la plus homogène")
    print("[3] Ajouter une faute à une équipe")
    print("[4] Sauvegarder les statistiques")
    print("[5] Sortir")

    choix_utilisateur = int(input('Ecriver votre option: '))

    if choix_utilisateur ==1:
        print

    elif choix_utilisateur ==2:
        print()

    elif choix_utilisateur ==3:
        pass

    elif choix_utilisateur ==4:
        pass
    else:
        choix_utilisateur ==5
        print("Vous quitter le menu: ")
    
def etape_3():
    #doit apprendre comment utiliser des infosd'une autre def
    Meilleur_coureur_A = min(data_A)
    Meilleur_coureur_B = min(data_B)
    Meilleur_coureur_C = min(data_C)
    
    if Meilleur_coureur_A < Meilleur_coureur_B and Meilleur_coureur_A < Meilleur_coureur_C:
        print('Coureur le plus rapide: Equipe A', Meilleur_coureur_A)
    elif Meilleur_coureur_B < Meilleur_coureur_A and Meilleur_coureur_B < Meilleur_coureur_C:
        print('Coureur le plus rapide: Equipe B', Meilleur_coureur_B)
    else:
        Meilleur_coureur_C < Meilleur_coureur_A and Meilleur_coureur_A < Meilleur_coureur_B
        print('Coureur le plus rapide: Equipe C', Meilleur_coureur_C)

moyenne_A = sum(data_A) / len(data_A)
print("La moyenne de cette equipe est: ", round(moyenne_A, 2))


moyenne_B = sum(data_B) / len(data_B)
print("La moyenne de cette equipe est: ", round(moyenne_B, 2))

moyenne_C = sum(data_C) / len(data_C)
print("La moyenne de cette equipe est: ", round(moyenne_C, 2))

if moyenne_A < moyenne_B and moyenne_A < moyenne_C:
    print("L'equipe A est la plus rapide avec un temps moyen de ", moyenne_A)
elif moyenne_B < moyenne_A and moyenne_B < moyenne_C:
    print("L'equipe B est la plus rapide avec un temps moyen de ", moyenne_B)
else:
    moyenne_C < moyenne_A and moyenne_C < moyenne_B
    print("L'equipe C est la plus rapide avec un temps moyen de ", moyenne_C)

import math

def trier(donnees: list[int]):

    donnees_triees = []

    while len(donnees) > 0:

        min = math.inf
        donnees_temp = []

        for donnee in donnees:
            if donnee < min:
                min = donnee

        for donnee in donnees:
            if donnee != min:
                donnees_temp.append(donnee)

        donnees = donnees_temp
        donnees_temp = []

        donnees_triees.append(min)
    return donnees_triees

données = [moyenne_A, moyenne_B, moyenne_C]
print(trier(données))

def etape_4():
   #doit apprendre comment utiliser des infosd'une autre def
   #doit voir la vrai règle pour écart type
    Equipea = sqrt(Sum((data - moyenne)**2)/nombre de données - 1)
    Equipeb = sqrt(Sum((data - moyenne)**2)/nombre de données - 1)
    Equipec = sqrt(Sum((data - moyenne)**2)/nombre de données - 1)

    if Equipea < Equipeb and Equipea < Equipec:
        print("Equipe A est l'equipe avec le plus petit écart-type: ", Equipea)
    elif Equipeb < Equipea and Equipeb < Equipec:
        print("Equipe B est l'equipe avec le plus petit écart-type: ", Equipeb)
    else:
        Equipec < Equipea and Equipec < Equipeb:
        print("Equipe C est l'equipe avec le plus petit écart-type: ", Equipec)

def etape_5():
    #doit apprendre comment ouvrir un fichier comment le prof veut
f = open('Desktop', 'w')
with open('Montréal.txt', 'w') as f:
    f.write(1)
f = open("Montréal.txt")

print('Voici les choix disponible: ')
print("[1] Afficher les statistiques")
print("[2] Afficher l'équipe la plus homogène")
print("[3] Ajouter une faute à une équipe")
print("[4] Sauvegarder les statistiques")
print("[5] Sortir")

choix_user = int(input('Choisir un phrase a recevoir (ex: 1 , 2  ou 3 ): '))
   #doit apprendre comment utiliser des infosd'une autre def
if choix_user ==1:
        input("Quel joeur a la faute en question: ")
        print(joeur, faute) #fichier text
if choix_user ==2:
        input("Quel joeur a la faute en question: ")
        print(joeur, faute) #fichier text
if choix_user ==3:
        input("Quel joeur a la faute en question: ")
        print(joeur, faute) #fichier text
if choix_user ==4:
        input("Quel joeur a la faute en question: ")
        print(joeur, faute) #fichier text

#Étape 6:
#lire info étape 3
#créer nouveau doc os
#mettre info étape 3

