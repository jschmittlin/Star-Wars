#-*- coding:utf-8 -*-

#------------------------------------------------------------------------------#

#On importe les diffèrentes extention 
from tkinter import*
from PIL import Image,ImageTk
from random import*
import time
#------------------------------------------------------------------------------#


nm_joueur = "jerome"
score_joueur = 40000

def score ():
    global score_joueur,nm_joueur
    fichier = open("score_2.txt", "r")
    score = fichier.read()
    fichier.close()

    score = score.split()
    liste = []



    #rangement dans une double liste ([[j1,s1],[j2,s2],...])

    for k in range (0,len(score),2):
        liste.append([score[k],score[k+1]])
    #ajout du nouveau score 
    liste.append([nm_joueur,score_joueur])

    liste_2 = liste
    #recherche de la position des joueurs
    for k in range (len(liste)):
        position = 0
        for g in range (len(liste)):
            if int(liste[k][1]) < int(liste[g][1]):
                position = position + 1
        liste_2[k].append(position)

    #creaton du classement des joueurs
    liste_3 = []
    for k in range(len(liste_2)):
        for g in range(len(liste_2)):
            if k == liste_2[g][2]:
                liste_3.append(liste_2[g])
                
    #suppression de l'element indiquant la position 
    for k in range (len(liste_3)):
        del liste_3[k][2]

    #creation d'une chaine de caractere avvec les joueur et leur score
    chaine = ""
    for k in range (len(liste_3)):
        chaine = chaine + " " + str(liste_3[k][0]) + " "  + str(liste_3[k][1])

    #sauvegarde des resultat dans un fichier texte
    fichier = open("score_2.txt", "w")
    fichier.write(chaine)
    fichier.close()


    #------------------------------------------------------------------------------#

    #ouverture du fichier des 12 meilleurs scores

    fichier = open("score_2.txt", "r")
    score = fichier.read()
    fichier.close()

    fichier = open("score.txt", "r")
    texte = fichier.read()
    fichier.close()

    score = score.split()
    texte = texte.split()

    texte_2 = []
    for k in range (4):
    #    texte_2.append(texte[0])
        del texte[0]


    for k in range (0,len(score),2):
        if k < 24:
            texte_2.append(texte[k])
            texte_2.append(texte[k+1])
            texte_2.append(score[k])
            texte_2.append(score[k+1])


    texte_3 = []
    texte_3.append("           PLAYER      SCORE                PLAYER        SCORE")
    texte_3.append("\n")
    texte_3.append("\n")

    for k in range (0,len(texte_2),8): 
        texte_3.append(texte_2[k])
        texte_3.append("  ")
        texte_3.append(texte_2[k+1])
        if k < 4.5*8:
            for g in range (int(12 - len(str(texte_2[k+2])))//2):
                texte_3.append(" ")
        else:
            for g in range ((int(12 - len(str(texte_2[k+2])))//2)-1):
                texte_3.append(" ")
        texte_3.append(texte_2[k+2])
        for g in range (int(12 - len(str(texte_2[k+2])))//2):
            texte_3.append(" ")
        for g in range (int(16 - len(str(texte_2[k+3])))//2):
            texte_3.append(" ")
        texte_3.append(texte_2[k+3])
        for g in range (int(16 - len(str(texte_2[k+3])))//2):
            texte_3.append(" ")
            
        if k + 4 != len(texte_2):               
            texte_3.append(texte_2[k+4])
            texte_3.append("  ")
            texte_3.append(texte_2[k+5])
            if k < 4*8:
                for g in range (int(12 - len(str(texte_2[k+6])))//2):
                    texte_3.append(" ")
            else:
                for g in range ((int(12 - len(str(texte_2[k+6])))//2)-1):
                    texte_3.append(" ")
            texte_3.append(texte_2[k+6])
            for g in range (int(12 - len(str(texte_2[k+6])))//2):
                texte_3.append(" ")
            for g in range(int(16 - len(str(texte_2[k+7])))//2):
                texte_3.append(" ")
            texte_3.append(texte_2[k+7])
            texte_3.append("\n")
            texte_3.append("\n")
        else:
            texte_3.append("\n")



    complet = ""
    for k in range(len(texte_3)):
        complet = complet + texte_3[k]

    fichier = open("score_3.txt", "w")
    fichier.write(complet)
    fichier.close()
        
