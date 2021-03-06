# -*- coding: utf-8 -*-
from tkinter import Tk,Button,Label,LEFT,RIGHT,WORD,BOTH,INSERT
import tkinter.font as tkFont
import tkinter.scrolledtext as tkst
from ClassGestionBKL import GestionBKL
from ClassGestionPSR import GestionPSR
from json import load
from sys import exit

pathConfig = r".\Config_etudiant.json"

#Récupérer la configuration
file = open(pathConfig, encoding='utf-8')
data = load(file)
file.close()
cheminDossierPSR = ".\\"

def fenetreEnSavoirPlus(self):
#    """
#    Cette méthode permet d'afficher la fenêtre montrant la charte juridique du projet
#    """
    monFichier = open("charteJuridique.txt","r",encoding="utf-8") #Ouverture en mode lecture du fichier contenant la charte juridique
    fenetreESP = Tk() #création de la fenêtre
    fenetreESP.attributes("-topmost",True) #Permet de donner le focus à cette fenêtre
    fenetreESP.title("En savoir plus")
    editArea = tkst.ScrolledText(master = fenetreESP, wrap = WORD) #Création de la zone contenant le texte avec une scrollbar
    editArea.pack(padx=10,pady=10,fill=BOTH,expand=True)
    editArea.insert(INSERT,monFichier.read())
    boutonFermer= Button(fenetreESP,text="Fermer", command=fenetreESP.destroy) #Création du bouton permettant de fermer la fenêtre
    boutonFermer.pack(side=RIGHT) #placement du bouton a droite de la fenêtre
    fenetreESP.pack()
    monFichier.close() #Fermeture du fichier

def affichageFenetreAutorisation():
#    """
#    Cette méthode permet d'afficher la fenêtre demandant l'autorisation de l'étudiant sur la collecte de ces traces.
#    Si l'étudiant accepte, cette méthode affichera la fenêtre permettant de mettre en pause la collecte et lancera les différents logiciels de capture de traces
#    Sinon cette méthode fermera l'application
#    """
    fenetreCommencerExercice.destroy() #Ferme la fenêtre précédente
    fenetreAutorisation = Tk() #Création de la fenêtre demandant l'autorisation
    fenetreAutorisation.title("New Window")
    label = Label(fenetreAutorisation, text="Acceptez-vous que vos données soient enregistrées dans un cadre pédagogique ?")
    label.pack()

    labelEnSavoirPlus = Label(fenetreAutorisation, text="En savoir plus",fg="blue") #Création du lien hypertexte qui ouvrira la fenêtre avec la charte juridique
    labelEnSavoirPlus.pack(side = LEFT)
    myfont = tkFont.Font(labelEnSavoirPlus, labelEnSavoirPlus.cget("font"))
    myfont.configure(underline = True)
    labelEnSavoirPlus.configure(font=myfont)
    labelEnSavoirPlus.bind("<Button-1>", fenetreEnSavoirPlus)

    boutonAccepter = Button(fenetreAutorisation,text="J'accepte", command=lambda: fenetreArreterExercice(fenetreAutorisation)) #Création du bouton permettant à l'étudiant d'accepter la collecte des données
    boutonAccepter.pack(side=RIGHT)
    boutonRefuser= Button(fenetreAutorisation,text="Je refuse", command=fenetreAutorisation.destroy) #Création du bouton permettant à l'étudiant de refuser la collecte des données
    boutonRefuser.pack(side=RIGHT)

    fenetreAutorisation.mainloop()

def fenetreArreterExercice(fenetreAutorisation):
#    """
#    Cette méthode permet d'afficher la fenêtre pour arreter l'exercice et les logiciels de capture de traces
#    """
    monBKL = GestionBKL()
    monPSR = GestionPSR(cheminDossierPSR)
    monPSR.lancer()
    fenetreAutorisation.destroy() #Ferme la fenêtre en savoir plus
    fenetreArret = Tk() #Création de la fenetre
    fenetreArret.geometry('200x50')
    fenetreArret.title("Système d'analyse de traces - Arreter l'exercice")
    fenetreArret.protocol("WM_DELETE_WINDOW", lambda: arreterExercice(monPSR,monBKL,fenetreArret))
    boutonArreterExercice = Button(fenetreArret, text="Arrêter exercice", command=lambda: arreterExercice(monPSR,monBKL,fenetreArret))
    boutonArreterExercice.config(height =150,width=40)
    boutonArreterExercice.pack()
    monBKL.lancer()
    fenetreArret.mainloop()

def arreterExercice(monPSR,monBKL,fenetreArret):
#    """
#    Cette méthode permet d'arreter les keyloggers et de fermer le programme
#    """
    monBKL.arreter()
    monPSR.arreter()
    fenetreArret.destroy()
    exit()
    
fenetreCommencerExercice = Tk() #Création de la fenêtre pour commencer l'exercice
fenetreCommencerExercice.geometry('200x50')
fenetreCommencerExercice.title("Système d'analyse de traces - Commencer l'exercice")
boutonCommencerExercice = Button(fenetreCommencerExercice, text="Commencer exercice", command=affichageFenetreAutorisation)
boutonCommencerExercice.config(height =150,width=40)
boutonCommencerExercice.pack()
fenetreCommencerExercice.mainloop()
