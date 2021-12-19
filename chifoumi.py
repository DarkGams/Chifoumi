from random import *

print("""\n ██████╗██╗  ██╗██╗███████╗ ██████╗ ██╗   ██╗███╗   ███╗██╗
██╔════╝██║  ██║██║██╔════╝██╔═══██╗██║   ██║████╗ ████║██║
██║     ███████║██║█████╗  ██║   ██║██║   ██║██╔████╔██║██║
██║     ██╔══██║██║██╔══╝  ██║   ██║██║   ██║██║╚██╔╝██║██║
╚██████╗██║  ██║██║██║     ╚██████╔╝╚██████╔╝██║ ╚═╝ ██║██║
 ╚═════╝╚═╝  ╚═╝╚═╝╚═╝      ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝
                                                  By Gam's\n""")

def game():

    print("Vous jouez a chifoumi contre l'ordi , il peut choisir 3 options , les voici :\n\n1-Pierre\n2-Feuille\n3-Ciseaux\n")

    choix_joueur = input('Pierre (p), Feuille (f) ou Ciseaux (c) ?')
    choix_pc = randint(1, 3)

    if choix_pc == 1:
        choix_pc == "Pierre"

    elif choix_pc == 2:
        choix_pc == "Feuille"

    elif choix_pc == 3:
        choix_pc == "Ciseaux"

    if choix_joueur == 'p':
        print("Vous avez choisi Pierre.")
        print("L'ordinateur a choisi", choix_pc)

    elif choix_joueur == 'f':
        print("Vous avez choisi Feuille.")
        print("L'ordinateur a choisi", choix_pc)

    elif choix_joueur == 'c':
        print("Vous avez choisi Ciseaux.")
        print("L'ordinateur a choisi", choix_pc)

    if (choix_joueur == 'p' and choix_pc == 3) or (choix_joueur == 'f' and choix_pc == 1) or (choix_joueur == 'c' and choix_pc == 2):
        print("Vous gagnez !")

    elif (choix_joueur == 'p' and choix_pc == 2) or (choix_joueur == 'f' and choix_pc == 3) or (choix_joueur == 'c' and choix_pc == 1):
        print("L'ordinateur gagne !")

    elif (choix_joueur == 'p' and choix_pc == 1) or (choix_joueur == 'f' and choix_pc == 2) or (choix_joueur == 'c' and choix_pc == 3):
        print("Egalité !")


    retry = input("\nVoulez vous rejouer ? O/N")

    if retry == 'o':
        game()
    else:
        exit()

start = input("Appuyez sur une touche pour commencer")

if start =='':
    game()
