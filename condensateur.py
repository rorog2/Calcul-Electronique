from math import pi

class Condensateur:

	def __init__(self):
		self.tension = 0.0
		self.capacite = 0.0
		self.frequence = 0
		self.resistance = 0


	def calculCapaciteCondensateur(self):
		self.frequence = int(input("Quelle est votre fréquence de coupure en Hz ? "))
		self.resistance = int(input("\nQuelle est la resistance appliquer pour le filtre en ohm ? "))

		#CALCUL ET RETOUR
		self.capacite = 1/(2*pi*self.resistance*self.frequence)
		return float(self.capacite*(10**6))	#capacite et F


	def calculFrequenceCoupure(self):
		self.capacite = float(input("Quelle est votre capacite de condensateur en F ? "))
		self.resistance = int(input("\nQuelle est la resistance appliquer pour le filtre en ohm ? "))

		#CALCUL ET RETOUR
		self.frequence = 1/(2*pi*self.resistance*self.capacite)
		return int(self.frequence)	#Frequence en Hz






if __name__ == "__main__":
	condo = Condensateur()
	res = condo.calculFrequenceCoupure()
	res2 = condo.calculCapaciteCondensateur()
	print(res, "Hz, ",res2, "F")
	input("Appuyer sur une touche pour continuer...")