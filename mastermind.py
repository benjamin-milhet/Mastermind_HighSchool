#mastermind
from tkinter import*
from tkinter import messagebox, simpledialog

from PIL import Image
from tkinter.messagebox import *
import sys
import random

##menu
fen1 = Tk()
fen1.title("Menu")

# creation des differents cadres
zone_55 = Frame(fen1)
zone_55.grid(row=1,rowspan=3,column=1,padx=10,pady=10)

zone_22 = Frame(fen1)
zone_22.grid(row=4,column=1,padx=10,pady=10)

# creation de la zone de dessin du cadre zone_1
canevas = Canvas(zone_55)
canevas.configure(width=500,height=150,bg="white")
canevas.pack()

# image de fond dans la zone de dessin du cadre zone_1
# ouverture de l'image
ima = Image.open("image13.png")
# redimensionnement de l'image
ima = ima.resize((525,300))
# sauvegarde de l'image redimensionnee
ima.save(("image13_redim.png"))
# chargement de l'image dans la zone de dessin
photo1 = PhotoImage(file="image13_redim.png")
canevas.create_image(0, 0, anchor=NW, image=photo1)
canevas.pack()

menubar = Menu(fen1)


#les boutons
bouton_888 = Button(zone_22)
bouton_888.configure(text="JOUER", width="40", height="3")
bouton_888.grid(row=1, column=1)

Nom=[]
def clic_888(event):
    global Nom
    global Fen1

    ok=simpledialog.askstring("Nom","Quelle est ton nom?")
    Nom.append(ok)
    Fichier = open("Nom","a")
    Fichier.write(Nom[0])
    Fichier.write(" ")
    Fichier.close()

    fen1.destroy()
    
bouton_888.bind("<ButtonPress-1>",clic_888)

bouton_777 = Button(zone_22)
bouton_777.configure(text="REGLES", width="40", height="3")
bouton_777.grid(row=2, column=1)

def clic_777(event):
    messagebox.showinfo("REGLES"," Le but du jeu du Mastermind est pour l’ordinateur d’élaborer une combinaison "
                        "difficilement déchiffrable et pour son adversaire, de deviner en un minimum de coup cette "
                        "combinaison.")
bouton_777.bind("<ButtonPress-1>",clic_777)

bouton_666 = Button(zone_22)
bouton_666.configure(text="QUITTER", width="40", height="3")
bouton_666.grid(row=3, column=1)


def clic_666(event): 
    fen1.destroy()
    sys.exit(0)

bouton_666.bind("<ButtonPress-1>",clic_666)
fen1.mainloop()

##jeu
fenetre = Tk()
fenetre.title("Mastermind") 

#le random   
liste_des_couleurs = ["bleu", "rouge", "vert", "jaune", "noir", "blanc", "violet", "orange"]
aq=random.choice(liste_des_couleurs)
zs=random.choice(liste_des_couleurs)
ed=random.choice(liste_des_couleurs)
rf=random.choice(liste_des_couleurs)

combinaison_secrete=[]
combinaison_secrete.append(aq)
while aq==zs :
    zs=random.choice(liste_des_couleurs)
combinaison_secrete.append(zs)
while aq==ed or zs==ed :
    ed=random.choice(liste_des_couleurs)
combinaison_secrete.append(ed)
while aq==rf or zs==rf or ed==rf :
    rf=random.choice(liste_des_couleurs)
combinaison_secrete.append(rf)


def alert():
    showinfo("alerte", "Bravo!")


# creation des differents cadres
zone_1 = Frame(fenetre)
zone_1.grid(row=1,rowspan=3,column=1,padx=10,pady=10)

zone_2 = Frame(fenetre)
zone_2.grid(row=1,column=2,padx=10,pady=10)

# creation de la zone de dessin du cadre zone_1
canevas = Canvas(zone_1)
canevas.configure(width=485,height=450,bg="white")
canevas.pack()

# image de fond dans la zone de dessin du cadre zone_1
# ouverture de l'image
im = Image.open("image4.png")
# redimensionnement de l'image
im = im.resize((550,550))
# sauvegarde de l'image redimensionnee
im.save(("image4_redim.png"))
# chargement de l'image dans la zone de dessin
photo = PhotoImage(file="image4_redim.png")
canevas.create_image(0, 0, anchor=NW, image=photo)
canevas.pack()

menubar = Menu(fenetre)
    

#les boutons
bouton_1 = Button(zone_2)
bouton_1.configure(bg="red", width="3", height="2")
bouton_1.grid(row=3, column=2)

bouton_2 = Button(zone_2)
bouton_2.configure(bg="green", width="3", height="2")
bouton_2.grid(row=4, column=1)

bouton_3 = Button(zone_2)
bouton_3.configure(bg="black", width="3", height="2")
bouton_3.grid(row=3, column=1)

bouton_4 = Button(zone_2)
bouton_4.configure(bg="blue", width="3", height="2")
bouton_4.grid(row=4, column=2)

bouton_5 = Button(zone_2)
bouton_5.configure(bg="orange", width="3", height="2")
bouton_5.grid(row=5, column=1)

