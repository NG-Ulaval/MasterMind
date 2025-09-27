import player_123 as pl
import random
import Game_rule as GR
import time
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
        nb_essai = 3
        essai = []
        data = {}
        record_bas = {}
        record_haut = {}
        time_count = {}
        for i in range(nb_essai):
            essai += [1 + i,]
            data[i+1] = 0
            record_bas[i+1] = [20, 0]
            record_haut[i+1] = [0, 0]
            time_count[i+1] = 0


        choices = [1, 2, 3, 4, 5, 6, 7, 8]
        length = 5


        for j in essai:
            time_count[j] = time.time()
            for i in range(30):
                answer = GR.MasterMind(random.choices(choices, k=length))
                jeu = pl.MMsolveur(answer.reponse, choices, length)
                reponse = jeu.solve(j)
                # print("La réponse était: ", reponse, "Nb d'essais: ", jeu.count)
                data[j] += jeu.count
                if jeu.count < record_bas[j][0]:
                    record_bas[j] = [jeu.count, j]
                if jeu.count > record_haut[j][0]:
                    record_haut[j] = [jeu.count, j]
            time_count[j] = round(time.time() - time_count[j], 1)

        # Présentation finale

        print("\n----------------------------------")
        for i in essai:
            print(f"Approche {i} :\n {data[i]} tours jouer")
            print(f" Max : {record_haut[i][0]}\n Min : {record_bas[i][0]}")
            print(f" Time : {time_count[i]}\n")
        # print(f"L'approche {record_bas[1]} a eu le nombre de tour le plus bas avec {record_bas[0]} tours.")
        # print(f"L'approche {record_haut[1]} a eu le nombre de tour le plus haut avec {record_haut[0]} tours.")
        print("----------------------------------\n")
if __name__ == '__main__':
    PlayMM().repeat_solve()
    play = input("Voulez-vous jouez ? (O/N): ")
    if play == 'O':
        PlayMM().play_mastermind()
