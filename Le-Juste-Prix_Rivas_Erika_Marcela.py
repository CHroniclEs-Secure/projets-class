import numpy as np, random
def joueur():  # fonction pour le nom du jouer
    joueur = Nom_d_utilisateur
    return joueur
def listeProduits(): #Fonction pour le choix de produits
    choix_d_article = print("********************************************\n"
                            "*      >>> Liste des produits: <<<         *\n"
                            "* ---------------------------------------- *\n"
                            "* 1 --->>> Produit désinfectant            *\n"  # Prix: entre  1$ et  10$ - random library
                            "* 2 --->>> Boîtes de barres énergisantes   *\n"  # Prix: entre 10$ et  15$ - borne sup exclue
                            "* 3 --->>> Café pur arabica                *\n"  # Prix: entre 20$ et  30$ - borne sup exclue
                            "* 4 --->>> Liquide magique lave-linge      *\n"  # Prix: entre 30$ et  40$ - borne sup exclue
                            "* 5 --->>> Plante aérosol aspire poussière *\n"  # Prix: entre 40$ et 100$ - borne incluse
                            "********************************************\n")
    return choix_d_article
# fonction pour la géneration des prix pour les articles
def choix_1():
    if choix_d_article == 1:
        choix_1 = np.random.randint(1, 10, 1)
        return choix_1
def choix_2():
    if choix_d_article == 2:
        choix_2 = np.random.randint(10, 15, 1)
        return choix_2
def choix_3():
    if choix_d_article == 3:
        choix_3 = np.random.randint(20, 30, 1)
        return choix_3
def choix_4():
    if choix_d_article == 4:
        choix_4 = np.random.randint(30, 40, 1)
        return choix_4
def choix_5():
    if choix_d_article == 5:
        choix_5 = np.random.randint(50, 101, 1)
        return choix_5

Jouer = True
wallet = 0                  #somme d'argent initial dans le game

Nom_d_utilisateur = input("*******************************************\n"
                          "*            B I E N V E N U E            *\n"
                          "*  --- dans le jeu: «Le Juste Prix » ---  *\n"
                          "*  >>>    Saisir le nom du Joueur:    <<<  *\n"
                          "*******************************************\n")
print("*** ヘ( ^o^)ノ＼(^_^ )/! Merci,", joueur(), ". Tu est prêt(e) à jouer!!! ~(˘▾˘~)!!!***\n"
                                               "*** Maintenant, ( ˘▽˘)っ tu dois choisir le numéro sur la liste des articles pour commencer***\n")
