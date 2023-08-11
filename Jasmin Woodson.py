#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Challenge 5/50
#Kreye yon tab miltiplikasyon kote utilisateur a ap choisi yon vale soti 1 rive 10. Si li choisi yon bon vale, code la ap execute normalement.
#Sinon, mande utilisateur a poul choisi yon bon vale, ki soti na 1 rive nan 10. Une fois li choisi bon vale a epi kod la execute...
#mande sil vle yon lot tab. sil reponn wi, remandel chisi yon vale soti nan 1 rive nan 10. sil choisi non, kod la ap tou kanpe la.

def tab_miltiplikasyon():
    while True:
        try:
            num = int(input("Chwazi yon vale soti nan 1 rive 10 : "))
            if num < 1 or num > 10:
                print(" Chwazi yon vale soti nan 1 rive 10.")
                continue
        except ValueError:
            print("Rantre yon bon vale")
            continue
        
        print(f"Tab miltiplikasyon {num} :")
        for i in range(1, 11):
            print(f"{num} x {i} = {num*i} ")
        
        choice = input("Ou vle yon lot tab ? (W/N) ").strip().lower()
        if choice != "w":
            break

