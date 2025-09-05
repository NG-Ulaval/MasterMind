import player_123 as pl
import random
import Game_rule as GR
class PlayMM:
    def __init__(self):
        self.record = [20, 0]

    def play_mastermind(self):
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
        for j in [1, 2]:
            for i in range(30):
                answer = GR.MasterMind(random.choices(choices, k=length))
                jeu = pl.MMsolveur(answer.reponse, choices, length)
                reponse = jeu.solve(j)
                # print("La réponse était: ", reponse, "Nb d'essais: ", jeu.count)
                data[j] += jeu.count
                if jeu.count < self.record[0]:
                    self.record = [jeu.count, j]
        print("Approche 1: ", data[1], " tour jouer.")
        print("Approche 2: ", data[2], " tour jouer.")
        print(f"L'approche {self.record[1]} a eu le tour le plus bas avec {self.record[1]} tours.")





if __name__ == '__main__':
    PlayMM().repeat_solve()
