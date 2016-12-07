#Liste des items des menu
liste_menu_principal = [1, 2, 3, 4]
liste_menu_resistance = [1, 2, 3, 4]
liste_menu_condensateur = [1, 2, 3]

#Affichage de la banderole de bienvenue
def bienvenue():
    print("+-----------------------------------------------------------+")
    print("| Bienvenue dans le programme regroupant les calculs de SIN |")
    print("+-----------------------------------------------------------+\n\n")

#Affichage du menu principal
def menu_principal():
    print("Sur quelle composant voulez-vous travailler ?")
    print("     1 - Travaille sur les résistance")
    print("     2 - Travaille sur les transistors")
    print("     3 - Travaille sur les condensateur")
    print("     4 - Quitter")
    choix = int(input("\nChoisissez votre choix en tapant un numéro correspondant a un choix: "))
    return choix

def menu_resistance():
    print("Quelle calcul voulez-vous effectuer ?")
    print("     1 - Calculer une resistance pour un composant")
    print("     2 - Calculer la tension de sortie d'un pont diviseur")
    print("     3 - Calculer la resistance R2 dans un pont diviseur")
    print("     4 - Retour")
    choix = int(input("\nChoisissez votre choix en tapant un numéro correspondant a un choix: "))
    return choix

def menu_condensateur():
    print("Quelle calcul voulez-vous effectuer ?")
    print("     1 - Calculer la capacité d'un condensateur pour un filtre")
    print("     2 - Calculer la fréquence de coupure pour un filtre RC")
    print("     3 - Retour")
    choix = int(input("\nChoisissez votre choix en tapant un numéro correspondant a un choix: "))
    return choix
