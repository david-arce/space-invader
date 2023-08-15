import pygame
import random
import math
import sys
import os

pygame.init()

# establecer tamaño de pantalla
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

# funcion para obtener la ruta de los recursos


def resource_path(relative_path):
    try:
        base_path = sys.MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)


# cargar imagen de fondo
asset_background = resource_path('assets\\images\\background.png')
background = pygame.image.load(asset_background)

# cargar icono de ventana
asset_icon = resource_path('assets\\images\\ufo.png')
icon = pygame.image.load(asset_icon)

# cargar sonido de fondo
asset_sound = resource_path('assets\\audios\\background_music.mp3')
background_sound = pygame.mixer.music.load(asset_sound)

# cargar imagen del jugador
asset_playerImg = resource_path('assets\\images\\space-invaders.png')
playerImg = pygame.image.load(asset_playerImg)

# cargar imagen de bala
asset_bulletImg = resource_path('assets\\images\\bullet.png')
bulletImg = pygame.image.load(asset_bulletImg)

# cargar fuente para texto de game over
asset_overFont = resource_path('assets\\fonts\\RAVIE.TTF')
over_font = pygame.font.Font(asset_overFont, 20)

# cargar fuente para texto de puntaje
asset_font = resource_path('assets\\fonts\\comicbd.ttf')
font = pygame.font.Font(asset_font, 20)


# establecer titulo de la ventana del juego
pygame.display.set_caption("Space Invader")

# establecer icono de ventana
pygame.display.set_icon(icon)

# reproducir sonido de fondo en loop
pygame.mixer.music.play(-1)

# crear reloj para controlar la velocidad del juego
clock = pygame.time.Clock()

# posicion inicial del jugador
playerX = 370
playerY = 470
player_change = 0
player_change = 0

# lista para almacenar posiciones de los enemigos
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 10

# se inicializan las variables para guardar las posiciones de los enemigos
for i in range(num_of_enemies):
    #se carga la imagen del enemigo 1
    enemy1 = resource_path('assets\\images\\enemy1.png')
    enemyImg.append(pygame.image.load(enemy1))

    enemy2 = resource_path('assets\\images\\enemy2.png')
    enemyImg.append(pygame.image.load(enemy2))
    
    #se asigna una posición aleatoria en X y Y para el enemigo
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(0, 150))

    #se establece la velocidad de movimiento del enemigo en X y Y
    enemyX_change.append(5)
    enemyY_change.append(20)
    
    #se inicializan las variables para guardar la posición de la bala
    bulletX = 0
    bulletY = 480
    bulletX_change = 0
    bulletY_change = 10
    bullet_state = "ready"
    
    #se inicializa la puntuación en 0
    score = 0
    
    