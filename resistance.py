class Resistance:
	
	def __init__(self):
		#VARIABLES
		self.tension = 0.0
		self.tension_composant = 0.0
		self.courant = 0.0
		self.anneau = 0.0
		self.couleur = ""
		
	def calculResistance(self):
		#DEMANDE D'INFORMATION
		self.tension = float(input("Quelle est la tension dans votre montage ? "))
		self.tension_composant = float(input("\nQuelle est la tension du composant a associer avec la resistance ? "))
		self.courant = float(input("\nQuelle est le courant que doit recevoir votre composant ? "))
		
		#CALCUL ET RETOUR
		self.resultat = (self.tension - self.tension_composant)/self.courant
		return int(self.resultat)