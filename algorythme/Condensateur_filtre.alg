<?xml version="1.0" encoding="UTF-8"?>
<Algo>
    <description courant="AFFICHER resultat" texte=""/>
    <extension extnom="inactif"/>
    <fonction fctetat="inactif" fctcode=""/>
    <F2 F2para="" F2lignes="" F2defaut="" F2etat="inactif"/>
    <repere repetat="inactif" repcode="-10#10#-10#10#2#2"/>
    <item code="100#declarationsvariables" algoitem="VARIABLES">
        <item code="1#NOMBRE#frequence" algoitem="frequence EST_DU_TYPE NOMBRE"/>
        <item code="1#NOMBRE#capacité" algoitem="capacité EST_DU_TYPE NOMBRE"/>
        <item code="1#NOMBRE#resistance" algoitem="resistance EST_DU_TYPE NOMBRE"/>
        <item code="1#NOMBRE#choix" algoitem="choix EST_DU_TYPE NOMBRE"/>
        <item code="1#NOMBRE#resultat" algoitem="resultat EST_DU_TYPE NOMBRE"/>
    </item>
    <item code="101#debutalgo" algoitem="DEBUT_ALGORITHME">
        <item code="4#Que voulez vous faire ?#1" algoitem="AFFICHER &quot;Que voulez vous faire ?&quot;"/>
        <item code="4#1 - Determiner fréquence de coupure#1" algoitem="AFFICHER &quot;1 - Determiner fréquence de coupure&quot;"/>
        <item code="4#2 - Determiner capacité du condensateur#1" algoitem="AFFICHER &quot;2 - Determiner capacité du condensateur&quot;"/>
        <item code="2#choix#pasliste" algoitem="LIRE choix"/>
        <item code="6#choix == 1" algoitem="SI (choix == 1) ALORS">
            <item code="7#debutsi" algoitem="DEBUT_SI"/>
            <item code="2#capacité#pasliste" algoitem="LIRE capacité"/>
            <item code="2#resistance#pasliste" algoitem="LIRE resistance"/>
            <item code="5#resultat#1/(2*Math.PI*resistance*capacité)#pasliste" algoitem="resultat PREND_LA_VALEUR 1/(2*Math.PI*resistance*capacité)"/>
            <item code="4#La fréquence de coupure est: #0" algoitem="AFFICHER &quot;La fréquence de coupure est: &quot;"/>
            <item code="3#resultat#0#pasliste" algoitem="AFFICHER resultat"/>
            <item code="8#finsi" algoitem="FIN_SI"/>
            <item code="9#sinon" algoitem="SINON">
                <item code="10#debutsinon" algoitem="DEBUT_SINON"/>
                <item code="2#frequence#pasliste" algoitem="LIRE frequence"/>
                <item code="2#resistance#pasliste" algoitem="LIRE resistance"/>
                <item code="5#resultat#1/(2*Math.PI*resistance*frequence)#pasliste" algoitem="resultat PREND_LA_VALEUR 1/(2*Math.PI*resistance*frequence)"/>
                <item code="4#La capacité du condensateur a mettre est: #0" algoitem="AFFICHER &quot;La capacité du condensateur a mettre est: &quot;"/>
                <item code="3#resultat#0#pasliste" algoitem="AFFICHER resultat"/>
                <item code="11#finsinon" algoitem="FIN_SINON"/>
            </item>
        </item>
    </item>
    <item code="102#finalgo" algoitem="FIN_ALGORITHME"/>
</Algo>
