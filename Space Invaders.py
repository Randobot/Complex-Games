import turtle as t
import os
import math
import random
import time
enemyspeed = 3
#------------------Setup

wn = t.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.setup( width = 700, height = 700, startx = None, starty = None)

#------------------------Score
score = 0
scoret = t.Turtle()
scoret.penup()
scoret.hideturtle()

scoret.color("white")
scoret.setpos(250,310)
scoret.write(score)
scoret.setpos(210,310)
scoret.write("Score: ")


#-------------------Border
border_pen = t.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setpos(-300,-300)
border_pen.pendown()
border_pen.pensize(3)

for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()
#---------------------Player

player = t.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setpos(0, -250)
player.setheading(90)
playerspeed = 20

#----------------------Chose numebr of enemies
#------------------------Enemy


x = random.randint(-200,200)
y = random.randint(100, 250)
enemy = t.Turtle()
enemy.color ("lime")
enemy.shape("circle")

enemy.penup()
enemy.speed(0)

enemy.setposition(x, y)



#------------------------Bullet]
bullet = t.Turtle()
bullet.color("cyan")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()
bulletspeed = 10
# define bullet state
bulletstate = "ready"


def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)
    
def fire_bullet():
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        x = player.xcor()
        y = player.ycor()
        bullet.setpos(x,y + 10)
        bullet.showturtle()

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False
    
t.listen()
t.onkey(move_left, "Left")
t.onkey(move_right, "Right")
t.onkey(fire_bullet, "space")

#----------------------------Main game Loop
while True:
    
    
    x = enemy.xcor()
    x += enemyspeed
    enemy.setx(x)

    if enemy.xcor() > 280:
        y = enemy.ycor()
        enemyspeed += 0.5
        y -=30
        enemyspeed *= -1
        enemy.sety(y)

    if enemy.xcor() < -280:
        y = enemy.ycor()
        enemyspeed -= 0.5
        y -=40
        enemyspeed *= -1
        enemy.sety(y)
        

    if isCollision(bullet, enemy):
        bullet.hideturtle()
        bulletstate = "ready"
        bullet.setpos(0, -400)
        enemy.setpos(-200, 250)
        score += 10
        enemyspeed += 1
       

        scoret.clear()
        scoret.penup()
        scoret.hideturtle()
        scoret.color("white")
        scoret.setpos(250,310)
        scoret.write(score)
        scoret.setpos(210,310)
        scoret.write("Score: ")
        


    if isCollision(player,enemy):
        player.hideturtle()
        enemy.hideturtle()
        print("Game Over")
        break
    

    y = bullet.ycor()
    y += bulletspeed
    bullet.sety(y)

    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"










