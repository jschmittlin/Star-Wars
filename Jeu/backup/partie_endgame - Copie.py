#-*- coding:utf-8 -*-

#------------------------------------------------------------------------------#

#On importe les diffèrentes extention 
from tkinter import*
from PIL import Image,ImageTk
from random import*
import time
import tkinter.font as tkFont
import os
from partie_menu import*
from partie_score import*
#------------------------------------------------------------------------------#

 
##définition de la fonction lorsque la vie du joueur est nul
def endgame():
    global menu, score
    #Création d'une nouvelle fenetre
    fenetre_end = Tk()
    fenetre_end.title("MENU ENDGAME")
    fenetre_end.geometry("1280x720")

    #mise en place des zones
    zone_bouton = Frame(fenetre_end)
    zone_deco1 = Frame(fenetre_end)
    zone_deco2 = Frame(fenetre_end)

    police = tkFont.Font(family='Tw Cen MT Condensed Extra Bold', size= 12, weight='bold')


    #on définie l'emplacements des zones
    zone_bouton.grid(row=0,column=2,padx=0,pady=0)
    zone_deco1.grid(row=0,column=1,padx=0,pady=0)
    zone_deco2.grid(row=0,column=3,padx=0,pady=0)

    #création des boutons
    bouton_menu = Button(zone_bouton)
    bouton_score1 = Button(zone_bouton)
    bouton_quit = Button(zone_bouton)

    #on configure les boutons
    bouton_menu.configure(text="RETOURNER AU MENU PRINCIPAL",bg="white",fg="black", width="20", height="1", relief=FLAT, font=police)
    bouton_score1.configure(text="SCORE",bg="white",fg="black", width="20", height="1", relief=FLAT, font=police)
    bouton_quit.configure(text="QUITTER LE JEU",bg="white",fg="black", width="20", height="1", relief=FLAT, font=police)

    #on définie l'emplacements des boutons
    bouton_menu.grid(row=3,column=1)    
    bouton_score1.grid(row=5,column=1)
    bouton_quit.grid(row=7,column=1)

    #zone de saisie du pseudo du joueur
    
    nm_joueur = StringVar()
    entree = Entry(zone_bouton, textvariable=nm_joueur.get(), width="21")
    entree.configure(bg="white",fg="black", relief=FLAT, font=police)
    entree.grid(row=2,column=1)
    
    etiquette = Label(zone_bouton, text="ENTREE VOTRE PSEUDO", font=police, bg="white", fg="black").pack(padx=0, pady=0)
    etiquette.grid(row=1,column=1)
    
    while nm_joueur == "" or len(nm_joueur) >= 12:
        etiquette.configure(text="ENTREE VOTRE PSEUDO !!")
        
    score()
    
    def bouton_menue(event):
        fenetre_end.destroy()
        menu()

    def bouton_quitter(event):
        fenetre_end.destroy()

    ##Création de la fonction 'score':
    def score(event):

    #Création d'une fenetre
        fenetre_score = Toplevel()
        fenetre_score.title("Tableau des Scores")
        fenetre_score.configure(bg="black")
        fenetre_score.geometry("1280x720")
        
    #Insertion de zones
        zone_score_image = Frame(fenetre_score)
        zone_score_bouton = Frame(fenetre_score)
        zone_score_table = Frame(fenetre_score)
        
        zone_score_table.grid(row=1,column=0,padx=2,pady=0)
        zone_score_bouton.grid(row=1,column=1,padx=0,pady=0)
        zone_score_image.grid(row=0,column=0,padx=0,pady=0)
        
    #Ajoute une image a une des zones
        bgSC = Canvas(zone_score_image, width=1210, height=165)
        
        im_SC = Image.open("images/logo.png")
        im_SC = im_SC.resize((1210,165))
        im_SC.save(("images/logo.gif"))
    
        im_SC = PhotoImage(file="images/logo.gif")
        bgSC.create_image(0,0, image=im_SC, anchor=NW)
        bgSC.pack()

    #Création graphique du tableau des scores

        fichier = open("score_3.txt", "r")
        content = fichier.read()
        fichier.close()
        

        Label(zone_score_table, text=content, font=police1, bg="black", fg="white").pack(padx=0, pady=0)

    #Création du bouton retour dans l'autre zone   
        bouton_retour = Button(zone_score_bouton)
        bouton_retour.configure(text="RETOUR",bg="black",fg="white", width="5", height="29", relief=FLAT, font=police)
        bouton_retour.grid(row=0,column=0)
        
    #Définition de la fonction retour associer au bouton retour
        def retour(event):
            fenetre_score.destroy()
        
        bouton_retour.bind("<ButtonPress-1>",retour)

        fenetre_score.mainloop()

        
    bouton_menu.bind("<ButtonPress-1>",bouton_menue)
    bouton_quit.bind("<ButtonPress-1>",bouton_quitter)
    bouton_score1.bind("<ButtonPress-1>",score)
    
    return pseudo

    fenetre_end.mainloop()

