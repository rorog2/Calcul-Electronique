class Ttip31c:

    def __init__(self):
        #BASE DE DONNE
        self.m_vbesat = 1.8
        self.m_vcesat = 1.2

        self.m_v = 100
        self.m_a = 3

        self.m_beta_min = [25, 10]

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
        self.m_icsat = float(input("Quelle valeur de Ic est dans votre montage ? "))
        print("\nQuelle valeur de beta correspond à votre montage")
        print(" 1 - IC: 1 A, Vce: 4 V - 25")
        print(" 1 - IC: 1 A, Vce: 4 V - 10")
        self.m_beta_reponse = int(input("\nRépondez par un chiffre entre 1 et 2: "))
        self.m_e = float(input("\nQuelle est la tension du générateur sur le base? "))

        #CALCUL ET RETOUR
        self.m_rb = (self.m_e - self.m_vbesat)/((2*self.m_icsat)/self.m_beta_min[self.m_beta_reponse-1])
        return m_rb

    def calculResistanceCircuit(self):
        #DEMANDE DES INFORMATIONS
        self.m_icsat = int(input("Quelle valeur de Ic est dans votre montage ? "))
        self.m_vcc = int(input("\nQuelle est la tension du générateur sur le montage ? "))
        self.m_vdiode = int(input("\nQuelle est la tension de la diode ? "))

        #CALCUL ET RETOUR
        self.m_r = (self.m_vcc - self.m_vcesat - self.m_vdiode)/(self.m_icsat)
        return m_r

    def afficherCaracteristiques(self):
        print("\nCARACTERISTIQUES DU TRANSISTOR 2N2222")
        print("Sa tension maximal est de  V".format(self.m_v))
        print("Son courant maximal est de  A".format(self.m_a))
        print("Sa tension de saturation entre le collecteur et l'emeteur est: 1.2 V")
        print("\nSa tension de saturation entre la base et l'emeteur est: 1.8 V")
        print("\nSes coeficient Beta sont:")
        print("   1 - Ic 1 A, Vce 4 V = 25")
        print("   2 - Ic 1 A, Vce 4 V = 10")


        
