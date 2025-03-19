import pgzrun,random
WIDTH=1200
HEIGHT=800
TITLE="iron man vs doom"
iron_man=Actor("iron_man2")
iron_man.pos=random.randint(50,WIDTH-50),random.randint(50,HEIGHT-50)
doom=Actor("drdoom")
doom.pos=random.randint(50,WIDTH-50),random.randint(50,HEIGHT-50)
score=0
def draw():
    screen.blit("avt",(0,-150))
    iron_man.draw()
    doom.draw()
def update():
    global score
    if keyboard.left:
        iron_man.x-=2

    if keyboard.right:
        iron_man.x+=2

    if keyboard.up:
        iron_man.y-=2

    if keyboard.down:
        iron_man.y+=2
    if iron_man.colliderect(doom):
        score+=10
        doom.pos=random.randint(50,WIDTH-50),random.randint(50,HEIGHT-50)               
pgzrun.go()