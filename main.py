#Importation des modules
import sys
import os
import getpass


#Importation des transistors
from transistor.t2n2222 import *

T2n2222 = T2n2222()

T2n2222.afficherCaracteristiques()

input("Appuyer sur une touche pour continuer...")
