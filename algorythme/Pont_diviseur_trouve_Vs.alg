<?xml version="1.0" encoding="UTF-8"?>
<Algo>
    <description courant="AFFICHER Vs" texte=""/>
    <extension extnom="inactif"/>
    <fonction fctetat="inactif" fctcode=""/>
    <F2 F2lignes="" F2etat="inactif" F2defaut="" F2para=""/>
    <repere repetat="inactif" repcode="-10#10#-10#10#2#2"/>
    <item code="100#declarationsvariables" algoitem="VARIABLES">
        <item code="1#NOMBRE#R1" algoitem="R1 EST_DU_TYPE NOMBRE"/>
        <item code="1#NOMBRE#R2" algoitem="R2 EST_DU_TYPE NOMBRE"/>
        <item code="1#NOMBRE#Ve" algoitem="Ve EST_DU_TYPE NOMBRE"/>
        <item code="1#NOMBRE#Vs" algoitem="Vs EST_DU_TYPE NOMBRE"/>
    </item>
    <item code="101#debutalgo" algoitem="DEBUT_ALGORITHME">
        <item code="2#R1#pasliste" algoitem="LIRE R1"/>
        <item code="2#R2#pasliste" algoitem="LIRE R2"/>
        <item code="2#Ve#pasliste" algoitem="LIRE Ve"/>
        <item code="5#Vs#(R1/(R1+R2))*Ve#pasliste" algoitem="Vs PREND_LA_VALEUR (R1/(R1+R2))*Ve"/>
        <item code="4#La valeur de la tension en sortie du pont est de: #0" algoitem="AFFICHER &quot;La valeur de la tension en sortie du pont est de: &quot;"/>
        <item code="3#Vs#0#pasliste" algoitem="AFFICHER Vs"/>
    </item>
    <item code="102#finalgo" algoitem="FIN_ALGORITHME"/>
</Algo>
