import tkinter as tk
from main import CALC

Calc=CALC()

#FENETRE
window=tk.Tk()
window.title("CALCULATRICE de Elie et Isa")
#window.configure(bg="#483C32")
def recup_calcul():
    entree=TXT_ent.get("1.0","end")
    return entree
    #fonction qui récupère la string dans l'écran

def ecrire_touche(valeur):
    TXT_ent.insert("end",str(valeur))

def calcul():
    nb1=""
    nb2=""
    operateur=""
    entree=recup_calcul().strip()

    for i in range(len(entree)):
        char=entree[i]

        if operateur=="" and char in "0123456789":
            nb1+=char
        elif char in "+-/*" and operateur=="" :
            operateur=char
        elif char in "0123456789" and operateur!="" :
            nb2+=char
        else:
            TXT_ent.delete("1.0", "end")
            TXT_ent.insert("end","Calcul invalide")

    nb1 = int(nb1)
    nb2 = int(nb2)

    if operateur =="+":
        return Calc.addition(nb1,nb2)
    if operateur =="-":
        return Calc.soustraction(nb1,nb2)
    if operateur =="*":
        return Calc.multiplication(nb1,nb2)
    if operateur =="/":
        return Calc.divisionEUC(nb1,nb2)
    else:
        return None


    #gestion des priorités, faire une pile avec l'ordre des choses à faire
    #fonction qui récupère une string et la transforme en chiffre et en opéateur puos exécute le calcul
    #return calcul fait
    pass

def executer_calcul():
    TXT_ent.delete("1.0","end")
    TXT_ent.insert("end",f"{calcul()}")



#Frames
frame_affichage=tk.Frame(window)
frame_affichage.pack(expand=True,fill="both",side="top")

frm_bouton_chf=tk.Frame(window)
frm_bouton_chf.pack(expand=True,fill="both",side="left")

frm_bouton_calcul=tk.Frame(window)
frm_bouton_calcul.pack(expand=True,fill="both",side="right")

TXT_ent=tk.Text(bg="#483C32",
                fg="white",
                height=10,
                width=50,
                master=frame_affichage)


TXT_ent.pack()

chiffres=[(1,0,0),(2,0,1),(3,0,2),
         (4,1,0),(5,1,1),(6,1,2),
         (7,2,0),(8,2,1),(9,2,2)]
for chf,l,c in chiffres:
        bouton=tk.Button(master=frm_bouton_chf, text=f"{chf}", command=lambda val=chf:ecrire_touche(val))
        bouton.grid(row=l,column=c,ipadx=10, ipady=10,
                    padx=0,pady=0,sticky="NSEW")
        #frm_bouton_chf.columnconfigure(c,weight=1)
        #frm_bouton_chf.rowconfigure(l,weight=1)

for l in range(3):
    frm_bouton_chf.rowconfigure(l,weight=1)
    frm_bouton_calcul.rowconfigure(l,weight=1)
for c in range(3):
    frm_bouton_chf.columnconfigure(c,weight=1)
    frm_bouton_calcul.columnconfigure(c, weight=1)

operateur=[("+",0,0),("-",0,1),("*",0,2),
         ("/",1,0),('fibo',1,1),("premier",1,2),
         ("e",2,0),("!",2,1)]
for chf,l,c in operateur:
    bouton=tk.Button(master=frm_bouton_calcul, text=chf,command=lambda val=chf:ecrire_touche(val))
    bouton.grid(row=l,column=c,ipadx=10,ipady=10,sticky="NSEW")

BUT_exe=tk.Button(master=frm_bouton_calcul, text="calculer\n=",command=executer_calcul)
BUT_exe.grid(row=2,column=2,ipadx=10,ipady=10,sticky="NSEW")

window.mainloop()