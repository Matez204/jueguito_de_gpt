import pygame
import sys

# Inicializar pygame
pygame.init()

# Definir colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Definir dimensiones de la pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Definir la velocidad de movimiento del círculo
SPEED = 5

# Crear la ventana
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mover círculo")

# Definir el círculo
circle_radius = 8
circle_x = SCREEN_WIDTH // 2
circle_y = SCREEN_HEIGHT // 2

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Obtener las teclas presionadas
    keys = pygame.key.get_pressed()

    # Mover el círculo según las teclas presionadas
    if keys[pygame.K_LEFT]:
        circle_x -= SPEED
    if keys[pygame.K_RIGHT]:
        circle_x += SPEED
    if keys[pygame.K_UP]:
        circle_y -= SPEED
    if keys[pygame.K_DOWN]:
        circle_y += SPEED

    # Verificar si el círculo sale de la pantalla y hacerlo volver por el lado contrario
    if circle_x - circle_radius > SCREEN_WIDTH:
        circle_x = -circle_radius
    elif circle_x + circle_radius < 0:
        circle_x = SCREEN_WIDTH + circle_radius
    if circle_y - circle_radius > SCREEN_HEIGHT:
        circle_y = -circle_radius
    elif circle_y + circle_radius < 0:
        circle_y = SCREEN_HEIGHT + circle_radius

    # Limpiar la pantalla
    screen.fill(BLACK)

    # Dibujar el círculo en la nueva posición
    pygame.draw.circle(screen, WHITE, (circle_x, circle_y), circle_radius)

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad de la animación
    pygame.time.Clock().tick(1000)

# Salir de pygame
pygame.quit()
sys.exit()