import random
from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Enemy import Enemy
from code.Player import Player

class EntityFactory:
    @staticmethod
    def get_entity(name: str):
        match name:
            case 'Level1Bg':
                return [Background(f'Level1Bg{i}', (x*WIN_WIDTH, 0)) for i in range(7) for x in range(2)]
            case 'Level2Bg':
                return [Background(f'Level2Bg{i}', (x*WIN_WIDTH, 0)) for i in range(5) for x in range(2)]
            case 'Level3Bg': 
                return [Background(f'Level3Bg{i}', (x*WIN_WIDTH, 0)) for i in range(5) for x in range(2)]
            case 'Player1': return Player('Player1', (10, WIN_HEIGHT/2 - 30))
            case 'Player2': return Player('Player2', (10, WIN_HEIGHT/2 + 30))
            case 'Enemy1': return Enemy('Enemy1', (WIN_WIDTH+10, random.randint(40, WIN_HEIGHT-40)))
            case 'Enemy2': return Enemy('Enemy2', (WIN_WIDTH+10, random.randint(40, WIN_HEIGHT-40)))
            
            # Instancia o Enemy3 em uma posição vertical aleatória para iniciar seu padrão de zigue-zague
            case 'Enemy3': return Enemy('Enemy3', (WIN_WIDTH+10, random.randint(40, WIN_HEIGHT-40)))