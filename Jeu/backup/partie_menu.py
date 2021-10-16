#-*- coding:utf-8 -*-

#------------------------------------------------------------------------------#

#On importe les diffèrentes extention
from tkinter import*
from PIL import Image,ImageTk
import pygame
from pygame.locals import*
import tkinter.font as tkFont
import os
from random import*
import time
#from partie_endgame import*
from partit_gameplay import*



#------------------------------------------------------------------------------#
                                #ETAPE no.2:#
                              #Création du menu#
#------------------------------------------------------------------------------#

#Définition de la fonction menu
def menu():

    global menu_principal

    try:
        root.destroy()
    except:
        pass
    
   
    #Création de la fenetre du menu principal 
    menu_principal = Tk()
    menu_principal.title("Menu Principal")
    menu_principal.configure(bg="white")
    menu_principal.geometry("1280x720")

    #Création de zones
    zone_1 = Frame(menu_principal)
    zone_1.grid(row=0,column=2,padx=0,pady=0)
    
    zone_2 = Frame(menu_principal)
    zone_2.grid(row=0,column=3,padx=0,pady=0)

    zone_3 = Frame(menu_principal)
    zone_3.grid(row=0,column=1,padx=0,pady=0)
    
    #Insertion d'image à des zones
    background = Canvas(zone_2, width=1000, height=720)
    
    im = Image.open("images/MenuBGG.png")
    im.save(("images/MENUBG.gif"))
    
    im = PhotoImage(file="images/MENUBG.gif")
    background.create_image(0,0, image=im, anchor=NW)
    background.pack()

    bgg = Canvas(zone_3, width=120, height=720)
    
    ima = Image.open("images/FOND_COLOR.png")
    ima = ima.resize((1280,720))
    ima.save(("images/fond.gif"))
    
    ima = PhotoImage(file="images/fond.gif")
    bgg.create_image(0,0, image=ima, anchor=NW)
    bgg.pack()
    
    #Mise en place de la police écriture

    police = tkFont.Font(family='Tw Cen MT Condensed Extra Bold', size= 12, weight='bold')
    police1 = tkFont.Font(family='Tw Cen MT Condensed Extra Bold', size= 25, weight='bold')
        
    #Création des boutons dans la zone 1
    bouton_1 = Button(zone_1)
    bouton_1.configure(text="NOUVELLE PARTIE",bg="white",fg="black", width="20", height="1", relief=FLAT, font=police)
    bouton_1.grid(row=1,column=1)

    bouton_2 = Button(zone_1)
    bouton_2.configure(text="DIDACTICIELS",bg="white",fg="black", width="20", height="1", relief=FLAT, font=police)
    bouton_2.grid(row=3,column=1)

    bouton_3 = Button(zone_1)
    bouton_3.configure(text="SCORE",bg="white",fg="black", width="20", height="1", relief=FLAT, font=police)
    bouton_3.grid(row=5,column=1)

    bouton_4 = Button(zone_1)
    bouton_4.configure(text="QUITTER LE JEU",bg="white",fg="black", width="20", height="1", relief=FLAT, font=police)
    bouton_4.grid(row=7,column=1)
    
#------------------------------------------------------------------------------#
                                #ETAPE no.3:#
                      #Création des extentions du menu#
#------------------------------------------------------------------------------#
    
#Création des fonctions pour le menu:

##Création de la fonction 'Didacticiels':
    def instruction(event):
        
    #Création de la fenetre 
        fenetre_intro = Toplevel()
        fenetre_intro.title("Didacticiels")
        fenetre_intro.configure(bg="black")
        fenetre_intro.geometry("1280x720")

    #Insertion de 2 zones
        zone_intro_image = Frame(fenetre_intro)
        zone_intro_image.grid(row=0,column=0,padx=0,pady=0)
        
        zone_intro_bouton = Frame(fenetre_intro)
        zone_intro_bouton.grid(row=0,column=1,padx=0,pady=0)

    #Ajoute une image a une des zones
        background1 = Canvas(zone_intro_image, width=1220, height=720)
        
        im_intro = Image.open("images/didacticiels.png")
        im_intro = im_intro.resize((1220,720))
        im_intro.save(("images/didact.gif"))
    
        im_intro = PhotoImage(file="images/didact.gif")
        background1.create_image(0,0, image=im_intro, anchor=NW)
        background1.pack()

    #Création du bouton retour dans l'autre zone   
        bouton_retour = Button(zone_intro_bouton)
        bouton_retour.configure(text="RETOUR",bg="black",fg="white", width="5", height="33", relief=FLAT, font=police)
        bouton_retour.grid(row=0,column=0)

    #Définition de la fonction retour associer au bouton retour
        def retour(event):
            fenetre_intro.destroy()
        
        bouton_retour.bind("<ButtonPress-1>",retour)
        
        fenetre_intro.mainloop()
        

##Création de la fonction 'quitter':   
    def quitter(event):
        menu_principal.destroy()
        
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
       

##Création de la fonction 'jouer':
    def jouer(event):
        menu_principal.destroy() 
        partit_gameplay()
        

        
        

##Association des boutons du menu au différentes fonctions
    bouton_3.bind("<ButtonPress-1>",score)
    bouton_4.bind("<ButtonPress-1>",quitter)
    bouton_2.bind("<ButtonPress-1>",instruction)
    bouton_1.bind("<ButtonPress-1>",jouer)
    
    menu_principal.mainloop()

