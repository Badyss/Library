class  Livre:
#Une classe representant des livres,
	def  __init__(self , titre, annee, genre): # Donne toute les catégories de la classe Livre 
		self.titre = titre # Catégories de la classe Livre
		self.annee = annee # Catégories de la classe Livre
		self.genre = genre # Catégories de la classe Livre

	def __str__(self):
		return (self.titre) + str(self.annee)  + self.genre
        
	'''Méthode permettant de trier les livres par année, puis genre puis Titre'''

	def __lt__(self, other):
		if self.annee != other.annee:
			#si l'année est différente d'une autre année
			return self.annee < other.annee
		elif self.genre != other.genre:
			#si le genre est différent d'un autre genre
			return self.genre < other.genre
		else:
			return self.titre < other.titre


#Scooby = Livre("scooby-doo",1998,"BD") 
# print(Scooby) # Teste de la classe Livre avec l'exemple suivant
