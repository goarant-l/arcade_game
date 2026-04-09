import pyxel
class Enemy :
    def __init__(self, game, x, y):
       self.game = game
       self.x = x
       self.y = y
       self.w = 8
       self.h = 8
    # =====================================================
    # == DRAW
    # =====================================================
    def draw(self):
        """
        Dessin d'un ennemi
        """
        pyxel.blt(self.x, self.y, 0, 0, 8, 8, 8)
    # =====================================================
    # == UPDATE
    # =====================================================
    def update(self):
        """Mise à jour de l'ennemi
        """
        self.y += 2