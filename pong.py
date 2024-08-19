import turtle
import time
import random
import pygame

# Inicializar pygame y la música
pygame.mixer.init()
pygame.mixer.music.load("5. Python/Proyectos/pong.mp3")  # Reemplaza con tu archivo de música
pygame.mixer.music.play(-1)  # Reproduce en bucle

# Configuración de la ventana
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=1280, height=720)
wn.tracer(0)

# Marcadores
score_a = 0
score_b = 0

# Paleta izquierda
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=6, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-620, 0)

# Paleta derecha
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize(stretch_wid=6, stretch_len=1)
paddle_b.penup()
paddle_b.goto(610, 0)

# Pelota
ball = turtle.Turtle()
ball.speed(1)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)

# Función para inicializar la bola con dirección aleatoria
def initialize_ball():
    ball.goto(0, 0)
    direction = random.choice([(0.2, 0.2), (0.2, -0.2), (-0.2, 0.2), (-0.2, -0.2)])
    ball.dx, ball.dy = direction

initialize_ball()

# Función para mover la paleta izquierda hacia arriba
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 310:
        y += 40
    paddle_a.sety(y)

# Función para mover la paleta izquierda hacia abajo
def paddle_a_down():
    y = paddle_a.ycor()
    if y > -300:
        y -= 40
    paddle_a.sety(y)

# Función para mover la paleta derecha hacia arriba
def paddle_b_up():
    y = paddle_b.ycor()
    if y < 310:
        y += 40
    paddle_b.sety(y)

# Función para mover la paleta derecha hacia abajo
def paddle_b_down():
    y = paddle_b.ycor()
    if y > -300:
        y -= 40
    paddle_b.sety(y)

# Controles del teclado
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Marcador
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 320)
pen.write("Jugador A: 0  Jugador B: 0", align="center", font=("Courier", 24, "bold"))

# Función para actualizar el marcador y pausar el juego
def update_score_and_pause():
    pen.clear()
    pen.write("Jugador A: {}  Jugador B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "bold"))
    wn.update()
    time.sleep(2)
    initialize_ball()



# Bucle principal del juego
start_time = time.time()
while True:
    wn.update()

    # Mover la pelota
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Colisiones con la pared superior e inferior
    if ball.ycor() > 300:
        ball.sety(300)
        ball.dy *= -1
        ball.dx *= 1.1

    if ball.ycor() < -320:
        ball.sety(-320)
        ball.dy *= -1
        ball.dx *= 1.1

    # Colisiones con las paredes izquierda y derecha
    if ball.xcor() > 640:
        score_a += 1
        update_score_and_pause()

    if ball.xcor() < -640:
        score_b += 1
        update_score_and_pause()

    # Colisiones con las paletas
    if (ball.dx > 0) and (620 > ball.xcor() > 610) and (paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(610)
        ball.dx *= -1

    if (ball.dx < 0) and (-630 < ball.xcor() < -620) and (paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-620)
        ball.dx *= -1

    # Incrementar la velocidad de la pelota cada 30 segundos
    elapsed_time = time.time() - start_time
    if elapsed_time > 30:
        ball.dx *= 1.1
        ball.dy *= 1.1
        start_time = time.time()  # Reiniciar el temporizador
