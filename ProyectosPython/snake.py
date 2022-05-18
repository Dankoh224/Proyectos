import turtle # Importar para crear ventana y objeto.
import time # Importar para que la serpiente avanze lento
import random

posponer = 0.1
listaSegmento = []

# Creación de la ventana. 
ventana = turtle.Screen() # Creación ventana
ventana.title("cAMI") # Título
ventana.bgcolor("black") # Color de fondo backGround
ventana.setup(width=600, height=600) # Dimensión ventana
ventana.tracer(0) # Animaciones más agradables a los ojos

# Creación de la cabeza de la serpiente.
cabeza = turtle.Turtle() # Turtle crea un objeto para mover
cabeza.speed(0) # Velocidad de movimiento
cabeza.shape("square") # Forma del cursos (cuadrado)
cabeza.color("white") # Color de la forma
cabeza.penup() # Quitar rastro
cabeza.goto(0,0) # Posición inicial de Snake en el plano en Turtle
cabeza.direction = "stop" #Comando para dar dirección (en este momento esta detenido)

# Creación de la comida de la serpiente.
manzana = turtle.Turtle() # Turtle crea un objeto para mover
manzana.speed(0) # Velocidad de movimiento
manzana.shape("circle") # Forma del cursor (círculo)
manzana.color("red") # Color de la forma
manzana.penup() # Quitar rastro
manzana.goto(0,100) # Posición inicial del plano en Turtle

# Funciones
def arriba():
    cabeza.direction = "up"
def abajo():
    cabeza.direction = "down"
def izquierda():
    cabeza.direction = "left"
def derecha():
    cabeza.direction = "right"


def mov():
    if cabeza.direction == "up": # Si la dirección de la cabeza es arriba, la siguiente condición hará que cabeza suba 20 pixeles.
        y = cabeza.ycor()
        cabeza.sety(y+20)
    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y-20)
    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x-20)
    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x+20)

ventana.listen()
ventana.onkeypress(arriba,"Up")
ventana.onkeypress(abajo,"Down")
ventana.onkeypress(izquierda,"Left")
ventana.onkeypress(derecha,"Right")

while True:
    ventana.update()

    # Colisiones con los bordes
    if cabeza.xcor() > 275 or cabeza.xcor() < -275 or cabeza.ycor() > 280 or cabeza.ycor() < -275:
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.direction("stop")

    # Esconder los segmentos
    for segmento in listaSegmento:
        segmento.goto(1000,1000)

    # Aparecer comida random despues que Snake se alimente.
    if cabeza.distance(manzana) < 20:
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        manzana.goto(x,y)

        nuevoSegmento = turtle.Turtle() 
        nuevoSegmento.speed(0) 
        nuevoSegmento.shape("square")
        nuevoSegmento.color("grey")
        nuevoSegmento.penup()
        listaSegmento.append(nuevoSegmento)
    
    # Mover el cuerpo de la serpiente.
    totalSegmentos = len(listaSegmento)
    for index in range(totalSegmentos-1,0,-1):
        x = listaSegmento[index-1].xcor()
        y = listaSegmento[index-1].ycor()
        listaSegmento[index].goto(x,y)
    
    if totalSegmentos > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        listaSegmento[0].goto(x,y)

    mov()
    time.sleep(posponer)

