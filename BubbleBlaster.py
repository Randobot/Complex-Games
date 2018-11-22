

#Bubble Blaster Game

from tkinter import *

H = 500
W = 800

window = Tk()
window.title('Bubble Blaster')
c = Canvas( window, width=W,height=H, bg = 'navyblue')
c.pack()
#----------------------------------------------------- Window and Background (UP)

sub= c.create_polygon(5,5,5,25,30,15, outline='red', fill='red')
sub2= c.create_oval(0,0,30,30,outline='red')
subr= 15
MID_X = W/2
MID_Y = H/2
c.move(sub,MID_X,MID_Y)
c.move(sub2,MID_X,MID_Y)
#----------------------------------------------------- Creates the Submarine
speed = 19
def move_ship(event):
    if event.keysym == 'Up':
        c.move(sub, 0,-speed)
        c.move(sub2, 0,-speed)
    elif event.keysym == 'Down':
        c.move(sub, 0,speed)
        c.move(sub2, 0,speed)
    elif event.keysym == 'Right':
        c.move(sub, speed,0)
        c.move(sub2, speed,0)
    elif event.keysym == 'Left':
        c.move(sub, -speed,0)
        c.move(sub2, -speed,0)
c.bind_all('<Key>',move_ship)
#------------------------------------------------------ Controls

from random import randint
bub_id = list()
bub_r = list()
bub_speed = list()
MIN_BUB_R = 10
MAX_BUB_R = 30
MAX_BUB_SPEED = 10
GAP = 10

def create():
    x = W + GAP
    y = randint(0,H)
    r = randint(MIN_BUB_R,MAX_BUB_R)
    id1 = c.create_oval( x - r, y - r, x + r, y + r, outline='white')
    bub_id.append(id1)
    bub_r.append(r)
    bub_speed.append(randint(1, MAX_BUB_SPEED))
#---------------------------------------------------Generates Bubbles

def move():
    for i in range(len(bub_id)):
        c.move(bub_id[i], -bub_speed[i], 0)
#---------------------------------------------------Moves Bubbles (Not Automatically)

def get_coords(id_num):
    pos = c.coords(id_num)
    x = (pos[0]+pos[2])/2
    y = (pos[1]+pos[3])/2
    return x, y
#--------------------------------------------------Finds Bubble Locations

def del_bubble(i):
    del bub_r[i]
    del bub_speed[i]
    c.delete(bub_id[i])
    del bub_id[i]

def clean_up():
    for i in range(len(bub_id)-1, -1, -1):
        x, y = get_coords(bub_id[i])
        if x < -GAP:
            del_bubble(i)
#--------------------------------------------------Clears Bubbles off screen
from math import sqrt
def distance(id1, id2):
    x1, y1 = get_coords(id1)
    x2, y2 = get_coords(id2)
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)
#--------------------------------------------------- a^2+b^2=C^2
'''
o--------
 \      |
  \     |
   \    |
    \   |
     \  |
      \ |
       \|
        o
        '''

def collision():
    points = 0
    for bub in range (len(bub_id) -1, -1, -1):
        if distance(sub2, bub_id[bub]) < (subr + bub_r[bub]):
            points += (bub_r[bub] + bub_speed[bub])
            del_bubble(bub)
    return points
#-------------------------------------------------- BUBBLE COLLITION

c.create_text(50,30, text='TIME',fill='white')
c.create_text(150,30, text='SCORE',fill='white')
time_text =  c.create_text(50,50, fill='white')
score_text = c.create_text( 150,50, fill ='white')
def show_score(score):
    c.itemconfig(score_text, text=str(score))
def show_time(time_left):
    c.itemconfig(time_text, text=str(time_left))

from time import sleep, time
BUB_CHANCE = 10
TIME_LIMIT = 25
BONUS_SCORE = 1000
score = 0
bonus = 0
end = time() + TIME_LIMIT
#------------------------------------------------------Makes Time Limit

    
from time import sleep, time
BUB_CHANCE = 10
score = 0

#MAIN GAME LOOP
while time() < end:
    
    if randint(1,BUB_CHANCE)==1:
        create()
    move()
    clean_up()
    score += collision()
    if (int(score / BONUS_SCORE)) > bonus:
        bonus += 1
        end += TIME_LIMIT
    show_score(score)
    show_time(int(end - time()))
    window.update()
    sleep(0.01)

#--------------------------------------------------Moving bubbles

