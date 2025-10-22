import tkinter as tk
from doctest import master
from tkinter import ttk

#FENETRE
window=tk.Tk()
window.title("CALCULATRICE de Elie et Isa")
#window.configure(bg="#483C32")

#Frames
frame_affichage=tk.Frame(window)
frame_affichage.pack(expand=True,fill="both",side="top")

frm_bouton_chf=tk.Frame(window)
frm_bouton_chf.pack(expand=True,fill="both",side="left")

frm_bouton_calcul=tk.Frame(window)
frm_bouton_calcul.pack(expand=True,fill="both",side="right")

entree=tk.Text(bg="#483C32",
                fg="white",
                height=10,
                width=50,
                master=frame_affichage)


entree.pack()

chiffres=[(1,0,0),(2,0,1),(3,0,2),
         (4,1,0),(5,1,1),(6,1,2),
         (7,2,0),(8,2,1),(9,2,2)]
for chf,l,c in chiffres:
        bouton=tk.Button(master=frm_bouton_chf, text=f"{chf}")
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

calcul=[("+",0,0),("-",0,1),("*",0,2),
         ("/",1,0),('fibo',1,1),("premier",1,2),
         ("e",2,0),("=",2,1),("",2,2)]
for chf,l,c in calcul:
    if chf=="=":
        bouton = tk.Button(master=frm_bouton_calcul, text=chf)
        bouton.grid(row=l, column=c, ipadx=10, ipady=5, sticky="NSEW",columnspan=3)
    else:
        bouton=tk.Button(master=frm_bouton_calcul, text=chf)
        bouton.grid(row=l,column=c,ipadx=10,ipady=5,sticky="NSEW")


window.mainloop()