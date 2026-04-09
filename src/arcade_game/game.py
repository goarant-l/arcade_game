"""
le module principal du projet arcade_game
# 
                  :: ::::: ::
                  :: ::::: ::
                  :: ::::: ::
                  :: ::::: ::
                  :: ::::: ::


                 .:: ::::: ::.
                .::: ::::: :::.
               .:::' ::::: ':::.
              .::::' ::::: '::::.
             .::::'  :::::  '::::.
           .:::::'   :::::   ':::::.
         .::::::'    :::::    '::::::.
    ...:::::::'      :::::      ':::::::...
    :::::::''        :::::        '':::::::
    ::::''           :::::           ''::::

      _______ _______ _______ ______  ___
     |   _   |       |   _   |   _  \|   |(R)
     |.  1   |.|   | |.  1   |.  l   |.  |
     |.  _   `-|.  |-|.  _   |.  _  <|.  |
     |:  |   | |:  | |:  |   |:  |   |:  |
     |::.|:. | |::.| |::.|:. |::.|:. |::.|
     `--- ---' `---' `--- ---`--- ---`---'

"""

import pyxel
from random import randint
from arcade_game.spaceship import Spaceship
from arcade_game.enemy import Enemy
class Game:
    """
    Une classe pour notre jeu
    """
    def __init__(self):
        """
        Initialisation du jeu
        """
        self.w = 128 #largeur de l'écran
        self.h = 256 #hauteur de l'écran
        self.spaceship = Spaceship(self, self.w//2, self.h-8) #instanciation du vaisseau
        self.enemies = []
        pyxel.init(self.w, self.h, title="Arcade Game")
        # chargement des images
        pyxel.load("images.pyxres")
        # --> appel de la fonction principale
        pyxel.run(self.update, self.draw)

    # =====================================================
    # == UPDATE (30FPS)
    # =====================================================
    def update(self):
        """mise à jour des variables (30 fois par seconde)"""

        # deplacement du vaisseau
        self.spaceship.update()

        for shoot in self.spaceship.shoots:
          shoot.update()
        self.update_shoots()
        if pyxel.frame_count % 30 == 0:
          new_enemy = Enemy(self, randint(0, self.w-8), -10)
          self.enemies.append(new_enemy)
        self.update_enemies()

    def update_shoots(self):
        visible_shoots = []
        for shoot in self.spaceship.shoots:
          if shoot.y > -shoot.h :
            visible_shoots.append(shoot)
        self.spaceship.shoots = visible_shoots

    def update_enemies(self):
      for e in self.enemies:
        e.update()


          



    # =====================================================
    # == DRAW (30FPS)
    # =====================================================
    def draw(self):
        """création et positionnement des objets (30 fois par seconde)"""

        # vide la fenetre 30 fois par seconde
        pyxel.cls(0)

        
        
        for shoot in self.spaceship.shoots:
          shoot.draw()
        self.spaceship.draw()
        for e in self.enemies:
          e.draw()




        
# instanciation de notre classe
Game()