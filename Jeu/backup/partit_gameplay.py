#-*- coding:utf-8 -*-

#------------------------------------------------------------------------------#

#On importe les diffèrentes extention 
from tkinter import*
from PIL import Image,ImageTk
from random import*
import time
#from partie_endgame import*
#from partie_score import*
import os
from partie_menu import*
#------------------------------------------------------------------------------#

def partit_gameplay():

    global x,y,c,id_player,coord_missile,vitesse_missile,id_missile,coord,id_ennemi,score_joueur,vie_vaisseau,endgame
    
    #creation d'une fenetre
    root = Tk()
    root.title("STAR WARS : LA GUERRE DES ÉTOILES")
    root.geometry("1280x720")
    c = Canvas(root,height=720, width=1280)
    c.pack()

    #insertion d'un fond d'ecran
    fond = Image.open("images/FOND_COLOR.png")
    fond = fond.resize((1280,720))
    fond.save(("images/fond.gif"))
    fond = PhotoImage(file="images/fond.gif")
    c.create_image(0,0, image=fond, anchor=NW)

    #------------------------------------------------------------------------------#

    #creation de l'image du joueur
    x = 640
    y = 500

    vaiseau = Image.open("images/xxx.png")
    vaiseau = vaiseau.resize((100,100))
    vaiseau.save(("images/xxx2.png"))
    player = PhotoImage(file="images/xxx2.png")       
    id_player = c.create_image(x, y, image=player, anchor=NW)
    c.grid(row=1,column=1)

    #definition de la fonction du deplacement du joueur
    def deplacer_player(event):
        global x,y, id_player, c ,fond,endgame
        vitesse_vaisseau = 25
        control = event.keysym

        if control == "Up" or control == "z" :
            if y > vitesse_vaisseau:
                y = y - vitesse_vaisseau
        elif control == "Down" or control == "s":
            if y < 620 - vitesse_vaisseau:
                y = y + vitesse_vaisseau
        elif control == "Right" or control == "d":
            if x < 1180 - vitesse_vaisseau:
                x = x + vitesse_vaisseau
        elif control == "Left" or control == "q":
            if x > vitesse_vaisseau:
                x -= vitesse_vaisseau
        elif control == "Escape" :
            root.destroy()
            endgame()
            
        c.coords(id_player, x, y)

    root.bind_all('<Key>', deplacer_player)

              

    #------------------------------------------------------------------------------#

    #creation des tir allie


    vitesse_missile = 0.5

    missile = Image.open("images/a.png")
    missile = missile.resize((10,60))
    missile.save(("images/a2.png"))
    missile_im = PhotoImage(file="images/a2.png")

    coord_missile = []
    id_missile = []

    def creer_coord_missile():
        global coord_missile , y ,x
        y0 = y - 20
        x0 = x + 85
        y1 = y -20
        x1 = x + 5
        
        coord_missile.append([x0,y0])
        id_missile.append(c.create_image(coord_missile[-1][0], coord_missile[-1][1], image=missile_im, anchor=NW))
        c.pack
        coord_missile.append([x1,y1])
        id_missile.append(c.create_image(coord_missile[-1][0], coord_missile[-1][1], image=missile_im, anchor=NW))
        c.pack
        c.after(1500, creer_coord_missile)
        
    def deplacer_missile():
        global coord_missile ,id_missile ,c, vitesse_missile
        for k in range (len(coord_missile)):
            coord_missile[k][1] -= vitesse_missile
            c.coords(id_missile[k], coord_missile[k][0], coord_missile[k][1])
            c.pack()
        c.after(10, deplacer_missile)

    creer_coord_missile()
    deplacer_missile()


    #------------------------------------------------------------------------------#
    #creation des ennemis avec deplacements automatiques

    vitesse_ennemi = 1

    ennemi = Image.open("images/destroyer.png")
    ennemi = ennemi.resize((100,167))
    ennemi.save(("images/destroyer2.png"))
    ennemi_im = PhotoImage(file="images/destroyer2.png")

    id_ennemi = []
    coord = []

    def creer_coord():
        global coord
        x = randrange(0,1180)
        y = 0
        coord.append([x,y])
        id_ennemi.append(c.create_image(coord[-1][0], coord[-1][1], image=ennemi_im, anchor=NW))
        c.pack()
        c.after(2000, creer_coord)
        
    def deplacer_ennemi():
        global coord ,id_ennemi ,c
        for k in range (len(coord)):
            coord[k][1] += vitesse_ennemi
            c.coords(id_ennemi[k], coord[k][0], coord[k][1])
            c.pack()
        c.after(10, deplacer_ennemi)

    creer_coord()
    deplacer_ennemi()

    #------------------------------------------------------------------------------#
    #destruction des vaisseaux
    score_joueur = 0
    def destruction_ennemi():
        global coord, coord_missile, id_ennemi , id_missile, c ,root ,ennemi_im ,score_joueur
        liste_4 = []
        liste_5 =[]
        for k in range(len(coord)):
            for g in range(len(coord_missile)):
                if coord[k][0] < coord_missile[g][0] :
                    if coord_missile[g][0] < coord[k][0]+90:
                        if coord[k][1] < coord_missile[g][1]:
                            if coord_missile[g][1] < coord[k][1]+157:
                                score_joueur = score_joueur + 100
                                point = 0
                                for h in range(len(liste_4)):
                                    if liste_4[h] == k :
                                        point = 1
                                if point != 1:
                                    liste_5.append(g)
                                    liste_4.append(k)

                                    
        while len(liste_4) != 0:
            c.delete(id_ennemi[liste_4[-1]])
            del(coord[liste_4[-1]])
            del(id_ennemi[liste_4[-1]])
            del(liste_4[-1])

        while len(liste_5) != 0:
            c.delete(id_missile[liste_5[-1]])
            del(coord_missile[liste_5[-1]])  
            del(id_missile[liste_5[-1]])
            del(liste_5[-1])

            
        c.after(100,destruction_ennemi)

    destruction_ennemi()

    vie_vaisseau = 100

    def destruction_vaisseau():
        liste_6 = []
        global coord ,id_ennemi ,id_player ,x ,y ,vie_vaisseau ,c
        for k in range (len(coord)):
            if (x < coord[k][0] + 100 and x > coord[k][0]) or (x + 100 > coord[k][0] and x + 100 < coord[k][0] + 100):
                if (y < coord[k][1] + 167 and y > coord[k][0]) or (y + 100 > coord[k][1] and y + 100 < coord[k][1] + 167):
                    vie_vaisseau -= 10
                    print(vie_vaisseau)
                    liste_6.append(k)
        
        while len(liste_6) != 0:
            c.delete(id_ennemi[liste_6[-1]])
            del(coord[liste_6[-1]])
            del(id_ennemi[liste_6[-1]])
            del(liste_6[-1])
      
        c.after(1,destruction_vaisseau)
                    
    destruction_vaisseau()

    def check_vie():
        global vie_vaisseau,endgame
        if vie_vaisseau <= 0:
            root.destroy()
            endgame()
        c.after(1000,check_vie)
    
    check_vie()

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
        police1 = tkFont.Font(family='Tw Cen MT Condensed Extra Bold', size= 25, weight='bold')

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
        
        etiquette = Label(zone_bouton, text="ENTREE VOTRE PSEUDO", font=police, bg="white", fg="black")

        etiquette.grid(row=1,column=1)
        
        while nm_joueur == "" or len(str(nm_joueur)) >= 12:
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
        
        return nm_joueur

        fenetre_end.mainloop()


     
    root.mainloop()

