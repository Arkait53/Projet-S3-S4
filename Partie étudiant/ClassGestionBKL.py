# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 19:08:37 2020
@author: Louison VINCENT
"""

from subprocess import Popen
from os import chdir
from json import load

pathConfig = r".\Config_etudiant.json"

#Récupérer la configuration du fichier pathConfig
file = open(pathConfig, encoding='utf-8')
data = load(file)
file.close()


class GestionBKL:
    def __init__(self):
        pass #On ne fait rien dans l'__init__()

    def lancer(self):
#        """
#        Lance le logiciel BKL en mode caché
#        """
        chdir(r".\basicKeyLogger") #Positionner le répertoire de travaille sur celui de Basic KeyLogger
        Popen(["startHidden.exe"], shell=True)
        chdir(r".\..") #Revenir au répertoire parent

    def arreter(self):
#        """
#        Arrête BKL
#        """
        chdir(r".\basicKeyLogger") #Positionner le répertoire de travaille sur celui de Basic KeyLogger
        Popen(["stopKeyLogger.exe"], shell=True)
        chdir(r".\..") #Revenir au répertoire parent
