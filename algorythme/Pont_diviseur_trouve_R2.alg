<?xml version="1.0" encoding="UTF-8"?>
<Algo>
    <description courant="AFFICHER R2" texte=""/>
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
        <item code="2#Vs#pasliste" algoitem="LIRE Vs"/>
        <item code="2#Ve#pasliste" algoitem="LIRE Ve"/>
        <item code="5#R2#R1*(Ve/Vs)-R1#pasliste" algoitem="R2 PREND_LA_VALEUR R1*(Ve/Vs)-R1"/>
        <item code="4#La valeur de la résistance R2 pour une tension de : #0" algoitem="AFFICHER &quot;La valeur de la résistance R2 pour une tension de : &quot;"/>
        <item code="3#Vs#0#pasliste" algoitem="AFFICHER Vs"/>
        <item code="4# volt en sortie du pont est de: #0" algoitem="AFFICHER &quot; volt en sortie du pont est de: &quot;"/>
        <item code="3#R2#0#pasliste" algoitem="AFFICHER R2"/>
    </item>
    <item code="102#finalgo" algoitem="FIN_ALGORITHME"/>
</Algo>