bouton_6 = Button(zone_2)
bouton_6.configure(bg="white", width="3", height="2")
bouton_6.grid(row=5, column=2)

bouton_7 = Button(zone_2)
bouton_7.configure(bg="purple", width="3", height="2")
bouton_7.grid(row=6, column=1)

bouton_8 = Button(zone_2)
bouton_8.configure(bg="yellow", width="3", height="2")
bouton_8.grid(row=6, column=2)

bouton_valide = Button(zone_2)
bouton_valide.configure(bg="silver", width="6", height="2", text="valider", fg=("black"))
bouton_valide.grid(row=4, column=3)


#bouton aide
bouton_nul = Button(zone_2)
bouton_nul.configure(bg="silver", width="6", height="2", text="aide", fg=("black"))
bouton_nul.grid(row=3, column=3)
    
#pour quitter
bouton_quitter = Button(zone_2)
bouton_quitter.configure(bg="silver", width="6", height="2", text="quitter", fg=("black"), command=fenetre.destroy)
bouton_quitter.grid(row=6, column=3)

#pour effacer
bouton_rien = Button(zone_2)
bouton_rien.configure(bg="silver", width="6", height="2", text="effacer", fg=("black"))
bouton_rien.grid(row=5, column=3)

x_cercle = 150
y_cercle = 322
def clic_001(event):
    global x_cercle, y_cercle
    global liste_joueur
    if x_cercle > 150:
        x_cercle = x_cercle - 65
        canevas.create_oval(x_cercle-10,y_cercle-10,x_cercle+10,y_cercle+10, fill="white", outline="white")
        del liste_joueur[-1]
    
bouton_rien.bind("<ButtonPress-1>",clic_001)


#pour la première ligne
liste_joueur=[]
nb_pion_bien=0
nb_pion_mal=0

nb_coup=8
#pour le vert
def clic_2(event):
    global x_cercle, y_cercle
    global nb_pion_bien
    global nb_pion_mal
    global nb_coup
    if len(liste_joueur) < (len(combinaison_secrete)):
        canevas.create_oval(x_cercle-10,y_cercle-10,x_cercle+10,y_cercle+10, fill="green", outline="green")
        x_cercle = x_cercle + 65
        liste_joueur.append("vert")
          
    
bouton_2.bind("<ButtonPress-1>",clic_2)


#pour le rouge
def clic_3(event):
    global x_cercle, y_cercle
    global nb_pion_bien
    global nb_pion_mal
    global nb_coup
    if len(liste_joueur) < (len(combinaison_secrete)):
        canevas.create_oval(x_cercle-10,y_cercle-10,x_cercle+10,y_cercle+10, fill="red", outline="red")
        x_cercle = x_cercle + 65
        liste_joueur.append("rouge")
        
    
    
    
bouton_1.bind("<ButtonPress-1>",clic_3)

#pour le noir
def clic_4(event):
    global x_cercle, y_cercle
    global nb_pion_bien
    global nb_pion_mal
    global nb_coup
    if len(liste_joueur) < (len(combinaison_secrete)):
        canevas.create_oval(x_cercle-10,y_cercle-10,x_cercle+10,y_cercle+10, fill="black", outline="black")
        x_cercle = x_cercle + 65
        liste_joueur.append("noir")
        
    
    
    
bouton_3.bind("<ButtonPress-1>",clic_4)

#pour le blanc
def clic_5(event):
    global x_cercle, y_cercle
    global nb_pion_bien
    global nb_pion_mal
    global nb_coup
    if len(liste_joueur) < (len(combinaison_secrete)):
        canevas.create_oval(x_cercle-10,y_cercle-10,x_cercle+10,y_cercle+10, fill="white")
        x_cercle = x_cercle + 65
        liste_joueur.append("blanc")
        
   
    
    
bouton_6.bind("<ButtonPress-1>",clic_5)

#pour le orange
def clic_6(event):
    global x_cercle, y_cercle
    global nb_pion_bien
    global nb_pion_mal
    global nb_coup
    if len(liste_joueur) < (len(combinaison_secrete)):
        canevas.create_oval(x_cercle-10,y_cercle-10,x_cercle+10,y_cercle+10, fill="orange", outline="orange")
        x_cercle = x_cercle + 65
        liste_joueur.append("orange")
        
    
    
    
bouton_5.bind("<ButtonPress-1>",clic_6)

#pour le violet
def clic_7(event):
    global x_cercle, y_cercle
    global nb_pion_bien
    global nb_pion_mal
    global nb_coup
    if len(liste_joueur) < (len(combinaison_secrete)):
        canevas.create_oval(x_cercle-10,y_cercle-10,x_cercle+10,y_cercle+10, fill="purple", outline="purple")
        x_cercle = x_cercle + 65
        liste_joueur.append("violet")
        
   
    
bouton_7.bind("<ButtonPress-1>",clic_7)

