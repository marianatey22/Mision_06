#Autor: Mariana Teyssier Cervantes
#Espirógrafo con ecuaciones paramétricas


import pygame   # Librería de pygame
import math

# Dimensiones de la pantalla
ANCHO = 640
ALTO = 480
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul


# Estructura básica de un programa que usa pygame para dibujar
def dibujar(r,R,l):
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo

        # Borrar pantalla
        ventana.fill(BLANCO)


        for angulo in range(0,(360*(r//math.gcd(r,R))+1)):
            a = math.radians(angulo)
            k= r/R
            x = int(R*((1-k) * math.cos(a) + l * k * math.cos(a*((1-k)/k))))
            y = int(R*((1-k) * math.sin(a) - l * k * math.sin(a*((1-k)/k))))
            pygame.draw.circle(ventana, ROJO, (ANCHO//2 + x, ALTO//2 - y),1)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    r = int(input("Teclea el valor de r:"))
    R = int(input("Tecles el valor de R:"))
    l = float(input("Teclea el valor de l:"))
    dibujar(r,R,l)


# Llamas a la función principal
main()