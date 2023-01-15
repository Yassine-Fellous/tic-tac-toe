morpion =["-","-","-",          
          "-","-","-",         
          "-","-","-"]

def grille(inp, joueur):
    if joueur == 1:
        morpion[inp] = "X"
    elif joueur == 2:
        morpion[inp] = "O"
    print("\n", morpion[0], "|", morpion[1], "|", morpion[2], "\n", morpion[3], "|", morpion[4], "|", morpion[5], "\n", morpion[6], "|", morpion[7], "|", morpion[8], "\n")

def joueur():
    k = 0
    joueur1 = 1
    joueur2 = 2
    p1 = input("nom du joueur 1 : ")
    p2 = input("nom du joueur 2 : ")
    inp = input("si vous voulez commencer a jouer tapez sur entrer : ")
    exit = "exit"
    while inp != exit:
        k += 1
        if k % 2 == 0:
          p = "P2 -" + p2
        else:
          p = "P1 -" + p1
        inp = int(input("{} selectionnez une case de 0 a 8 : ".format(p)))
        while inp > 8:
            print("cette case n'existe pas")
            inp = int(input("{} player selectionnez une case de 0 a 8 : ".format(p)))
        while morpion[inp] == "X" or morpion[inp] == "O":
            print("cette case est déja utiliser")
            inp = int(input("{} player selectionnez une case de 0 a 8 : ".format(p)))
        if k % 2 == 0:
          joueur = joueur2
        else:
          joueur = joueur1
        grille(inp, joueur)
        if (morpion[0] == "X" and morpion[1] == "X" and morpion[2] == "X") or (morpion[3] == "X" and morpion[4] == "X" and morpion[5] == "X") or (morpion[6] == "X" and morpion[7] == "X" and morpion[8] == "X") or (morpion[0] == "X" and morpion[3] == "X" and morpion[6] == "X") or (morpion[1] == "X" and morpion[4] == "X" and morpion[7] == "X") or (morpion[2] == "X" and morpion[5] == "X" and morpion[8] == "X") or (morpion[0] == "X" and morpion[4] == "X" and morpion[8] == "X") or (morpion[2] == "X" and morpion[4] == "X" and morpion[6] == "X"):
           print("le joueur {} a gagné!".format(p))
           break
        elif (morpion[0] == "O" and morpion[1] == "O" and morpion[2] == "O") or (morpion[3] == "O" and morpion[4] == "O" and morpion[5] == "O") or (morpion[6] == "O" and morpion[7] == "O" and morpion[8] == "O") or (morpion[0] == "O" and morpion[3] == "O" and morpion[6] == "O") or (morpion[1] == "O" and morpion[4] == "O" and morpion[7] == "O") or (morpion[2] == "O" and morpion[5] == "O" and morpion[8] == "O") or (morpion[0] == "O" and morpion[4] == "O" and morpion[8] == "O") or (morpion[2] == "O" and morpion[4] == "O" and morpion[6] == "O"):
           print("joueur {} a gagné!".format(p))
           break
        elif (morpion[0] != "-" and morpion[1] != "-" and morpion[2] != "-" and morpion[3] != "-" and morpion[4] != "-" and morpion[5] != "-" and morpion[6] != "-" and morpion[7] != "-" and morpion[8] != "-"):
           print("match nul!")
           break
        inp = joueur

joueur()

        
    