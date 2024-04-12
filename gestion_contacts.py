# -*- coding: latin-1 -*-


import os
import time

###VARIABLES GLOBALES###
dictionnaire_contacts = {}



def SeeContacts1():
    print(30*'*')
    for nom, numero in dictionnaire_contacts.items():
        print(f"{nom} ==> {numero}")
        time.sleep(0.2)
    print(30*'*')
    input("Appuyez sur une touche pour retourner au menu...")
    menu()

def AddContact2():
    nom, numero = input("Nom du nouveau contact : ").capitalize(), input("Num�ro de t�l�phone du nouveau contact : ")
    alreadyRegistered = False
    #V�rifie si le num�ro de t�l�phone est d�j� attribu� dans le r�pertoire
    for num in dictionnaire_contacts.values():
        if numero == num:
            alreadyRegistered = True
            break

    if not alreadyRegistered:
        dictionnaire_contacts[nom] = numero
        print(f"[*]Contact {nom} ajout� avec succ�s ![*]")
    else:
        print(f"[!]Num�ro {num} d�j� utilis�, impossible de l'utiliser pour deux contacts.\nRequ�te annul�e.[!]")
    
    input("Appuyez sur une touche pour retourner au menu...")
    menu()
        
            

def DelContact3():
    for contact in dictionnaire_contacts.keys():
        print(f"- {contact}")
    
    choix_suppression_contact = input("Entrez le nom du contact � supprimer : ").capitalize()
    if choix_suppression_contact not in dictionnaire_contacts:
        print(f"[!]Le contact {choix_suppression_contact} n'a pas �t� trouv�\nRequ�te annul�e.[!]")
    
    else:
        del dictionnaire_contacts[choix_suppression_contact]
        print(f"[*]Contact {choix_suppression_contact} supprim� avec succ�s ![*]")

    input("Appuyez sur une touche pour retourner au menu...")
    menu()

def EditContact4():
    for nom, numero in dictionnaire_contacts.items():
        print(f"{nom} ==> {numero}")

    edit_num = input("0 - Modifier un nom\n1 - Modifier un num�ro\nVotre choix (O ou 1) : ")
    
    if edit_num == '0':
        nom_edit = input("Entrez le nom actuel du contact dont vous souhaitez modifier le nom : ").capitalize()
        if nom_edit not in dictionnaire_contacts.keys():
            print(f"[!]Contact {nom_edit} non-reconnu\nRequ�te annul�e.[!]")
        else:
            stock_num = dictionnaire_contacts[nom_edit]
            del dictionnaire_contacts[nom_edit]
            dictionnaire_contacts[input("Entrez le nouveau nom du contact : ").capitalize()] = stock_num
            print(f"[*]Ancien nom du contact {nom_edit} modifi� avec succ�s ![*]")
            
    elif edit_num == '1':
        nom_edit = input("Entrez le nom du contact dont vous souhaitez modifier le num�ro : ").capitalize()
        if nom_edit not in dictionnaire_contacts.keys():
            print(f"[!]Contact {nom_edit} non-reconnu\nRequ�te annul�e.[!]")
        else:
            dictionnaire_contacts[nom_edit] = input(f"Entrez le nouveau num�ro de t�l�phone de {nom_edit} : ")
            print(f"[*]Num�ro de {nom_edit} modifi� avec succ�s ![*]")

    else:
        print("[!]Choix impossible[!]")

    input("Appuyez sur une touche pour retourner au menu...")
    menu()
            
            

def Quit5():
    while True:
        verif = input("Voulez-vous vraiment quitter ? (o/n) : ")
        if verif == "o":
            print("Au revoir !")
            time.sleep(2)
            quit()
        elif verif == 'n':
            menu()

        




def menu():
    os.system("cls")
    print("Menu principal\n1 - Regarder les contacts\n2 - Ajouter un contact\n3 - Supprimer un contact\n4 - Modifier un contact\n5 - Quitter\n"+60*'/')
    choix_menu = input("Votre choix : ")
    
    if choix_menu == '1':
        SeeContacts1()

    elif choix_menu == '2':
        AddContact2()
       
    elif choix_menu == '3':
        DelContact3()

    elif choix_menu == '4':
        EditContact4()

    elif choix_menu == '5':
        Quit5()

    else:
        print("[!]Choisissez un nombre compris dans la liste des choix disponibles[!]")
        time.sleep(2)
        menu()
    

#Ex�cution du programme
menu()