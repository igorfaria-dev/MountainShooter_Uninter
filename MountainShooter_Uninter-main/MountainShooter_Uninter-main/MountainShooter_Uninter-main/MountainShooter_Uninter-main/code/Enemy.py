from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY, WIN_HEIGHT
from code.EnemyShot import EnemyShot
from code.Entity import Entity

class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        self.direction_y = 1 

    # Controla o movimento horizontal e o zigue-zague vertical (subida/descida) específico do Enemy3
    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        if self.name == 'Enemy3':
            if self.direction_y == 1:
                self.rect.centery += ENTITY_SPEED[self.name] * 2
            else: 
                self.rect.centery -= ENTITY_SPEED[self.name]
            if self.rect.bottom >= WIN_HEIGHT:
                self.direction_y = -1
            elif self.rect.top <= 0:
                self.direction_y = 1

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))