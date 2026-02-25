import pygame

# Cores
C_ORANGE = (255, 128, 0)
C_YELLOW = (255, 255, 128)
C_WHITE = (255, 255, 255)
C_GREEN = (0, 128, 0)
C_CYAN = (0, 128, 128)

# Eventos
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2

# Velocidades
ENTITY_SPEED = {
    'Level1Bg0': 0, 'Level1Bg1': 1, 'Level1Bg2': 2, 'Level1Bg3': 3, 'Level1Bg4': 4, 'Level1Bg5': 5, 'Level1Bg6': 6,
    'Level2Bg0': 0, 'Level2Bg1': 1, 'Level2Bg2': 2, 'Level2Bg3': 3, 'Level2Bg4': 4,
    
    # Velocidades das camadas de fundo do Level 3 para efeito Parallax
    'Level3Bg0': 0, 'Level3Bg1': 1, 'Level3Bg2': 2, 'Level3Bg3': 3, 'Level3Bg4': 4,
    
    'Player1': 3, 'Player1Shot': 5, 'Player2': 3, 'Player2Shot': 5,
    'Enemy1': 1, 'Enemy1Shot': 5, 'Enemy2': 1, 'Enemy2Shot': 2,
    
    # Velocidade base do Enemy3 e seu tiro
    'Enemy3': 2, 'Enemy3Shot': 4,
}

# Vida
ENTITY_HEALTH = {
    'Level1Bg0': 999, 'Level1Bg1': 999, 'Level1Bg2': 999, 'Level1Bg3': 999, 'Level1Bg4': 999, 'Level1Bg5': 999, 'Level1Bg6': 999,
    'Level2Bg0': 999, 'Level2Bg1': 999, 'Level2Bg2': 999, 'Level2Bg3': 999, 'Level2Bg4': 999,
    
    # Adicionado suporte de vida para o fundo do Level 3
    'Level3Bg0': 999, 'Level3Bg1': 999, 'Level3Bg2': 999, 'Level3Bg3': 999, 'Level3Bg4': 999,
    
    'Player1': 300, 'Player2': 300, 
    'Enemy1': 50, 'Enemy2': 60, 
    
    # HP definido para o novo Enemy3
    'Enemy3': 100,
    
    'Player1Shot': 1, 'Player2Shot': 1, 'Enemy1Shot': 1, 'Enemy2Shot': 1, 'Enemy3Shot': 1,
}

# Dano
ENTITY_DAMAGE = {
    'Level1Bg0': 0, 'Level1Bg1': 0, 'Level1Bg2': 0, 'Level1Bg3': 0, 'Level1Bg4': 0, 'Level1Bg5': 0, 'Level1Bg6': 0,
    'Level2Bg0': 0, 'Level2Bg1': 0, 'Level2Bg2': 0, 'Level2Bg3': 0, 'Level2Bg4': 0,
    'Level3Bg0': 0, 'Level3Bg1': 0, 'Level3Bg2': 0, 'Level3Bg3': 0, 'Level3Bg4': 0,
    'Player1': 1, 'Player2': 1, 'Enemy1': 1, 'Enemy2': 1, 'Enemy3': 1,
    
    # Dano do tiro do Enemy3 definido como 25
    'Player1Shot': 25, 'Player2Shot': 20, 'Enemy1Shot': 20, 'Enemy2Shot': 15, 'Enemy3Shot': 25,
}

# Pontuação
ENTITY_SCORE = {
    'Player1': 0,
    'Player2': 0,
    'Player1Shot': 0,
    'Player2Shot': 0,
    'Enemy1': 100,
    'Enemy2': 125,
    
    # Pontuação atribuída ao derrotar o Enemy3
    'Enemy3': 250,
    
    'Enemy1Shot': 0, 'Enemy2Shot': 0, 'Enemy3Shot': 0,
    'Level1Bg0': 0, 'Level1Bg1': 0, 'Level1Bg2': 0, 'Level1Bg3': 0, 'Level1Bg4': 0, 'Level1Bg5': 0, 'Level1Bg6': 0,
    'Level2Bg0': 0, 'Level2Bg1': 0, 'Level2Bg2': 0, 'Level2Bg3': 0, 'Level2Bg4': 0,
    'Level3Bg0': 0, 'Level3Bg1': 0, 'Level3Bg2': 0, 'Level3Bg3': 0, 'Level3Bg4': 0,
}

ENTITY_SHOT_DELAY = {
    'Player1': 20, 'Player2': 15, 'Enemy1': 100, 'Enemy2': 200, 
    
    # Delay de tiro do novo inimigo
    'Enemy3': 120,
}

# Teclas
PLAYER_KEY_UP = {'Player1': pygame.K_UP, 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN, 'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT, 'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT, 'Player2': pygame.K_d}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_RCTRL, 'Player2': pygame.K_LCTRL}

MENU_OPTION = ('NEW GAME 1P', 'NEW GAME 2P - COOPERATIVE', 'NEW GAME 2P - COMPETITIVE', 'SCORE', 'EXIT')
WIN_WIDTH = 576
WIN_HEIGHT = 324
TIMEOUT_STEP = 100

# Tempo base de fase (será dobrado para 40s no Level 3 via código no Level.py)
TIMEOUT_LEVEL = 20000 

SPAWN_TIME = 4000

SCORE_POS = {
    'Title': (WIN_WIDTH / 2, 50), 'EnterName': (WIN_WIDTH / 2, 80), 'Label': (WIN_WIDTH / 2, 90), 'Name': (WIN_WIDTH / 2, 110),
    0: (WIN_WIDTH / 2, 110), 1: (WIN_WIDTH / 2, 130), 2: (WIN_WIDTH / 2, 150), 3: (WIN_WIDTH / 2, 170), 4: (WIN_WIDTH / 2, 190),
    5: (WIN_WIDTH / 2, 210), 6: (WIN_WIDTH / 2, 230), 7: (WIN_WIDTH / 2, 250), 8: (WIN_WIDTH / 2, 270), 9: (WIN_WIDTH / 2, 290),
}