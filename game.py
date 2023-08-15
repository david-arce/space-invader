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
asset_background = resource_path('assets/images/background.png')
background = pygame.image.load(asset_background)

# cargar icono de ventana
asset_icon = resource_path('assets/images/ufo.png')
icon = pygame.image.load(asset_icon)

# cargar sonido de fondo
asset_sound = resource_path('assets/audios/background_music.mp3')
background_sound = pygame.mixer.music.load(asset_sound)

# cargar imagen del jugador
asset_playerImg = resource_path('assets/images/space-invaders.png')
playerImg = pygame.image.load(asset_playerImg)

# cargar imagen de bala
asset_bulletImg = resource_path('assets/images/bullet.png')
bulletImg = pygame.image.load(asset_bulletImg)

# cargar fuente para texto de game over
asset_overFont = resource_path('assets/fonts/RAVIE.TTF')
over_font = pygame.font.Font(asset_overFont, 60)

# cargar fuente para texto de puntaje
asset_font = resource_path('assets/fonts/comicbd.ttf')
font = pygame.font.Font(asset_font, 32)


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
playerX_change = 0
playerY_change = 0

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
    
    #función para mostrar la puntuación en la pantalla
    def show_score():
        score_value = font.render("SCORE" + str(score), True, (255, 255, 255))
        screen.blit(score_value, (10, 10))
        
    #función para dibujar el jugador en la pantalla
    def player(x, y):
        screen.blit(playerImg, (x, y))
        
    #función para dibujar un enemigo en la pantalla
    def enemy(x, y, i):
        screen.blit(enemyImg[i], (x, y))
        
    #función para disparar la bala
    def fire_bullet(x, y):
        global bullet_state
        
        bullet_state = "fire"
        screen.blit(bulletImg, (x + 16, y + 10))
        
    #función para comprobar si ha habido una colisión entre la bala y el enemigo
    def isCollision(enemyX, enemyY, bulletX, bulletY):
        distance = math.sqrt((math.pow(enemyX - bulletX, 2)) +
                             (math.pow(enemyY - bulletY, 2)))
        
        if distance < 27:
            return True
        else:
            return False
        
    #función para mostrar el texto de game over en pantalla
    def game_over_text():
        over_text = over_font.render("GAME OVER", True, (255, 255, 255))
        text_rect = over_text.get_rect(
            center = (int(screen_width/2), int(screen_height/2)))
        screen.blit(over_text, text_rect)
        
    #función principal del juego
    def gameLoop():
        global score
        global playerX
        global playerX_change
        global bulletX
        global bulletY
        global collision
        global bullet_state
        
        in_game = True
        while in_game:
            #Maneja eventos, actualiza y renderiza el juego
            #limpia la pantalla
            screen.fill((0, 0, 0))
            screen.blit(background, (0, 0))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    in_game = False
                    pygame.quit()
                    sys.exit()
                    
                if event.type == pygame.KEYDOWN:
                    #maneja el movimiento del jugador y el disparo
                    if event.key == pygame.K_LEFT:
                        playerX_change = -5
                        
                    if event.key == pygame.K_RIGHT:
                        playerX_change = 5
                        
                    if event.key == pygame.K_SPACE:
                        if bullet_state == "ready":
                            bulletX = playerX
                            fire_bullet(bulletX, bulletY)
                        
                if event.type == pygame.KEYUP:
                    playerX_change = 0
                        
            #actualizando la posición del jugador
            playerX += playerX_change
                
            if playerX <= 0:
                playerX = 0
            elif playerX >= 736:
                playerX = 736
                    
            #bucle que se ejecuta para cada enemigo
            for i in range(num_of_enemies):
                if enemyY[i] > 440:
                    for j in range(num_of_enemies):
                        enemyY[j] = 2000
                    game_over_text()
                    
                enemyX[i] += enemyX_change[i]
                if enemyX[i] <= 0:
                    enemyX_change[i] = 5
                    enemyY[i] += enemyY_change[i]
                elif enemyX[i] >= 736:
                    enemyX_change[i] = -5
                    enemyY[i] += enemyY_change[i]
                        
                #se comprueba si ha habido una colisión entre un enemigo y una bala
                collison = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
                if collison:
                    bulletY = 454
                    bullet_state = "ready"
                    score += 1
                    enemyX[i] = random.randint(0, 736)
                    enemyY[i] = random.randint(0, 150)
                enemy(enemyX[i], enemyY[i], i)
                    
            if bulletY < 0:
                bulletY = 454
                bullet_state = "ready"
            if bullet_state == "fire":
                fire_bullet(bulletX, bulletY)
                bulletY -= bulletY_change
                
            player(playerX, playerY)
            show_score
            
            pygame.display.update()
            
            clock.tick(120)
                
gameLoop()
                        
                            
    