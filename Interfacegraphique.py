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
    nb1 = ""
    nb2 = ""
    operateur = ""
    entree = recup_calcul().strip()

    if "fibo" in entree:
        entree.split("fibo")
        nb = entree.split("fibo")[1]
        try:
            nb=int(nb)
        except ValueError:
            TXT_ent.insert("erreur")

        return Calc.fibonacci(nb)
    if "premier" in entree:
        entree.split("premier")
        nb = entree.split("premier")[1]
        try:
            nb=int(nb)
        except ValueError:
            TXT_ent.insert("erreur")

        return Calc.premier(nb)
    if "exp" in entree:
        nb = entree.split("exp")[1]
        try:
            nb = int(nb)
        except ValueError:
            TXT_ent.insert("erreur")

        return Calc.exp(nb)

    for i in range(len(entree)):
        char = entree[i]
        # TXT_ent.insert("end",f"interation {i} / char: {char} /type:{type(char)} /op:{operateur} \n")
        # TXT_ent.insert("end", f'{entree},type:{type(entree)}')

        if operateur == "" and char in "0123456789":
            nb1 += char
            # TXT_ent.insert("end", f'nb1: {nb1} / type:{type(nb1)}')
        elif char in "+-/*" and operateur == "":
            operateur = char
                # TXT_ent.insert("end", f'opérateur: {operateur} / type:{type(operateur)}')
        elif char in "0123456789" and operateur != "":
            nb2 += char
                # TXT_ent.insert("end", f'nb2: {nb2} / type:{type(nb2)}')
        elif char =="!" and operateur=="":
            return Calc.factoriel(int(nb1))
        else:
            TXT_ent.delete("1.0", "end")
            return "Calcul invalide"

        # TXT_ent.insert("end", f'nb1: {nb1} / type:{type(nb1)}')
    if nb1 and nb2 :
        nb1int = int(nb1)
        nb2int = int(nb2)
        # TXT_ent.insert("end", f"{nb1int}, type {type(nb1int)}")
        # TXT_ent.insert("end", f'opérateur: {operateur} / type:{type(operateur)}')

        if operateur == "+":
            # TXT_ent.insert("end","hey")
            # TXT_ent.insert("end",f"{Calc.addition(nb1int,nb2int)}")
            return Calc.addition(nb1int, nb2int)
        if operateur == "-":
            return Calc.soustraction(nb1int, nb2int)
        if operateur == "*":
            return Calc.multiplication(nb1int, nb2int)
        if operateur == "/":
            return Calc.divisionEUC(nb1int, nb2int)
    if operateur == "" :
            return nb1
    else:
        return None


    #gestion des priorités, faire une pile avec l'ordre des choses à faire
    #fonction qui récupère une string et la transforme en chiffre et en opéateur puos exécute le calcul
    #return calcul fait


def executer_calcul():
    calc_exec=calcul()
    TXT_ent.insert("end",f"= {calc_exec}")

def effacer_lettre():
    TXT_ent.delete("insert-1c", "insert")

def effacer_tout():
    TXT_ent.delete("1.0","end")

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

TXT_ent.pack(expand=True,fill="both")

chiffres=[(1,0,0),(2,0,1),(3,0,2),
         (4,1,0),(5,1,1),(6,1,2),
         (7,2,0),(8,2,1),(9,2,2),
        ("",3,0),(0,3,1),("",3,2)]
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

operateur=[("+",0,0),("-",0,1),("*",1,1),
           ("/",1,0),('fibo',0,2),("premier",1,2), ("exp",2,2),("!",2,1),(".",2,0)]
for chf,l,c in operateur:
    bouton=tk.Button(master=frm_bouton_calcul, text=chf,command=lambda val=chf:ecrire_touche(val))
    bouton.grid(row=l,column=c,ipadx=10,ipady=10,sticky="NSEW")

BUT_exe=tk.Button(master=frm_bouton_calcul, text="calculer\n=",command=executer_calcul)
BUT_exe.grid(row=2,column=3,ipadx=10,ipady=10,sticky="NSEW")

BUT_effacer=tk.Button(master=frm_bouton_calcul, text="←",command=effacer_lettre)
BUT_effacer.grid(row=0,column=3,ipadx=10,ipady=10,sticky="NSEW")

BUT_AC = tk.Button(master=frm_bouton_calcul, text="AC",command=effacer_tout)
BUT_AC.grid(row=1,column=3,ipadx=10,ipady=10,sticky="NSEW")


window.mainloop()