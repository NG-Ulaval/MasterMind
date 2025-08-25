"""
MasterMind solver

Maintaineur: Noah Garant
"""
from itertools import product
import Game_rule as GM


class MMsolveur:
    def __init__(self, to_solve, choice, length = 5):
        self.to_solve = GM.MasterMind(to_solve)
        self.choice = choice
        self.length = length
        # Création d'une liste avec toutes les possibilité
        possibility = product(choice, repeat = length)
        self.possibility = []
        for poss in possibility:
            self.possibility += [poss,]
        self.count = 0

    def solve(self, quel_essai = 1):
        """ Résout le puzzle """
        # Résout le problème
        if len(self.possibility) == 1:
            return self.possibility[0]

        # La série essai (1: par placement, 2: par couleur, 3: Par l'inv du placement, 4: par la première
        # Le 1 est plus précis, le 4 est plus rapide
        if len(self.possibility) != 32768:
            if quel_essai == 1:
                essai_x = self.choisir_essai_placem()
            else:
                essai_x = self.possibility[0]
        else:
            essai_1 = [self.choice[0]]
            for i in range(self.length-1):
                essai_1 += [self.choice[i],]
            essai_x = essai_1
        reponse = self.to_solve.essai(essai_x)
        self.tri_possible(essai_x, reponse)
        self.count += 1
        return self.solve(quel_essai)


    def tri_possible(self, essai_x, reponse):
        """Tri les valeurs possibles et change les valeurs possibles selon"""
        possibility = []
        for poss in self.possibility:
            valeur = GM.MasterMind(poss)
            reponse_x = valeur.essai(essai_x)
            if reponse_x == reponse:
                possibility.append(poss)
        self.possibility = possibility


    def choisir_essai_placem(self):
        """ Pondère selon le placement des pièces"""

        # Créé des sources pour garder les biens placer
        choix = {}
        valeur = {}
        for i in range(self.length):
            choix[i] = []
            valeur[i] = {}

        # Ajouter les couleurs sur la ligne
        for poss in self.possibility:
            for i, color in enumerate(poss):
                choix[i] += [color, ]

        # Pondérée les valeurs
        for i, listes in choix.items():
            for poss in self.choice:
                valeur[i][poss] = listes.count(poss)

        for i in range(self.length):
            tot = 0
            for j in valeur[i].keys():
                tot += valeur[i][j]
            for j in valeur[i].keys():
                valeur[i][j] = valeur[i][j] / tot

        # Choisir le plus probable
        plus_poss = [(), 0]
        for poss in self.possibility:
            tot = 0
            for ligne in valeur.values():
                for i in range(self.length):
                    if poss[i] in ligne.keys():
                        tot += ligne[poss[i]]

            if tot > plus_poss[1]:
                plus_poss = [poss, tot]
        if plus_poss[0] == ():
            Exception("Pas de valeur possible")
            return None
        return plus_poss[0]



if __name__ == '__main__':
    la_reponse = [8, 8, 5, 7, 8]
    choices = [1, 2, 3, 4, 5, 6, 7, 8]
    jeu = MMsolveur(to_solve = la_reponse, choice = choices, length = 5)
    ## print(jeu.solve(quel_essai=1), "count:", jeu.count)
    print(jeu.solve(quel_essai=2), "count:", jeu.count)
    ## print(jeu.solve(quel_essai=3), "count:", jeu.count)
    #### print(jeu.solve(quel_essai=4), "count:", jeu.count)









