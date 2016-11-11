#Importation des modules
import sys
import os
import getpass

#Importation Autre
from resistance import *
from condensateur import *

#Importation des transistors
from transistor.t2n2222 import *
from transistor.ttip120 import *
from transistor.ttip31c import *

#Création des variable d'objet
T2n2222 = T2n2222()
Ttip120 = Ttip120()
Ttip31c = Ttip31c()

#Code

T2n2222.afficherCaracteristiques()

input("Appuyer sur une touche pour continuer...")
