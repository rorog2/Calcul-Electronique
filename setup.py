"""Fichier d'installation un programme"""

from cx_Freeze import setup, Executable


setup(
	name = "Calcul de transistor",
	version = "1.0",
	description = "Ce programme est un test",
	executables = [Executable("F:\DATA\Documents\Dropbox\Travail\Logiciels\Calcul de transistor python\main.py")],
)