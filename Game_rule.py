"""
Play Master Mind
"""

class MasterMind:
    def __init__(self, reponse):
        self.reponse = reponse

    def essai(self, liste):
        black_piece = 0
        white_piece = 0
        reponse = []
        for color, answer in zip(liste, self.reponse):
            if color == answer:
                black_piece += 1
                reponse += [0,]
            else:
                reponse.append(answer)
        for color in liste:
            if color in reponse:
                white_piece += 1
                reponse.remove(color)
        return white_piece, black_piece

    def tour(self, liste):
        white_piece, black_piece = self.essai(liste)
        return f"white: {white_piece}, black: {black_piece}"

    def play_mastermind(self):
        pass


if __name__ == "__main__":
    la_reponse = [8, 7, 3, 4, 5]
    test_1 = [4, 2, 4, 4, 5]
    test_2 = [6, 7, 1, 5, 4]
    jeu = MasterMind(la_reponse)
    print(jeu.tour(test_1))
    print(jeu.tour(test_2))


