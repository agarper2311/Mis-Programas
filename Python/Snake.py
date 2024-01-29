import pygame
import random

# Inicializar Pygame
pygame.init()

# Definir colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)

# Definir dimensiones de la pantalla
ANCHO_PANTALLA = 800
ALTO_PANTALLA = 600

# Definir tamaño de bloque y velocidad de serpiente
TAMANO_BLOQUE = 10
VEL_SERPIENTE = 10

# Crear ventana de juego
pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("Juego de la Serpiente")

# Definir reloj y tiempo transcurrido
reloj = pygame.time.Clock()

# Definir fuente y tamaño de texto
fuente = pygame.font.Font(None, 36)

# Función para mostrar puntuación en pantalla
def mostrar_puntuacion(puntuacion):
    texto = fuente.render("Puntuación: " + str(puntuacion), True, BLANCO)
    pantalla.blit(texto, (10, 10))

# Función para mostrar mensaje de fin de juego
def mostrar_mensaje_fin(puntuacion, tiempo):
    texto1 = fuente.render("¡Fin del Juego!", True, ROJO)
    texto2 = fuente.render("Puntuación Final: " + str(puntuacion), True, BLANCO)
    texto3 = fuente.render("Tiempo Total Jugado: " + str(tiempo) + " segundos", True, BLANCO)
    pantalla.blit(texto1, (250, 200))
    pantalla.blit(texto2, (250, 250))
    pantalla.blit(texto3, (250, 300))
    pygame.display.update()

# Función principal del juego
def juego_serpiente():
    # Inicializar posición y dirección de la serpiente
    serpiente = [[100, 50], [90, 50], [80, 50]]
    direccion = "derecha"

    # Inicializar posición y generación de manzana
    manzana = [random.randint(1, (ANCHO_PANTALLA // TAMANO_BLOQUE)-1) * TAMANO_BLOQUE,
               random.randint(1, (ALTO_PANTALLA // TAMANO_BLOQUE)-1) * TAMANO_BLOQUE]

    # Inicializar puntuación
    puntuacion = 0

    # Inicializar fin del juego
    fin_juego = False

    while not fin_juego:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin_juego = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direccion != "abajo":
                    direccion = "arriba"
                elif event.key == pygame.K_DOWN and direccion != "arriba":
                    direccion = "abajo"
                elif event.key == pygame.K_LEFT and direccion != "derecha":
                    direccion = "izquierda"
                elif event.key == pygame.K_RIGHT and direccion != "izquierda":
                    direccion = "derecha"

        # Mover serpiente
        if direccion == "arriba":
            serpiente[0][1] -= VEL_SERPIENTE
        elif direccion == "abajo":
            serpiente[0][1] += VEL_SERPIENTE
        elif direccion == "izquierda":
            serpiente[0][0] -= VEL_SERPIENTE
        elif direccion == "derecha":
            serpiente[0][0] += VEL_SERPIENTE

        # Colisiones con el borde de la pantalla
        if (serpiente[0][0] >= ANCHO_PANTALLA or serpiente[0][0] < 0 or
                serpiente[0][1] >= ALTO_PANTALLA or serpiente[0][1] < 0):
            fin_juego = True

        # Colisiones con el cuerpo de la serpiente
        for segmento in serpiente[1:]:
            if segmento == serpiente[0]:
                fin_juego = True

        # Colisiones con la manzana
        if serpiente[0] == manzana:
            puntuacion += 1
            serpiente.append([])
            manzana = [random.randint(1, (ANCHO_PANTALLA // TAMANO_BLOQUE)-1) * TAMANO_BLOQUE,
                       random.randint(1, (ALTO_PANTALLA // TAMANO_BLOQUE)-1) * TAMANO_BLOQUE]

        # Actualizar posición del cuerpo de la serpiente
        for i in range(len(serpiente)-1, 0, -1):
            serpiente[i] = list(serpiente[i-1])

        # Mostrar elementos del juego en pantalla
        pantalla.fill(NEGRO)
        for segmento in serpiente:
            pygame.draw.rect(pantalla, VERDE, (segmento[0], segmento[1], TAMANO_BLOQUE, TAMANO_BLOQUE))
        pygame.draw.rect(pantalla, ROJO, (manzana[0], manzana[1], TAMANO_BLOQUE, TAMANO_BLOQUE))
        mostrar_puntuacion(puntuacion)

        # Actualizar pantalla
        pygame.display.flip()

        # Controlar velocidad del juego
        reloj.tick(20)

    # Mostrar mensaje de fin de juego
    mostrar_mensaje_fin(puntuacion, int(tiempo_transcurrido/1000))

# Bucle principal del juego
def bucle_principal():
    global pausado
    pausado = False
    terminado = False

    while not terminado:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminado = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pausado = not pausado

        if not pausado:
            tiempo_transcurrido = pygame.time.get_ticks()
            juego_serpiente() 

        pantalla.fill(NEGRO)
        pygame.display.update()
        reloj.tick(20)

    pygame.quit()

# Llamar al bucle principal del juego
bucle_principal()
