class Ttip31c:

    def __init__(self):
        #BASE DE DONNE
        self.m_vbesat = [1.3, 2.6]
        self.m_vcesat = [0.4, 1.6]

        self.m_v = 30
        self.m_a = 0.8

        self.m_beta_min = [35, 50, 75, 50, 30]

        #AUTRE
        self.m_e = 0
        self.m_rb = 0
        self.m_r = 0
        self.m_beta = 0
        self.m_icsat = 0
        self.m_vbe_reponse = 0
        self.m_vce_reponse = 0
        self.m_beta_reponse = 0
        self.m_vcc = 0
        self.m_vdiode = 0


    def calculResistanceBase(self):
        #DEMANDE DES INFORMATIONS
        print("De quelle valeur de Ic votre montage ce raproche le plus ?")
        print(" 1 - 150 mA")
        print(" 2 - 500 mA\n")
        self.m_vbe_reponse = int(input("Répondez par 1 ou 2: "))
        self.m_icsat = int(input("\nQuelle valeur de Ic est dans votre montage ? "))
        print("\nQuelle valeur de beta correspond à votre montage")
        print(" 1 - IC: 0.1 mA, Vce: 10 V - 35")
        print(" 1 - IC: 1 mA, Vce: 10 V - 50")
        print(" 1 - IC: 10 mA, Vce: 10 V - 75")
        print(" 1 - IC: 150 mA, Vce: 1 V - 50")
        print(" 1 - IC: 500 mA, Vce: 10 V - 30")
        self.m_beta_reponse = int(input("\nRépondez par un chiffre entre 1 et 5: "))
        self.m_e = int(input("\nQuelle est la tension du générateur sur le base? "))

        #CALCUL ET RETOUR
        self.m_rb = (self.m_e - self.m_vbesat[self.m_vbe_reponse-1])/((2*self.m_icsat)/self.m_beta_min[self.m_beta_reponse-1])
        return m_rb

    def calculResistanceCircuit(self):
        #DEMANDE DES INFORMATIONS
        print("De quelle valeur de Ic votre montage ce raproche le plus ?")
        print(" 1 - 150 mA")
        print(" 2 - 500 mA\n")
        self.m_vce_reponse = int(input("Répondez par 1 ou 2: "))
        self.m_icsat = int(input("\nQuelle valeur de Ic est dans votre montage ? "))
        self.m_vcc = int(input("\nQuelle est la tension du générateur sur le montage ? "))
        self.m_vdiode = int(input("\nQuelle est la tension de la diode ? "))

        #CALCUL ET RETOUR
        self.m_r = (self.m_vcc - self.m_vcesat[self.m_vce_reponse] - self.m_vdiode)/(self.m_icsat)
        return m_r

    def afficherCaracteristiques(self):
        print("\nCARACTERISTIQUES DU TRANSISTOR 2N2222")
        print("Sa tension maximal est de  V".format(self.m_v))
        print("Son courant maximal est de  A".format(self.m_a))
        print("Ses tension de saturation entre le collecteur et l'emeteur sont:")
        print("   1 - Ic 150 mA, Ib 15 mA = 0.4 V")
        print("   2 - Ic 500 mA, Ib 50 mA = 1.6 V")
        print("\nSes tension de saturation entre la base et l'emeteur sont:")
        print("   1 - Ic 150 mA, Ib 15mA = 1.3 V")
        print("   2 - Ic 500 mA, Ib 50 mA = 2.6 V")
        print("\nSes coeficient Beta sont:")
        print("   1 - Ic 0.1 mA, Vce 10 V = 35")
        print("   2 - Ic 1 mA, Vce 10 V = 50")
        print("   3 - Ic 10 mA, Vce 10 V = 75")
        print("   4 - Ic 150 mA, Vce 1 V = 50")
        print("   5 - Ic 500 mA, Vce 10 V = 30")


        