while Jouer:

    listeProduits()
    choix_d_article = int(input("          >>> Saisir votre choix (entre 1 et 5): \n"))
    while choix_d_article <= 0 or choix_d_article > 5:
        choix_d_article = int(input("Choix du produit erroné!!!\n"
                                "       ༼ つ ◕_◕ ༽つ>>> saisir à nouveux votre choix:\n"))

    nom = joueur()              #chaine de caractère nom du joeur pour qui soit plus claire
    #max_essais = 5              #max nombre d'essais
    essais = 0                  #initialization du nombre d'essais

    x_1 = 0                      #initialization pour le prix choix_1
    x_2 = 10                     #initialization pour le prix choix_2
    x_3 = 20                     #initialization pour le prix choix_3
    x_4 = 30                     #initialization pour le prix choix_4
    x_5 = 50                     #initialization pour le prix choix_5

    if choix_d_article == 1:
        print("Bonjour " + nom + ", vous avez choisi le produit «Produit désinfectant», le prix est moins de 10$, devinez le prix!:")
        random.seed(0)          #pourque le prix ne change pas une fois choisi
        prix_1 = choix_1()      #pourque le prix choisit par random soit mit dans une variable et ne change pas au bout des essaies
        print(prix_1)
        while x_1 != prix_1 and essais <= 5:
            x_1 = int(input("$"))
            essais = essais + 1
            if x_1 > 10:
                print("Désolé, (∵) vous n'avez pas respecté l'intervalle de prix accepté.")
            elif x_1 < prix_1:
                print("Plus!!!|")
            elif x_1 > prix_1:
                print("Moins!!!")

        if x_1 == prix_1:
            wallet = wallet + 100
            print("Bravo!!! └(^o^ )Ｘ( ^o^)┘ " + nom + ", vous avez gagné", wallet,"$ au bout de", essais, "essai(s)\n")
        else:
            print("Désolé, ε(*´･ω･)з vous avez utilisé vos", 5,"Vous avez gagné 0$")
            print("Le bon prix est", prix_1,".\n\n\n")

        continuer = str(input("Voulez-vous continuer? (n)on ou (N)on pour quitter:\n"))
        if continuer not in ('n', 'N', 'non', 'NON'):
            Jouer = True
            continue
        else:
            Jouer = False

            print("Gain total =", wallet)               #Wallet designe le montant gagné pendant le jeu
            if (wallet > 100):
                print("(づ｡◕‿‿◕｡)づ Bravo champion")
            elif (wallet) :
                print("Très bien,(. ❛ ᴗ ❛.) à votre place, j'aurai continué")
            else:
                print("Dommage, une autre fois¯\_(ツ)")

    if choix_d_article == 2:
        print("Bonjour " + nom + ", vous avez choisi le produit «Boîtes de barres énergisantes», le prix est entre 10$ et 15$, devinez le prix!:")
        random.seed(0)          #pourque le prix ne change pas une fois choisi
        prix_2 = choix_2()      #pourque le prix choisit par random soit mit dans une variable et ne change pas au bout des essaies
        print(prix_2)
        while x_2 != prix_2 and essais <= 4:
            x_2 = int(input("$"))
            essais = essais + 1
            if x_2 < 9 or x_2 > 15:
                print("Désolé, (∵) vous n'avez pas respecté l'intervalle de prix accepté.")
            elif x_2 < prix_2:
                print("Plus!!!|")
            elif x_2 > prix_2:
                print("Moins!!!")

        if x_2 == prix_2:
            wallet = wallet + 100
            print("Bravo!!! └(^o^ )Ｘ( ^o^)┘ " + nom + ", vous avez gagné", wallet,"$ au bout de", essais, "essai(s)\n")
        else:
            print("Désolé, ε(*´･ω･)з vous avez utilisé vos", 5,"Vous avez gagné 0$")
            print("Le bon prix est", prix_2,".\n\n\n")

        continuer = str(input("Voulez-vous continuer? (n)on ou (N)on pour quitter:\n"))     #Question pour continuer le jeu
        if continuer not in ('n', 'N', 'non', 'NON'):
            Jouer = True
            continue
        else:
            Jouer = False

            print("Gain total =", wallet)               #Wallet designe le montant gagné pendant le jeu
            if (wallet > 100):
                print("(づ｡◕‿‿◕｡)づ Bravo champion")
            elif (wallet) :
                print("Très bien,(. ❛ ᴗ ❛.) à votre place, j'aurai continué")
            else:
                print("Dommage, une autre fois¯\_(ツ)")


    if choix_d_article == 3:
        print("Bonjour " + nom + ", vous avez choisi le produit «Café pur arabica», le prix est entre 20$ et 30$, devinez le prix!:")
        random.seed(0)          #pourque le prix ne change pas une fois choisi
        prix_3 = choix_3()      #pourque le prix choisit par random soit mit dans une variable et ne change pas au bout des essaies
        print(prix_3)
        while x_3 != prix_3 and essais <= 4:
            x_3 = int(input("$"))
            essais = essais + 1
            if x_3 < 19 or x_3 > 30:
                print("Désolé, (∵) vous n'avez pas respecté l'intervalle de prix accepté.")
            elif x_3 < prix_3:
                print("Plus!!!|")
            elif x_3 > prix_3:
                print("Moins!!!")

        if x_3 == prix_3:
            wallet = wallet + 100
            print("Bravo!!! └(^o^ )Ｘ( ^o^)┘ " + nom + ", vous avez gagné", wallet,"$ au bout de", essais, "essai(s)\n")
        else:
            print("Désolé, ε(*´･ω･)з vous avez utilisé vos", 5,"Vous avez gagné 0$")
            print("Le bon prix est", prix_3,".\n\n\n")

        continuer = str(input("Voulez-vous continuer? (n)on ou (N)on pour quitter:\n"))     #Question pour continuer le jeu
        if continuer not in ('n', 'N', 'non', 'NON'):
            Jouer = True
            continue
        else:
            Jouer = False

            print("Gain total =", wallet)               #Wallet designe le montant gagné pendant le jeu
            if (wallet > 100):
                print("(づ｡◕‿‿◕｡)づ Bravo champion")
            elif (wallet) :
                print("Très bien,(. ❛ ᴗ ❛.) à votre place, j'aurai continué")
            else:
                print("Dommage, une autre fois¯\_(ツ)")

    if choix_d_article == 4:
        print("Bonjour " + nom + ", vous avez choisi le produit «Liquide magique lave-linge», le prix est entre 30$ et 40$, devinez le prix!:")
        random.seed(0)          #pourque le prix ne change pas une fois choisi
        prix_4 = choix_4()      #pourque le prix choisit par random soit mit dans une variable et ne change pas au bout des essaies
        print(prix_4)
        while x_4 != prix_4 and essais <= 4:
            x_4 = int(input("$"))
            essais = essais + 1
            if x_4 < 29 or x_4 > 40:
                print("Désolé, (∵) vous n'avez pas respecté l'intervalle de prix accepté.")
            elif x_4 < prix_4:
                print("Plus!!!|")
            elif x_4 > prix_4:
                print("Moins!!!")

        if x_4 == prix_4:
            wallet = wallet + 100
            print("Bravo!!! └(^o^ )Ｘ( ^o^)┘ " + nom + ", vous avez gagné", wallet,"$ au bout de", essais, "essai(s)\n")
        else:
            print("Désolé, ε(*´･ω･)з vous avez utilisé vos", 5,"Vous avez gagné 0$")
            print("Le bon prix est", prix_4,".\n\n\n")


        continuer = str(input("Voulez-vous continuer? (n)on ou (N)on pour quitter:\n"))     #Question pour continuer le jeu
        if continuer not in ('n', 'N', 'non', 'NON'):
            Jouer = True
            continue
        else:
            Jouer = False

            print("Gain total =", wallet)               #Wallet designe le montant gagné pendant le jeu
            if (wallet > 100):
                print("(づ｡◕‿‿◕｡)づ Bravo champion")
            elif (wallet) :
                print("Très bien,(. ❛ ᴗ ❛.) à votre place, j'aurai continué")
            else:
                print("Dommage, une autre fois¯\_(ツ)")


    if choix_d_article == 5:
        print("Bonjour " + nom + ", vous avez choisi le produit «Plante aérosol aspire poussière», le prix est entre 50$ et 100$, devinez le prix!:")
        random.seed(0)          #pourque le prix ne change pas une fois choisi
        prix_5 = choix_5()      #pourque le prix choisit par random soit mit dans une variable et ne change pas au bout des essaies
        print(prix_5)
        while x_5 != prix_5 and essais <= 4:
            x_5 = int(input("$"))
            essais = essais + 1
            if x_5 <= 49 or x_5 >= 101:
                print("Désolé, (∵) vous n'avez pas respecté l'intervalle de prix accepté.")
            elif x_5 < prix_5:
                print("Plus!!!|")
            elif x_5 > prix_5:
                print("Moins!!!")

        if x_5 == prix_5:
            wallet = wallet + 100
            print("Bravo!!! └(^o^ )Ｘ( ^o^)┘ " + nom + ", vous avez gagné", wallet,"$ au bout de", essais, "essai(s)\n")
        else:
            print("Désolé, ε(*´･ω･)з vous avez utilisé vos", 5,"Vous avez gagné 0$")
            print("Le bon prix est", prix_5,".\n\n\n")


        continuer = str(input("Voulez-vous continuer? (n)on ou (N)on pour quitter:\n"))     #Question pour continuer le jeu
        if continuer not in ('n', 'N', 'non', 'NON'):
            Jouer = True
            continue
        else:
            Jouer = False

            print("Gain total =", wallet)               #Wallet designe le montant gagné pendant le jeu
            if (wallet > 100):
                print("(づ｡◕‿‿◕｡)づ Bravo champion")
            elif (wallet) :
                print("Très bien,(. ❛ ᴗ ❛.) à votre place, j'aurai continué")
            else:
                print("Dommage, une autre fois ¯\_(ツ) ")