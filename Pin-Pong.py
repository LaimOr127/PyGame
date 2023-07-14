# Игра "Пинг-понг" на Python
import turtle

# создаем окно
window = turtle.Screen()
window.title("Pong Game")
window.bgcolor("black")
window.setup(width=600, height=400)

# создаем ракетки
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-250, 0)

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(250, 0)

# создаем мяч
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2

# переменные для уровней
level = 1
ball_speed = 2

# функции для перемещения ракеток
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# связываем функции с клавишами
window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")

# главный цикл игры
while True:
    window.update()

    # движение мяча
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # проверка столкновения мяча с верхней и нижней стенками
    if ball.ycor() > 190 or ball.ycor() < -190:
        ball.dy *= -1

    # проверка столкновения мяча с ракетками
    if ball.xcor() > 240 and ball.xcor() < 250 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1

    if ball.xcor() < -240 and ball.xcor() > -250 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1

    # проверка достижения конца уровня
    if ball.xcor() > 290:
        ball.goto(0, 0)
        ball.dx *= -1
        level += 1
        ball_speed += 1

    if ball.xcor() < -290:
        ball.goto(0, 0)
        ball.dx *= -1
        level += 1
        ball_speed += 1

    # увеличение скорости мяча с каждым уровнем
    ball.speed(ball_speed)

    # проверка достижения максимального уровня
    if level > 5:
        # добавьте здесь код для завершения игры или перехода на следующий уровень
        pass


#Этот код создает окно, две ракетки и мяч,
# а также связывает функции перемещения ракеток с клавишами.
# В главном цикле игры происходит движение мяча и проверка столкновений с верхней и нижней стенками,
# а также с ракетками. При достижении конца уровня мяч возвращается в центр поля,
# направление его движения меняется, и уровень и скорость увеличиваются.
# Вы можете настроить количество уровней и изменять другие аспекты игры в соответствии с вашими потребностями.
# Для добавления уровней, которые будут усложняться постепенно, можно использовать пример кода,
# который был представлен в предыдущем ответе.