class Ttip120:

    def __init__(self):
        #BASE DE DONNE
        self.m_vbesat = 2.5
        self.m_vcesat = [2, 4]

        self.m_v = 60
        self.m_a = 5

        self.m_beta_min = 1000

        #AUTRE
        self.m_e = 0.0
        self.m_rb = 0.0
        self.m_r = 0.0
        self.m_beta = 0.0
        self.m_icsat = 0.0
        self.m_vbe_reponse = 0.0
        self.m_vce_reponse = 0.0
        self.m_beta_reponse = 0.0
        self.m_vcc = 0.0
        self.m_vdiode = 0.0


    def calculResistanceBase(self):
        #DEMANDE DES INFORMATIONS
        self.m_icsat = float(input("Quelle est la valeur de Ic est dans votre montage ? "))
        self.m_e = float(input("\nQuelle est la tension de votre générateur de courant sur la base ? "))

        #CALCUL ET RETOUR
        self.m_rb = (self.m_e - self.m_vbesat)/((2*self.m_icsat)/self.m_beta_min)
        return int(self.m_rb)

    def calculResistanceCircuit(self):
        #DEMANDE DES INFORMATIONS
        print("De quelle valeur de Ic votre montage ce raproche le plus ?")
        print(" 1 - 3 A")
        print(" 2 - 5 A\n")
        self.m_vce_reponse = float(input("Répondez par 1 ou 2: "))
        self.m_icsat = float(input("\nQuelle valeur de Ic est dans votre montage ? "))
        self.m_vcc = float(input("\nQuelle est la tension du générateur sur le montage ? "))
        self.m_vdiode = float(input("\nQuelle est la tension de la diode ? "))

        #CALCUL ET RETOUR
        self.m_r = (self.m_vcc - self.m_vcesat[self.m_vce_reponse-1] - self.m_vdiode)/(self.m_icsat)
        return int(self.m_r)

    def afficherCaracteristiques(self):
        print("\nCARACTERISTIQUES DU TRANSISTOR 2N2222")
        print("Sa tension maximal est de {} V".format(self.m_v))
        print("Son courant maximal est de {} A".format(self.m_a))
        print("Ses tension de saturation entre le collecteur et l'emeteur sont:")
        print("   1 - Ic 3 A, Ib 12 mA = 2 V")
        print("   2 - Ic 5 A, Ib 20 mA = 4 V")
        print("\nSes tension de saturation entre la base et l'emeteur sont:")
        print("   1 - Vce 3V, Ic 3 A = 1.3 V")
        print("\nSon coeficient Beta est: 1000")


        
