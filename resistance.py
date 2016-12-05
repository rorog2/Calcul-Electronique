class Resistance:

    def __init__(self):
        #VARIABLES
        self.tension = 0.0
        self.tension_composant = 0.0
        self.courant = 0.0
        self.anneau = 0.0
        self.couleur = "."
        self.resultat = 0.0
        self.ve = 0.0
        self.vs = 0.0
        self.r1 = 0
        self.r2 = 0

    def calculResistance(self):
        #DEMANDE D'INFORMATION
        self.tension = float(input("Quelle est la tension dans votre montage ? "))
        self.tension_composant = float(input("\nQuelle est la tension du composant a associer avec la resistance ? "))
        self.courant = float(input("\nQuelle est le courant que doit recevoir votre composant ? "))

		#CALCUL ET RETOUR
        self.resultat = (self.tension - self.tension_composant)/self.courant
        return int(self.resultat)

    def calculPontDiviseurVs(self):
        #DEMANDE D'INFORMATION
        self.ve = float(input("Quelle est la tension d'entrÃ©e ? "))
        self.r1 = int(input("Quelle est la valeur de R1 ? "))
        self.r2 = int(input("Quelle est la valeur de R2 ? "))

        #CALCUL ET RETOUR
        self.resultat = (self.r1/(self.r1 + self.r2))*self.ve
        return self.resultat

    def calculPontDiviseurR2(self):
        #DEMANDE D'INFORMATION
        self.ve = float(input("Quelle est la tension d'entrée ? "))
        self.vs = float(input("Quelle est la tension de sortie ? "))
        self.r1 = int(input("Quelle est la valeur de R1 ? "))

        #CALCUL ET RETOUR
        self.resultat = self.r1 * (self.ve / self.vs) - R1
        return self.resultat

#Test du module seul
if __name__ == "__main__":
    #Menu
    print("Que voulez-vous faire ?")
    print("     1 - Calculer une résistance")
    print("     2 - Calculer Vs dans un pont diviseur")
    print("     3 - Calculer R2 dans un pont diviseur")
    choix = int(input("\nQuelle est votre choix: "))
    #Action suivant choix
    if choix == 1:
        res = Resistance().calculResistance()
    elif choix == 2:
        res = Resistance().calculPontDiviseurVs()
    elif choix == 3:
        res = Resistance().calculPontDiviseurR2()

    #Affichage du résultat
    print("Le résultat est: ", res)
    input("Appuyer sur une touche pour continuer...")