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
from partie_menu import*


#------------------------------------------------------------------------------#
                                #ETAPE no.1:#
                        #Appeler la fonction 'menu'#
#------------------------------------------------------------------------------#

#Création d'une fenetre
root = Tk()
root.title("STAR WARS : LA GUERRE DES ÉTOILES")

c = Canvas(root,heigh=720, width=1280)
c.pack()

#Ajoute une image à la fenetre

fond = Image.open("images/BG2.png")
fond = fond.resize((1280,720))
fond.save(("images/fond.gif"))
fond = PhotoImage(file="images/fond.gif")
c.create_image(0,0, image=fond, anchor=NW)

#Fonction pour appeler la fonction 'menu' avec la touche espace
def access_menu(event):
    global menu
    touche = event.keysym
    if touche == "space":
        root.destroy()
        menu()

root.bind_all('<Key>', access_menu)

root.mainloop()

