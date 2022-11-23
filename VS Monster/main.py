# import library
import pygame
import math
import random

# setup & prepare 
pygame.init()

####################### DISPLAY ##################################

width = 1000
height = 800
FPS = 120 

# resolution
screen = pygame.display.set_mode((width,height))

# timer
clock = pygame.time.Clock() # manage time (clock)

# icon game
icon = pygame.image.load('fire.png')
pygame.display.set_icon(icon)

# window name
pygame.display.set_caption("VS Monsters!")

# background
background = pygame.image.load('forest.png')

# increase size of bg 2x
background = pygame.transform.scale2x(background) 








#################### CHARACTER : MAGICIAN ########################

magicianImg = pygame.image.load('witch.png')

# position set & size (magician)

Magician_size = 128 # size of magician
Magician_posx = 100 # position (x) at start
Magician_posy = height - Magician_size # position (y) start
Magician_poschange = 0

def Magician(x,y):
    screen.blit(magicianImg,(x,y)) # place img into screen



    







#################### CHARACTER : MONSTER ##########################

enemyImg = pygame.image.load('monster2.png')

# position set & size (enemy)

Enemy_size = 64 # size of enemy 64px
Enemy_posx = 50
Enemy_posy = 0
Enemy_poschange = 1 # speed monster

def Enemy(x,y):
    screen.blit(enemyImg,(x,y))





    



############################# POWER @@@#############################
    
powerImg = pygame.image.load('magic.png')

Magic_size = 32 # size of power 64px
Magic_posx = 100
Magic_posy = height - Magician_size # shoot by magician
Magic_poschange = 20
Magic_state = 'ready'

def Firing(x,y):
    global Magic_state
    Magic_state = 'fire'
    screen.blit(powerImg,(x,y))




######################## COLLISION ############################## 
    
def collision(enemyX,enemyY,magicX,magicY):
    distance = math.sqrt(math.pow(enemyX-magicX,2)+math.pow(enemyY-magicY,2)) # ระยะห่างระหว่างจุดสองจุด
    print(f"Distance : {distance}")

    # check ว่าชนกันไหมถ้าชน return True
    # ถ้าระยะห่างน้อยกว่า 48 แสดงว่าชนกัน
    if distance < 48:
        return True
    else:
        return False
    





 





############################### SCORE ###########################
    
Total_score = 0
font = pygame.font.Font('angsana.ttc',50)

def showcore():
    score = font.render('คะแนน: {} '.format(Total_score),True,(255,255,255))
    screen.blit(score,(30,30))










############################# SOUND #############################
    
# backgroud music
pygame.mixer.music.load('backgroundmusic.wav')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1) # -1 เพื่อให้มันเล่นได้ตลอด

# sound at shart
sound = pygame.mixer.Sound('monstersound.wav')
sound.play()











####################### GAME LOOP ################################

running = True # run program

# run program
while running:

    # tic toc timeeee~
    clock.tick(FPS)





    # check event that occur while running
    for event in pygame.event.get():

        # close game when [x]
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                 Magician_poschange = -10
            if event.key == pygame.K_RIGHT:
                Magician_poschange = 10

            if event.key == pygame.K_SPACE:
                if Magic_state == 'ready':
                    Magic_posx = Magician_posx 
                    Firing(Magic_posx,Magic_posy)
                    sound = pygame.mixer.Sound('magicsound.wav')
                    pygame.mixer.Sound.set_volume(sound,0.2)
                    sound.play()        

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                Magician_poschange = 0





    # run magician
    Magician(Magician_posx,Magician_posy)

    

    
    # move section

    if Magician_posx <= 0:
        Magician_posx = 0
        Magician_posx += Magician_poschange

    elif Magician_posx >= width - Magician_size:
        Magician_posx = width - Magician_size
        Magician_posx += Magician_poschange

    else:
        Magician_posx += Magician_poschange

        




    # run enemy
        Enemy(Enemy_posx,Enemy_posy)
        Enemy_posy += Enemy_poschange



    

    # firing power
    if Magic_state == 'fire':
        Firing(Magic_posx,Magic_posy)
        Magic_posy -= Magic_poschange





    # check ว่าเวทวิ่งไปชนขอบบนยัง ถ้าชนแล้วก็รีให้มันมาอยู่ที่เดิมก่อนยิง
    if Magic_posy <= 0:
        Magic_posy = height - Magician_size



        Magic_state = 'ready'

    # check collision
    # ถ้าชนให้รีกลับมาเป็นโหมดพร้อมยิง!!
        




            
    checkCollision = collision(Enemy_posx,Enemy_posy,Magic_posx,Magic_posy)
    print(checkCollision)
    if checkCollision == True:
        Magic_posy = height - Magician_size
        Magic_state = 'ready'

        # รีให้มันล่วงมาใหม่
        Enemy_posy = 0
        # สุ่มตำแหน่งแกน x ที่มันจะร่วงลงมา
        Enemy_posx = random.randint(50,width-Enemy_size)

        Total_score += 1

        sound = pygame.mixer.Sound('monsterdead.wav')
        pygame.mixer.Sound.set_volume(sound,0.2)
        sound.play()        

        


    
    showcore()

    # update
    pygame.display.update()

    # place bg onto screen           
    screen.blit(background,(0,0)) 

