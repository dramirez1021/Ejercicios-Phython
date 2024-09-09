#proposito: tarea figuras tortuga
# autor: DRM
# Fecha: 3/12/2020
from turtle import Screen, Turtle

pantalla = Screen()  # creamos pantalla
pantalla.setup(600, 600)  # fija el ancho y alto de la ventana
pantalla.screensize(500, 500)  # fija el area de dibujo
tortuga = Turtle()  # creamos la tortuga
# tortuga.shape("turtle")
tortuga.speed(10)#velocidad para la tortuga
for x in range(10): # "x" la figura de afuera (decagono)
    for i in range(10): # "i" la figura que se va formando con los decagonos pequeños
        tortuga.pencolor("blue")
        tortuga.forward(50)
        tortuga.left(360/10)
    for i in range(5):
        tortuga.pencolor("red")
        tortuga.forward(100)
        tortuga.left(360/5)

    tortuga.left(360/10)

pantalla.exitonclick()