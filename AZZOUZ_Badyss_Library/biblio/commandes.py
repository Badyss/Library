#!/usr/bin/env python3

import os
from biblio.livre import Livre
from biblio.bibliotheque import Bibliotheque

'''Affiche le menu pour utiliser le programme'''

def affiche_menu():
		print(" \n\033[36mListe des touches : \033[0m\n")
		print(""" "M"  = Menu principal""")
		print(""" "LG" = Liste des genres""")
		print(""" "LL" = liste des livres""")
		print(""" "NG" = Nouveau genre""")
		print(""" "NL" = Nouveau livre""")
		print(""" "SG" = Supprimer genre""")
		print(""" "SL" = Supprimer livre""")
		print(""" "Q"  = Quitter le programme""")
		print(""" "H"  = Afficher l'historique""")


'''Fonction permettant de créer un genre, si il existe déja, un message d'erreur apparaitra 
    sinon il valide la création du genre'''

def nouveau_genre(bibliotheque): 
    genre = input("Veuillez entrer le nom du nouveau genre : \n")
    if bibliotheque.genre_existe(genre):
        #Ainsi cette commande renvoie à la fonction genre_existe en prennant comme argument le genre saisi par l'utilsateur juste avant.
        print("\033[31m\nCe genre existe déjà dans la bibliothèque.\033[0m")
    else:
        print(f"\033[32\nmLe genre {genre} a été ajouté à la bibliothèque.\033[0m")
        bibliotheque.ajoute_genre(genre)	

'''Fonction permettant de supprimer un genre, si il existe pas, alors un message d'erreur apparaitra,
    sinon il valide la suppresion du genre. Et si un livre appartenait au genre supprimé, alors
    son genre apparaitra comme vide.'''

def supprimer_genre(bibliotheque): 
    print("\033[36mLa liste des genres est :\033[0m \n", bibliotheque.liste_genres)
    genre = input("Veuillez entrer le nom du genre à supprimer : \n")
    if bibliotheque.genre_existe(genre):
        #Cette commande renvoie à la fonction genre_existe en prennant comme argument le genre saisi par l'utilsateur juste avant.
        bibliotheque.liste_genres.remove(genre)
        #Cette fonction va supprimer(remove) le genre saisi dans la liste_genres.
        print(f"\033[32mLe genre {genre} a été supprimé.\033[0m")

        for livre in bibliotheque.liste_livres:
                #Pour tous les livres dans la liste_livres
                if livre.genre == genre:
                    #Si le genre du livre est égal au genre qui a été supprimé
                    livre.genre = ''
					#Alors le genre du livre devient "" (du vide)
    else:
        print(f"\033[31mLe genre {genre} n'existe pas dans la bibliothèque.\033[0m")



    '''Fonction permtettant de créer un livre en demandant un titre, l'année en vérifiant que  celle-ci est correcte.
        Demande le genre, et si celui-ci n'existe pas, la fonction va demander à l'utilsateur de le créer. Si l'utilsateur
        accepte, alors le livre est crée et ajouté à la bibliothèque sinon un message d'erreur apparait'''
		
def nouveau_livre(bibliotheque):
	titre = input("Veuillez entrer le nom du livre : \n")
	annee = input("Veuillez entrer l'année du livre : \n")
	while int(annee) > 2023:
    #Tant que l'année saisie par l'utilisateur est supérieur à 2023 alors :
		print(" année du livre incorrecte.")
		annee = input("Veuillez entrer l'année du livre : \n")
        #Et donc on redemande à l'utilsateur de resaissir une valeur attribuée à annee pour pas que "annee du livre inccorecte" soit spamée.

	genre = input("Veuillez entrer le genre du livre : \n")
	while genre not in bibliotheque.liste_genres:
    #Tant que le genre n'est pas dans la listes des genres, alors :
			rep = input("Genre inexistant, Souhaitez vous le créer ?\n")
			if rep.lower() in ["oui","o", "y"]:
				bibliotheque.ajoute_genre(genre)
                #ON fait donc appel à la fonction ajoute_genre en prenant en compte le genre saisi par l'utilsateur
				print(f"Le genre {genre} a été crée et ajouté au livre")
			else: 
				print("\033[31mImpossible de créer un livre si aucun genre existant n'est saisi.\033[0m")
                #Si l'utilisateur ne veut pas créer le nouveau genre qu'il a attribué au livre, alors le livre ne serra pas crée.
				return
                

	livre = Livre(titre, annee, genre)
    #Toutes les variables qui sont attribuées à titre,annee,genre, vont être attribuées à Livre en tant qu'objet.
	bibliotheque.ajoute_livre(livre)
    #On renvoie donc à la fonction ajoute_livre la variable contenant l'objet du Livre.
	print(f"\033[32mLe livre {titre} a été ajouté à la Bibliothèque\033[0m")
    
'''Renvoie la liste des genres de la bibliothèque'''

def liste_genre(bibliotheque):
	print("\033[36mLa liste des genres est :\033[0m", bibliotheque.liste_genres)
    #Renvoie la listes_genres de la bibliothèque.

''' Fonction permettant d'afficher la liste des livres mais si il n'y en a aucuns, alors
    la fonction affiche un message d'erreur.'''

def liste_livre(bibliotheque):
    if len(bibliotheque.liste_livres) == 0:
    #Si il y'a 0 éléments dans la listes des livres.
        print("\033[31mLa liste des livres est vide\033[0m")
        #La fonction renvoie un message d'erreur.
    else:
        print("\033[36mLa liste des livres est :\033[0m\n")
        for livre in bibliotheque.liste_livres:
        #Pour tous les livres présent dans la liste des livres.
            print(f"{livre.annee} [{livre.genre}] {livre.titre}")
            #L'année serra d'abord collée, puis le genre entre crochets. Puis le titre.

    '''Fonction permettant de supprimer un livre en demandant à l'utilisateur le titre de celui-ci'''

def supprimer_livre(bibliotheque):
    titre = input("Quel livre souhaitez-vous supprimer ?\n")
    if titre not in [livre.titre for livre in bibliotheque.liste_livres]:
    #Si le titre saisi n'est pas présent dans la liste des livres contenant l'objet des livres
        print("\033[31mLivre inexistant, impossible de le supprimer\033[0m")
    else:
        for livre in bibliotheque.liste_livres:
	#Sinon pour tous les livres dans liste_livres donnés par l'utilisateur via la variable livre.
                bibliotheque.liste_livres.remove(livre)
                #La fonction supprimera(remove) l'objet livre de la liste_livres
                print("\033[32mLivre retiré correctement\033[0m") 
                return()

        '''Fonction qui renvoie à la méthode sauvegarer programme si l'utilisateur veut
            sauvegarder la bibliothèque'''

def quitter_prog(bibliotheque):
    rep = input("Souhaitez vous sauvegarder la bibliothèque? \n")
    if rep.lower() in ["non","n", "no"]:
        print("Au revoir et à bientôt")
    else:
        bibliotheque.sauv_biblio()
        print("\033[32mBibliothèque sauvegardée avec succès !\033[0m")
    exit()
    #Quitte entièrement le programme            

'''Fonction vérifiant si un fichier jason existant peut être chargé dans la bibliothèque.'''

def debut_prog(bibliotheque):
    fichier = os.path.expanduser("savebibliodb.json")
    #Cherche le fichier 'savebibliodb.json"
    if os.path.exists(fichier):
        bibliotheque.charger_biblio(fichier)
    else:
        print("\033[31mLe fichier JSON n'existe pas. La bibliothèque sera initialisée avec un contenu vide.\033[0m")