class  Bibliotheque:
#Une classe representant des bibliotheques,
	def  __init__(self , livre, genre): # Donne toute les catégories de la classe Bibliotheque 
		self.livre = [] # Liste vide de la classe Bibliotheque 
		self.genre = [] # Liste vide de la classe Bibliotheque 
	def __str__(self):
		return str(self.livre) + self.genre

