import random
import sys
import pygame
from pygame import Surface
from code.Const import (C_WHITE, WIN_HEIGHT, WIN_WIDTH, MENU_OPTION, EVENT_ENEMY, 
                        SPAWN_TIME, C_GREEN, C_CYAN, EVENT_TIMEOUT, TIMEOUT_STEP, TIMEOUT_LEVEL, C_YELLOW)
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player

class Level:
    def __init__(self, window: Surface, name: str, game_mode: str, player_score: list[int]):
        # Duração dobrada no Level 3 
        self.timeout = TIMEOUT_LEVEL * 2 if name == 'Level3' else TIMEOUT_LEVEL
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))
        
        # Jogadores e Score 
        p1 = EntityFactory.get_entity('Player1')
        p1.score = player_score[0]
        self.entity_list.append(p1)
        
        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            p2 = EntityFactory.get_entity('Player2')
            p2.score = player_score[1]
            self.entity_list.append(p2)
            
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)

    def run(self, player_score: list[int]):
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if hasattr(ent, 'shoot'):
                    s = ent.shoot()
                    if s: self.entity_list.append(s)
            
            # FPS, Level e Time (Canto superior esquerdo)
            self.level_text(18, f" {self.name}", C_WHITE, (10, 10)) 
            self.level_text(16, f"FPS: {clock.get_fps():.0f}", C_WHITE, (10, 300))
            self.level_text(18, f" -   TIME: {self.timeout / 1000:.0f}s", C_WHITE, (WIN_WIDTH / 2 - 230, 10))
            
            # Mostrar vida e score de cada Player
            for ent in self.entity_list:
                if isinstance(ent, Player):
                    if ent.name == 'Player1':
                        self.level_text(16, f"Player1 Score: {ent.score} | Heath: {ent.health}", C_GREEN, (10, 30))
                    if ent.name == 'Player2':
                        self.level_text(16, f"Player2 Score: {ent.score} | Heath: {ent.health}", C_CYAN, (10, 50))

            # 3. TRATAR EVENTOS
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit(); sys.exit()
                
                if event.type == EVENT_ENEMY:
                    choice = 'Enemy3' if self.name == 'Level3' else random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))
                
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout <= 0:
                        # Salva o score final para a próxima fase
                        for ent in self.entity_list:
                            if isinstance(ent, Player):
                                idx = 0 if ent.name == 'Player1' else 1
                                player_score[idx] = ent.score
                        return True

            pygame.display.flip()
            EntityMediator.verify_collision(self.entity_list)
            EntityMediator.verify_health(self.entity_list)
            
            # Se todos os jogadores morrerem, volta ao menu
            if not any(isinstance(e, Player) for e in self.entity_list):
                return False

    def level_text(self, size, text, color, pos):
        font = pygame.font.SysFont("Lucida Sans Typewriter", size)
        surf = font.render(text, True, color).convert_alpha()
        self.window.blit(surf, surf.get_rect(left=pos[0], top=pos[1]))