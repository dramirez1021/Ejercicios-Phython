#proposito: tarea figuras tortuga
# autor: DRM
# Fecha: 10/01/2021

from turtle import Screen, Turtle

pantalla = Screen()  # creamos pantalla
pantalla.setup(600, 600)  # fija el ancho y alto de la ventana
pantalla.screensize(500, 500)
tortuga = Turtle()
tortuga.speed(1)
(tortuga.sety(50))
a=50
b=100
c=50
d=98
for x in range (1,9):
    for i in range (1):
     tortuga.forward(a)
     tortuga.right(90)
     tortuga.forward(b)
     tortuga.right(90)
     tortuga.forward(c)
     tortuga.right(90)
     tortuga.forward(d)
     tortuga.right(90)
    if x == 1:
     a -=2
     b -=4
     c -=4
     d -=4
    else:
     a -= 4
     b -= 4
     c -= 4
     d -= 4


pantalla.exitonclick()


