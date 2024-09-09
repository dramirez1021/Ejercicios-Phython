#proposito: tarea figuras tortuga
# autor: DRM
# Fecha: 3/12/2020
from turtle import Screen, Turtle

pantalla = Screen()  # creamos pantalla
pantalla.setup(600, 600)  # fija el ancho y alto de la ventana
pantalla.screensize(500, 500)
tortuga = Turtle()
tortuga.speed(10)
for x in range (7):
  tortuga.pencolor("purple")
  tortuga.circle(100,60)
  tortuga.left(120)
  tortuga.circle(100,60)
  tortuga.right(240)
  tortuga.left(360/7)
pantalla.exitonclick()


