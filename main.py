# -*-coding:Latin-1 -*

#Importation des modules
import sys
import os
import getpass
import locale
import time
import platform

#Importation Autre
from resistance import *
from condensateur import *
from menu import *

#Importation des transistors
from transistor.t2n2222 import *
from transistor.ttip120 import *
from transistor.ttip31c import *

#--------Detection du systeme d'exploitation-----------
#Detection du systeme
systeme = platform.system()

#Definition des commande
if systeme == "Windows":
    effacer = "cls"
elif systeme == "Linux":
    effacer = "clear"

#-----------Creation des variable d'objet--------------
#Divers
Resistance = Resistance()
Condensateur = Condensateur()
#Transistors
T2n2222 = T2n2222()
Ttip120 = Ttip120()
Ttip31c = Ttip31c()

#------------------Initialisation----------------------
menu = True     #Partie menu principal
resistance = False      #Partie resistance
condensateur = False        #Partie transistor
transistor = False      #Partie condensateur
quitter = False     #Quitter le programme

#------------------------Code--------------------------
bienvenue()

while True:
    try:
        #Boucle du menu
        if menu:
            #Choix du menu
            choix_menu_principal = menu_principal()
            if choix_menu_principal == 1:
                resistance = True
            elif choix_menu_principal == 2:
                transistor = True
            elif choix_menu_principal == 3:
                condensateur = True
            elif choix_menu_principal == liste_menu_principal.__len__():
                quitter = True

            #Effacement du menu ou valeur fausse
            if choix_menu_principal in liste_menu_principal:
                menu = False
            else:
                os.system(effacer)
                print("\nVotre choix n'est pas dans le menu !")
                time.sleep(3)
                os.system(effacer)

        #Si resistance
        if resistance:
            #Choix du menu
            choix_menu_resistance = menu_resistance()
            if choix_menu_resistance == 1:
                resultat = Resistance.calculResistance()
                print("La résistance à appliquer est de: {}".format(resultat))
            elif choix_menu_resistance == 2:
                resultat = Resistance.calculPontDiviseurVs()
                print("La tension de sortie est de: {}".format(resultat))
            elif choix_menu_resistance == 3:
                resultat = Resistance.calculPontDiviseurR2()
                print("La résistance R2 à appliquer est de: {}".format(resultat))
            elif choix_menu_resistance == liste_menu_resistance.__len__():
                menu = True

            #Effacement du menu ou valeur fausse
            if choix_menu_principal in liste_menu_principal:
                resistance = False
            else:
                os.system(effacer)
                print("\nVotre choix n'est pas dans le menu !")
                time.sleep(3)
                os.system(effacer)


    #Si interruption du clavier
    except KeyboardInterrupt:
        os.system(effacer)
        print("\nVous allez quitter la programme...")
        time.sleep(3)
        sys.exit(0)

input("Appuyer sur une touche pour continuer...")
