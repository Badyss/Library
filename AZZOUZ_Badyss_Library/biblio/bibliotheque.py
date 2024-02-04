#!/usr/bin/python3
import json
from .livre import Livre

class Bibliotheque:
    def __init__(self):
        self.liste_livres = []
        self.liste_genres = []

        '''Méthode permettant d'ajouter un livre dans liste_livres'''

    def ajoute_livre(self, livre):
        self.liste_livres.append(livre)
        self.liste_livres.sort()
        #Fait appel à la méthode __It__ de Livre

        '''Méthode permettant d'ajouter un genre dans listes_genres'''

    def ajoute_genre(self, genre):
        self.liste_genres.append(genre)
        #Colle le genre dans la liste des genres

        '''Méthode permettant de sauvegarder la bibliothèque'''

    def sauv_biblio(self):
        biblio_dict = {"livre": []}
        #permet de créer un dictionnaire
        for livre in self.liste_livres:
            livre_dict = {"titre":livre.titre, "annee": livre.annee, "genre": livre.genre,}
            #On ajoute chaques informations à chaque livre.
            biblio_dict["livre"].append(livre_dict)
        try:
            with open("savebibliodb.json", "w") as f:
                #On ouvre le fichier en mode écriture
                json.dump(biblio_dict, f, indent=4)
        except:
            print("\033[31mImpossible de sauvegarder la bibliothèque.\033[0m")


        '''Méthode permettant de charger la bibliothèque, mais si celle-ci n'est pas compatible avec
            ce programme, alors un message d'erreur serra renvoyé'''

    def charger_biblio(self, fichier):
            try:
                with open(fichier, "r") as f:
                    biblio_dict = json.load(f)
                    #Permet de convertir le fichier jason en python
                    liste_livres_dict = biblio_dict.get("livre")
                    #Permet d'obtenir l'objet "livre" et de lattribuer à la variable liste_livres_dict
                    for livre_dict in liste_livres_dict:
                        self.liste_livres = [Livre(livre_dict.get("titre"), livre_dict.get("annee"), livre_dict.get("genre")) ]
                    #Permet d'ajouter toutes les données sur un livre
                    print("\033[32mBibliothèque chargée avec succès !\033[0m")
            except:
                print("\033[31mLe fichier JSON est mal formé. La bibliothèque sera initialisée avec un contenu vide.\033[0m")

    '''Renvoie tous les genres dans liste_genres'''

    def genre_existe(self, genre):
	    return genre in self.liste_genres
    
