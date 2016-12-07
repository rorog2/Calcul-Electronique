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
Resistance = Resistance()
Condensateur = Condensateur()

#------------------Initialisation----------------------
#Boucle principal
principal = True
menu = True     #Partie menu principal
resistance = False      #Partie resistance
condensateur = False        #Partie transistor
transistor = False      #Partie condensateur
quitter = False     #Quitter le programme

#Boucle d'arguments
caracteristique_transistor = False

#Arguments

arg = sys.argv[1]       #Argument du fichier

#Condition d'argument
if arg == "caractransistor":
    principal = False
    caracteristique_transistor = True
else:
    principal = True
    caracteristique_transistor = False

#------------------------Code--------------------------
bienvenue()

#Boucle principal
while principal:
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
                menu = True
            else:
                os.system(effacer)
                print("\nVotre choix n'est pas dans le menu !")
                time.sleep(3)
                os.system(effacer)

        #Si condensateur
        if condensateur:
            #Choix du menu
            choix_menu_condensateur = menu_condensateur()
            if choix_menu_condensateur == 1:
                resultat = Condensateur.calculCapaciteCondensateur()
                print("La résistance à appliquer est de: {}".format(resultat))
            elif choix_menu_condensateur == 2:
                resultat = Condensateur.calculFrequenceCoupure()
                print("La tension de sortie est de: {}".format(resultat))
            elif choix_menu_condensateur == liste_menu_condensateur.__len__():
                menu = True

            #Effacement du menu ou valeur fausse
            if choix_menu_condensateur in liste_menu_condensateur:
                condensateur = False
                menu = True
            else:
                os.system(effacer)
                print("\nVotre choix n'est pas dans le menu !")
                time.sleep(3)
                os.system(effacer)

        #Si quitter
        if quitter:
            os.system(effacer)
            print("\nVous allez quitter le programme...")
            time.sleep(3)
            sys.exit(0)

    #Si interruption du clavier
    except KeyboardInterrupt:
        os.system(effacer)
        print("\nVous allez quitter la programme...")
        time.sleep(3)
        sys.exit(0)

#+++++++++++++++++++++++++++Separation arguments++++++++++++++++++++++++++++
if caracteristique_transistor == True:
        T2n2222().afficherCaracteristique()
        Ttip31c().afficherCaracteristique()
        Ttip120().afficherCaracteristique()

input("Appuyer sur une touche pour continuer...")
