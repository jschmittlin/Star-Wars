#-*- coding:utf-8 -*-

#------------------------------------------------------------------------------#
#On importe les diffèrentes extention

from tkinter import*
from PIL import Image,ImageTk
import tkinter.font as tkFont
import os
from random import*
import time
#------------------------------------------------------------------------------#

#Création d'une fenetre
root = Tk()
root.title("STAR WARS : LA GUERRE DES ÉTOILES")

c = Canvas(root,heigh=720, width=1280)
c.pack()

#Ajoute une image à la fenetre

fond = Image.open("Jeu/images/BG2.png")
fond = fond.resize((1280,720))
fond.save(("Jeu/images/fond.gif"))
fond = PhotoImage(file="Jeu/images/fond.gif")
c.create_image(0,0, image=fond, anchor=NW)

#Fonction pour appeler la fonction 'menu' avec la touche espace
def access_menu(event):
    global menu_principal, score, police, police1,menu, BGD1,BGD2
    touche = event.keysym
    
    if touche == "space":
        root.destroy()
        def menu():
            global score,police,police1, BGD1,BGD2
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
            
            im = Image.open("Jeu/images/MenuBGG.png")
            im.save(("Jeu/images/MENUBG.gif"))
            
            im = PhotoImage(file="Jeu/images/MENUBG.gif")
            background.create_image(0,0, image=im, anchor=NW)
            background.pack()

            bgg = Canvas(zone_3, width=120, height=720)
            
            ima = Image.open("Jeu/images/FOND_COLOR.png")
            ima = ima.resize((1280,720))
            ima.save(("Jeu/images/fond.gif"))
            
            ima = PhotoImage(file="Jeu/images/fond.gif")
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

            #Création des fonctions pour le menu:

            #Création de la fonction 'Didacticiels':
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
                
                im_intro = Image.open("Jeu/images/didacticiels.png")
                im_intro = im_intro.resize((1220,720))
                im_intro.save(("Jeu/images/didact.gif"))
            
                im_intro = PhotoImage(file="Jeu/images/didact.gif")
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

            #Création de la fonction 'quitter':   
            def quitter(event):
                menu_principal.destroy()
                
            #Création de la fonction 'score':
            def score(event):
                global police,police1
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
                
                im_SC = Image.open("Jeu/images/logo.png")
                im_SC = im_SC.resize((1210,165))
                im_SC.save(("Jeu/images/logo.gif"))
            
                im_SC = PhotoImage(file="Jeu/images/logo.gif")
                bgSC.create_image(0,0, image=im_SC, anchor=NW)
                bgSC.pack()

                #Création graphique du tableau des scores
                fichier = open("Jeu/score_3.txt", "r")
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

            #Création de la fonction 'jouer':
            def jouer(event):
                global x,y,c,id_player,coord_missile,vitesse_missile,id_missile,coord,id_ennemi,score_joueur,vie_vaisseau,e,nm_joueur
                menu_principal.destroy() 
                #creation d'une fenetre
                root2 = Tk()
                root2.title("STAR WARS : LA GUERRE DES ÉTOILES")
                root2.geometry("1280x720")
                c = Canvas(root2,height=720, width=1280)
                c.pack()

                #insertion d'un fond d'ecran
                fond = Image.open("Jeu/images/FOND_COLOR.png")
                fond = fond.resize((1280,720))
                fond.save(("Jeu/images/fond.gif"))
                fond = PhotoImage(file="Jeu/images/fond.gif")
                c.create_image(0,0, image=fond, anchor=NW)

                #creation de l'image du joueur
                x = 640
                y = 500
                vaiseau = Image.open("Jeu/images/XXX.png")
                vaiseau = vaiseau.resize((90,108))
                vaiseau.save(("Jeu/images/x2.png"))
                player = PhotoImage(file="Jeu/images/x2.png")       
                id_player = c.create_image(x, y, image=player, anchor=NW)
                c.grid(row=1,column=1)

                #definition de la fonction du deplacement du joueur
                def deplacer_player(event):
                    global x,y, id_player, c  ,fond, menu, score, fenetre_end, police, police1,BGD1,BGD2,imD1,imD2,nm_joueur,score_joueur
                    vitesse_vaisseau = 23
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
                        root2.destroy()
                        #Création d'une nouvelle fenetre
                        fenetre_end = Tk()
                        fenetre_end.title("MENU ENDGAME")
                        fenetre_end.configure(bg="white")
                        fenetre_end.geometry("1280x720")

                        #mise en place des zones
                        zone_bouton = Frame(fenetre_end)
                        zone_deco1 = Frame(fenetre_end)
                        zone_deco2 = Frame(fenetre_end)

                        #on définie l'emplacements des zones
                        zone_bouton.grid(row=1,column=2,padx=0,pady=0)
                        zone_deco1.grid(row=1,column=1,padx=0,pady=0)
                        zone_deco2.grid(row=1,column=3,padx=0,pady=0)

                        #création des boutons
                        bouton_menu = Button(zone_bouton)
                        bouton_score1 = Button(zone_bouton)
                        bouton_quit = Button(zone_bouton)

                        #mise en place d'image
                        BGD1 = Canvas(zone_deco1, width=500, height=720)
                        imD1 = Image.open("Jeu/images/FOND_COLOR.png")
                        imD1.save(("Jeu/images/fond.gif"))
                        imD1 = PhotoImage(file="Jeu/images/fond.gif")
                        BGD1.create_image(0,0, image=imD1, anchor=NW)
                        BGD1.pack()


                        BGD2 = Canvas(zone_deco2, width=500, height=720)
                        imD2 = Image.open("Jeu/images/FOND_COLOR.png")
                        imD2.save(("Jeu/images/fond.gif"))
                        imD2 = PhotoImage(file="Jeu/images/fond.gif")
                        BGD2.create_image(0,0, image=imD2, anchor=NW)
                        BGD2.pack()

                        #Mise en place de la police écriture
                        police = tkFont.Font(family='Tw Cen MT Condensed Extra Bold', size= 12, weight='bold')
                        police1 = tkFont.Font(family='Tw Cen MT Condensed Extra Bold', size= 25, weight='bold')

                        #on configure les boutons
                        bouton_menu.configure(text="RETOURNER AU MENU PRINCIPAL",bg="white",fg="black", width="30", height="1", relief=FLAT, font=police)
                        bouton_score1.configure(text="TABLEAUX DES SCORES",bg="white",fg="black", width="30", height="1", relief=FLAT, font=police)
                        bouton_quit.configure(text="QUITTER LE JEU",bg="white",fg="black", width="30", height="1", relief=FLAT, font=police)

                        #on définie l'emplacements des boutons
                        bouton_menu.grid(row=7,column=1)    
                        bouton_score1.grid(row=8,column=1)
                        bouton_quit.grid(row=9,column=1)

                        #zone de saisie du pseudo du joueur
                        
                        nm_joueur = StringVar()
                        entree = Entry(zone_bouton, textvariable=nm_joueur.get(), width="31")
                        entree.configure(bg="white",fg="grey", relief=FLAT, font=police)
                        entree.grid(row=6,column=1)
                        
                        etiquette = Label(zone_bouton, text="ENTREE VOTRE PSEUDO", font=police, bg="white", fg="black")
                        etiquette.configure(width="30")
                        etiquette.grid(row=5,column=1)

                        etiquette2 = Label(zone_bouton, text="VOUS AVEZ", font=police1, bg="white", fg="red")
                        etiquette2.configure(width="17")
                        etiquette2.grid(row=0,column=1)

                        etiquette2 = Label(zone_bouton, text="ABANDONNER", font=police1, bg="white", fg="red")
                        etiquette2.configure(width="17")
                        etiquette2.grid(row=1,column=1)

                        etiquette2 = Label(zone_bouton, text=" ", font=police1, bg="white", fg="red")
                        etiquette2.configure(width="17")
                        etiquette2.grid(row=2,column=1)

                        etiquette2 = Label(zone_bouton, text="SCORE OBTENUE " + str(score_joueur), font=police, bg="white", fg="black")
                        etiquette2.configure(width="30")
                        etiquette2.grid(row=3,column=1)
                        
                        while nm_joueur == "" or len(str(nm_joueur)) >= 12:
                            etiquette.configure(text="ENTREE VOTRE PSEUDO !!")

                            fichier = open("Jeu/score_2.txt", "r")
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
                            fichier = open("Jeu/score_2.txt", "w")
                            fichier.write(chaine)
                            fichier.close()

                            #ouverture du fichier des 12 meilleurs scores
                            fichier = open("Jeu/score_2.txt", "r")
                            score = fichier.read()
                            fichier.close()

                            fichier = open("Jeu/score.txt", "r")
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

                            fichier = open("Jeu/score_3.txt", "w")
                            fichier.write(complet)
                            fichier.close()
                        
                        def bouton_menue(event):
                            fenetre_end.destroy()
                            menu()

                        def bouton_quitter(event):
                            fenetre_end.destroy()
             
                        bouton_menu.bind("<ButtonPress-1>",bouton_menue)
                        bouton_quit.bind("<ButtonPress-1>",bouton_quitter)
                        bouton_score1.bind("<ButtonPress-1>",score)
                        
                        return nm_joueur

                        fenetre_end.mainloop()
                      
                    c.coords(id_player, x, y)

                root2.bind_all('<Key>', deplacer_player)

                #creation des tir allie
                vitesse_missile = 10

                missile = Image.open("Jeu/images/missile.png")
                missile = missile.resize((10,60))
                missile.save(("Jeu/images/miss.png"))
                missile_im = PhotoImage(file="Jeu/images/miss.png")

                coord_missile = []
                id_missile = []

                def creer_coord_missile():
                    global coord_missile , y ,x
                    y0 = y - 19
                    x0 = x + 82
                    y1 = y - 19
                    x1 = x - 2
                    
                    coord_missile.append([x0,y0])
                    id_missile.append(c.create_image(coord_missile[-1][0], coord_missile[-1][1], image=missile_im, anchor=NW))
                    c.pack
                    coord_missile.append([x1,y1])
                    id_missile.append(c.create_image(coord_missile[-1][0], coord_missile[-1][1], image=missile_im, anchor=NW))
                    c.pack
                    c.after(2000, creer_coord_missile)
                    
                def deplacer_missile():
                    global coord_missile ,id_missile ,c, vitesse_missile
                    for k in range (len(coord_missile)):
                        coord_missile[k][1] -= vitesse_missile
                        c.coords(id_missile[k], coord_missile[k][0], coord_missile[k][1])
                        c.pack()
                    c.after(35, deplacer_missile)

                creer_coord_missile()
                deplacer_missile()
                
                #creation des ennemis avec deplacements automatiques
                vitesse_ennemi = 2

                ennemi = Image.open("Jeu/images/destroyer.png")
                ennemi = ennemi.resize((110,197))
                ennemi.save(("Jeu/images/destroyer2.png"))
                ennemi_im = PhotoImage(file="Jeu/images/destroyer2.png")

                id_ennemi = []
                coord = []

                def creer_coord():
                    global coord
                    x = randrange(0,1180)
                    y = 0
                    coord.append([x,y])
                    id_ennemi.append(c.create_image(coord[-1][0], coord[-1][1], image=ennemi_im, anchor=NW))
                    c.pack()
                    c.after(1600, creer_coord)
                    
                def deplacer_ennemi():
                    global coord ,id_ennemi ,c
                    for k in range (len(coord)):
                        coord[k][1] += vitesse_ennemi
                        c.coords(id_ennemi[k], coord[k][0], coord[k][1])
                        c.pack()
                        
                    c.after(30, deplacer_ennemi)

                creer_coord()
                deplacer_ennemi()

                #destruction des vaisseaux
                score_joueur = 0
                def destruction_ennemi():
                    global coord, coord_missile, id_ennemi , id_missile, c ,root ,ennemi_im ,score_joueur
                    liste_4 = []
                    liste_5 =[]
                    for k in range(len(coord)):
                        for g in range(len(coord_missile)):
                            if coord[k][0] < coord_missile[g][0] :
                                if coord_missile[g][0] < coord[k][0]+110:
                                    if coord[k][1] < coord_missile[g][1]:
                                        if coord_missile[g][1] < coord[k][1]+197:
                                            score_joueur = score_joueur + 100
                                            point = 0
                                            print(score_joueur)
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
                        if (x < coord[k][0] + 110 and x > coord[k][0]) or (x + 90 > coord[k][0] and x + 90 < coord[k][0] + 110):
                            if (y < coord[k][1] + 197 and y > coord[k][0]) or (y + 108 > coord[k][1] and y + 108 < coord[k][1] + 197):
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
                    global vie_vaisseau,menu, score, fenetre_end, police1, police, BGD1,BGD2,imD1,imD2, nm_joueur, score_joueur
                    if vie_vaisseau <= 0:
                        root2.destroy()
                        #Création d'une nouvelle fenetre
                        fenetre_end = Tk()
                        fenetre_end.title("MENU ENDGAME")
                        fenetre_end.configure(bg="white")
                        fenetre_end.geometry("1280x720")

                        #mise en place des zones
                        zone_bouton = Frame(fenetre_end)
                        zone_deco1 = Frame(fenetre_end)
                        zone_deco2 = Frame(fenetre_end)

                        #on définie l'emplacements des zones
                        zone_bouton.grid(row=1,column=2,padx=0,pady=0)
                        zone_deco1.grid(row=1,column=1,padx=0,pady=0)
                        zone_deco2.grid(row=1,column=3,padx=0,pady=0)

                        #mise en place d'image
                        BGD1 = Canvas(zone_deco1, width=500, height=720)
                        imD1 = Image.open("Jeu/images/FOND_COLOR.png")
                        imD1.save(("Jeu/images/fond.gif"))
                        imD1 = PhotoImage(file="Jeu/images/fond.gif")
                        BGD1.create_image(0,0, image=imD1, anchor=NW)
                        BGD1.pack()

                        BGD2 = Canvas(zone_deco2, width=500, height=720)
                        imD2 = Image.open("Jeu/images/FOND_COLOR.png")
                        imD2.save(("Jeu/images/fond.gif"))
                        imD2 = PhotoImage(file="Jeu/images/fond.gif")
                        BGD2.create_image(0,0, image=imD2, anchor=NW)
                        BGD2.pack()
                        
                        #création des boutons
                        bouton_menu = Button(zone_bouton)
                        bouton_score1 = Button(zone_bouton)
                        bouton_quit = Button(zone_bouton)

                        #Mise en place de la police écriture
                        police = tkFont.Font(family='Tw Cen MT Condensed Extra Bold', size= 12, weight='bold')
                        police1 = tkFont.Font(family='Tw Cen MT Condensed Extra Bold', size= 25, weight='bold')

                        #on configure les boutons
                        bouton_menu.configure(text="RETOURNER AU MENU PRINCIPAL",bg="white",fg="black", width="30", height="1", relief=FLAT, font=police)
                        bouton_score1.configure(text="TABLEAUX DES SCORES",bg="white",fg="black", width="30", height="1", relief=FLAT, font=police)
                        bouton_quit.configure(text="QUITTER LE JEU",bg="white",fg="black", width="30", height="1", relief=FLAT, font=police)

                        #on définie l'emplacements des boutons
                        bouton_menu.grid(row=6,column=1)    
                        bouton_score1.grid(row=7,column=1)
                        bouton_quit.grid(row=8,column=1)

                        #zone de saisie du pseudo du joueur
                        
                        nm_joueur = StringVar()
                        entree = Entry(zone_bouton, textvariable=nm_joueur.get(), width="31")
                        entree.configure(bg="white",fg="grey", relief=FLAT, font=police)
                        entree.grid(row=5,column=1)
                        
                        etiquette = Label(zone_bouton, text="ENTREE VOTRE PSEUDO ", font=police, bg="white", fg="black")
                        etiquette.configure(width="30")
                        etiquette.grid(row=4,column=1)

                        etiquette2 = Label(zone_bouton, text="VOUS AVEZ", font=police1, bg="white", fg="red")
                        etiquette2.configure(width="17")
                        etiquette2.grid(row=0,column=1)

                        etiquette2 = Label(zone_bouton, text="MORT", font=police1, bg="white", fg="red")
                        etiquette2.configure(width="17")
                        etiquette2.grid(row=1,column=1)

                        etiquette2 = Label(zone_bouton, text=" ", font=police1, bg="white", fg="red")
                        etiquette2.configure(width="17")
                        etiquette2.grid(row=2,column=1)

                        etiquette2 = Label(zone_bouton, text="SCORE OBTENUE " + str(score_joueur), font=police, bg="white", fg="black")
                        etiquette2.configure(width="30")
                        etiquette2.grid(row=3,column=1)
                        
                        while nm_joueur == "" or len(str(nm_joueur)) >= 12:
                            etiquette.configure(text="ENTREE VOTRE PSEUDO !!")

                            fichier = open("Jeu/score_2.txt", "r")
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
                            fichier = open("Jeu/score_2.txt", "w")
                            fichier.write(chaine)
                            fichier.close()

                            #ouverture du fichier des 12 meilleurs scores
                            fichier = open("Jeu/score_2.txt", "r")
                            score = fichier.read()
                            fichier.close()

                            fichier = open("Jeu/score.txt", "r")
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

                            fichier = open("Jeu/score_3.txt", "w")
                            fichier.write(complet)
                            fichier.close()
                                            
                        def bouton_menue(event):
                            fenetre_end.destroy()
                            menu()

                        def bouton_quitter(event):
                            fenetre_end.destroy()
             
                        bouton_menu.bind("<ButtonPress-1>",bouton_menue)
                        bouton_quit.bind("<ButtonPress-1>",bouton_quitter)
                        bouton_score1.bind("<ButtonPress-1>",score)
                        
                        return nm_joueur

                        fenetre_end.mzainloop()

                    c.after(1000,check_vie)
                
                check_vie()
                root2.mainloop()

            #Association des boutons du menu au différentes fonctions
            bouton_3.bind("<ButtonPress-1>",score)
            bouton_4.bind("<ButtonPress-1>",quitter)
            bouton_2.bind("<ButtonPress-1>",instruction)
            bouton_1.bind("<ButtonPress-1>",jouer)
        
            menu_principal.mainloop()

        menu()
root.bind_all('<Key>', access_menu)

root.mainloop()
