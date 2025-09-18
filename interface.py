import player_123 as pl
import random
import Game_rule as GR

class PlayMM:

    def play_mastermind(self):
        """ Pour jour à MasterMind"""
        length = input("La longueur de la suite à trouver: ('5' pour 5): ")
        if length == '5':
            length = 5
        length = int(length)
        choices = input("Les choix possibles ('8' pour 1 à 8): ")
        if choices == '8':
            choices = [1, 2, 3, 4, 5, 6, 7, 8]
        if choices == 'couleur':
            choices = ['bleu', 'jaune', 'vert', 'orange', 'noir', 'rouge', 'brun', 'rose']
        answer = GR.MasterMind(random.choices(choices, k=length))

        find = 'O'
        while find == 'O':
            essai = []
            for i in range(length):
                ess = input(f"{i+1} de la séquence: ")
                if ess == 'help':
                    jeu = pl.MMsolveur(answer.reponse, choices, length)
                    print(jeu.solve(4), "count:", jeu.count)
                    essai = jeu.solve(4)
                    break
                essai += [int(ess),]
            print(f"L'essai est : {essai}")
            print(answer.tour(essai))
            if answer.essai(essai) == (0, 5):
                print("Bravo! Vous avez réussi")
                find = input("Voulez vous rejouer? (O/N): ")
                if find == 'O':
                    answer = GR.MasterMind(random.choices(choices, k=length))

    def repeat_solve(self):
        """ Résout joue 60 fois"""
        data = {1:0,2:0}
        choices = [1, 2, 3, 4, 5, 6, 7, 8]
        length = 5
        record = [20, 0, 0, 0]
        for j in [1, 2]:
            for i in range(30):
                answer = GR.MasterMind(random.choices(choices, k=length))
                jeu = pl.MMsolveur(answer.reponse, choices, length)
                reponse = jeu.solve(j)
                print("La réponse était: ", reponse, "Nb d'essais: ", jeu.count)
                data[j] += jeu.count
                if jeu.count < record[0]:
                    record[0:1] = [jeu.count, j]
                if jeu.count > record[2]:
                    record[2:3] = [jeu.count, j]

        # Présentation finale
        print("\n----------------------------------")
        print("Approche 1: ", data[1], " tours jouer.")
        print("Approche 2: ", data[2], " tours jouer.")
        print(f"L'approche {record[1]} a eu le nombre de tour le plus bas avec {record[0]} tours.")
        print(f"L'approche {record[3]} a eu le nombre de tour le plus haut avec {record[2]} tours.")
        print("----------------------------------\n")

if __name__ == '__main__':
    PlayMM().repeat_solve()
    play = input("Voulez-vous rejouez ? (O/N): ")
    if play == 'O':
        PlayMM().play_mastermind()
