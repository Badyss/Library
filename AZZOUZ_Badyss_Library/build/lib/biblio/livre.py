class  Livre:
#Une classe representant des livres,
	def  __init__(self , titre , année , genre): # Donne toute les catégories de la classe Livre 
		self.titre = titre # Catégories de la classe Livre
		self.année = année # Catégories de la classe Livre
		self.genre = genre # Catégories de la classe Livre
	def __str__(self):
		return self.titre +  str(self.année) + self.genre

# Scooby = Livre("scooby-doo",1998,"BD") 
# print(Scooby) # Teste de la classe Livre avec l'exemple suivant