#pour le bleu
def clic_8(event):
    global x_cercle, y_cercle
    global nb_pion_bien
    global nb_pion_mal
    global nb_coup
    if len(liste_joueur) < (len(combinaison_secrete)):
        canevas.create_oval(x_cercle-10,y_cercle-10,x_cercle+10,y_cercle+10, fill="blue", outline="blue")
        x_cercle = x_cercle + 65
        liste_joueur.append("bleu")
        
   
    
    
bouton_4.bind("<ButtonPress-1>",clic_8)

#pour le jaune
def clic_9(event):
    global x_cercle, y_cercle
    global nb_pion_bien
    global nb_pion_mal
    global nb_coup
    if len(liste_joueur) < (len(combinaison_secrete)):
        canevas.create_oval(x_cercle-10,y_cercle-10,x_cercle+10,y_cercle+10, fill="yellow", outline="yellow")
        x_cercle = x_cercle + 65
        liste_joueur.append("jaune")
        
   
    
    
bouton_8.bind("<ButtonPress-1>",clic_9)

#pour comparer
k=0
label0=Label(zone_1, text="nombre de coup restant : "+str(nb_coup), fg='green')
def clic_valide(event):
    global liste_joueur
    global nb_pion_bien
    global nb_pion_mal
    global nb_coup
    global k
    global x_cercle, y_cercle
    for k in range (0,4):
        if liste_joueur[k] == combinaison_secrete[k] :
            nb_pion_bien+=1
        elif liste_joueur[k] in combinaison_secrete :
            nb_pion_mal+=1
           
    if liste_joueur==combinaison_secrete :
        fenetre.config(menu=menubar)
        label = Label(zone_1, text="Vous avez gagner !", fg='green')
        label.pack()
        
        global Nom
        Fichier = open("Nom","a")
        Fichier.write(str(9-nb_coup))
        Fichier.write("\n")
        Fichier.close()
        
        fenetre.destroy()

        
        fen2=Tk()
        fen2.title('Bravo')

        zone_bravo = Frame(fen2)
        zone_bravo.grid(row=1,rowspan=3,column=1,padx=10,pady=10)

        # creation de la zone de dessin du cadre zone_1
        canevas1 = Canvas(zone_bravo)
        canevas1.configure(width=525,height=100,bg="white")
        canevas1.pack()

        # image de fond dans la zone de dessin du cadre zone_1
        # ouverture de l'image
        ima_bravo2 = Image.open("bravo.png")
        # redimensionnement de l'image
        ima_bravo2 = ima_bravo2.resize((400,70))
        # sauvegarde de l'image redimensionnee
        ima_bravo2.save(("bravo_redim.png"))
        # chargement de l'image dans la zone de dessin
        photo_bravo2 = PhotoImage(file="bravo_redim.png")
        canevas1.create_image(62.5, 25, anchor=NW, image=photo_bravo2)
        canevas1.pack()

        
        
        
        fen2.mainloop()

        
    elif nb_coup==1:
        label = Label(zone_1, text="Vous avez perdu !", fg='green')
        label.pack()

        fenetre.destroy()
        
        fen3=Tk()
        fen3.title('PERDU')

        zone_perdu = Frame(fen3)
        zone_perdu.grid(row=1,rowspan=3,column=1,padx=10,pady=10)

        # creation de la zone de dessin du cadre zone_1
        canevas1 = Canvas(zone_perdu)
        canevas1.configure(width=525,height=300,bg="white")
        canevas1.pack()

        # image de fond dans la zone de dessin du cadre zone_1
        # ouverture de l'image
        ima_perdu = Image.open("bravo1.png")
        # redimensionnement de l'image
        ima_perdu = ima_perdu.resize((525,300))
        # sauvegarde de l'image redimensionnee
        ima_perdu.save(("bravo1_redim.png"))
        # chargement de l'image dans la zone de dessin
        photo_perdu = PhotoImage(file="bravo1_redim.png")
        canevas1.create_image(0, 0, anchor=NW, image=photo_perdu)
        canevas1.pack()

        fen3.mainloop()
        
    else :
        global label0
        global label1
        global label2
        nb_coup-=1
        fenetre.config(menu=menubar)
        label0.destroy()
        label0 = Label(zone_1, text="nombre de coup restant : "+str(nb_coup), fg='green')
        label0.pack()
        label4 = Label(zone_1, text="pion bien placé : "+str(nb_pion_bien), fg='green')
        label4 = canevas.create_window(x_cercle-350,y_cercle,window=label4)
        label5 = Label(zone_1, text="pion mal placé : "+str(nb_pion_mal), fg='red')
        label5 = canevas.create_window(x_cercle+20,y_cercle,window=label5)
    nb_pion_bien=0
    nb_pion_mal=0
    y_cercle-=25
    x_cercle-=260
    del(liste_joueur[0])
    del(liste_joueur[0])
    del(liste_joueur[0])
    del(liste_joueur[0])
bouton_valide.bind("<ButtonPress-1>", clic_valide)

#bouton aide
def clic_002(event):
    global liste_joueur
    label4 = Label(zone_1, text="AIDE : "+str(combinaison_secrete), fg='green')
    label4.pack()

bouton_nul.bind("<ButtonPress-1>",clic_002)



fenetre.mainloop()


