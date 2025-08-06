import pyxel
import debug
import player
import enemi


class Score:
    def __init__(self):
        '''
        Initialiser les variables nécessaires au calcul des points.
        '''
        self.enemy_type=0
        self._killed_enemies=0
        self._killed_enemies_1 = 0
        self._killed_enemies_2 = 0
        self._killed_enemies_3 = 0
        self._points_killed_enemies_1=10
        self._points_killed_enemies_2=20
        self._points_killed_enemies_3=50
        self._score=0
        self.debug_pos = 256 // 2 - 10

    def update_killed_enemies_count(self):
        '''
        Compter le nombre d'ennemis tuer.
        '''
        self.enemy_type=enemi.choose_enemi()
        if self.enemy_type==1:
            self._killed_enemies_1 += 1
        elif self.enemy_type==2:
            self._killed_enemies_2+=1
        elif self.enemy_type==5: self._killed_enemies_3+=5
    
    def update_score(self):
        '''
        Calculer le score.
        '''
        self.update_killed_enemies_count()
        self._score = (self._killed_enemies_1*self._points_killed_enemies_1)+(self._killed_enemies_2*self._points_killed_enemies_2)+(self._killed_enemies_3*self._points_killed_enemies_3)
        self._killed_enemies=self._killed_enemies_1+self._killed_enemies_2+ self._points_killed_enemies_3

    def get_score(self):
        return self._score
    
    def draw(self):
        '''
        Afficher le score.
        '''
        pyxel.text(player.player.x - self.debug_pos,
                   player.player.y - self.debug_pos,
                   f"Score : {self._score}",
                   pyxel.COLOR_WHITE)
        if debug.debug_mode == True:
            pyxel.text(player.player.x - self.debug_pos,
                       player.player.y - self.debug_pos + 7,
                       f"Killed enemies: {self._killed_enemies=}", pyxel.COLOR_YELLOW)   
    def reset(self):
        self._score          = 0
        self._killed_enemies_1 = 0
        self._killed_enemies_2 = 0
        self._killed_enemies_3 = 0
        self._killed_enemies=0


score = Score()