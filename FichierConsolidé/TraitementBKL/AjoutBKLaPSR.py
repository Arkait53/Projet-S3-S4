# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 22:45:00 2020
@author: paul6
"""


#RIEN N'EST FINI ICI ! TOUTE LA PARTIE D'AJOUT EST ENCORE A FAIRE

from lxml import etree
from TraitementBasicKeyLogger import BKLtoTxt
from TraitementBasicKeyLogger import Mot


def heureToNb(heure):
    (h, m, s) = heure.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)

conversion = BKLtoTxt('kpc_log.tsv')

tableauMots = conversion.recupererPhrases()

tableauActionsTxt = []


tree = etree.parse("testing.xml")

root = tree.getroot()
etree.tostring(root)

for action in root.xpath('/Report/UserActionData/RecordSession/EachAction/Action/text()'):
    #print(action)
    if action == "Saisie au clavier":
        parent = action.getparent().getparent() #Balise EachAction associée
        debutActionPSR = parent.get("Time")
        
        for mot in tableauMots:
            if(heureToNb(mot.getHeureDebut()) < heureToNb(debutActionPSR) or heureToNb(mot.getHeureFin()) > heureToNb(debutActionPSR)):
                break
            
            print("Ajouter le texte au BKL")
            
            #baliseTxt = etree.Element("texte")
            #baliseTxt.set("heureDebut", mot.getHeureDebut())
            
            
            #tableauActionsTxt.append(parent)
            
            
            
        
        #baliseTxt = etree.Element("texte")
        
        #parent.insert(parent.index(name)+1, etree.XML('<name>testage</name>'))
        

