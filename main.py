import pygame
import math
import random
# intialize the pygame
pygame.init()
# create the screen
screen = pygame.display.set_mode((800,600))#width // height
# adding title and icon
pygame.display.set_caption('Space War')
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)
# background image
Background = pygame.image.load('background.png')
# Player
Playerimg=pygame.image.load('spaceship.png')
PlayerX=370
PlayerY=480
Player_change=0
def PlayerFun(x,y):
	screen.blit(Playerimg,(PlayerX,PlayerY))
# Enemy
Enemyimg=[]
EnemyX=[]
EnemyY=[]
Enemy_changeX=[]
Enemy_changeY=[]
number_enemy=6
for i in range(number_enemy):
	Enemyimg.append(pygame.image.load('targetship.png'))
	EnemyX.append(random.randint(0,800))
	EnemyY.append(random.randint(50,150))
	Enemy_changeX.append(1)
	Enemy_changeY.append(30)
def EnemyFun(x,y,i):
	screen.blit(Enemyimg[i],(EnemyX[i],EnemyY[i]))
# Bullet
Bulletimg=pygame.image.load('bullet.png')
BulletX=0
BulletY=480
Bullet_changeX=0
Bullet_changeY=10
Bullet_state='Ready'
def Fire_Bullet(x,y):
	global Bullet_state
	Bullet_state='Fire'
	screen.blit(Bulletimg,(x+16,y+10))
# Collision Function
def isCollision(BulletX,BulletY,EnemyX,EnemyY):
	distance = math.sqrt(math.pow(EnemyX- BulletX ,2)+math.pow(EnemyY- BulletY ,2))
	if distance<=20:
		return True
	else:
		return False


secore_value=0
# show score
font = pygame.font.Font('freesansbold.ttf',32)
textX=10
textY=10
def showScore(x,y):
	score=font.render("score: "+str(secore_value),True,(255,255,255))
	screen.blit(score,(x,y))
# to stop window fading (Game loop)
running = True
while running:
	#  set color to screen
	screen.fill((0,0,0))
	# Background image
	screen.blit(Background,(0,0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running=False
		# if keystroke is pressed check whether i'ts right of left
		if event.type==pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				Player_change=-3
			if event.key == pygame.K_RIGHT:
				Player_change=3
			if event.key == pygame.K_SPACE:
				if Bullet_state is 'Ready': # to make spaceship shot one time
						BulletX=PlayerX
						Fire_Bullet(BulletX,BulletY)
		if event.type==pygame.KEYUP and event.key == pygame.K_LEFT :
			Player_change=0
		if event.type==pygame.KEYUP and event.key == pygame.K_RIGHT:
			Player_change=0
	# Plyer adding steps
	PlayerX+=Player_change
	# to stop the player at the edge of frame
	if PlayerX<=0:
		PlayerX=0
	elif PlayerX>=736:
		PlayerX=736

	# to stop the Enemy at the edge ofb frame
	for i in range(number_enemy):
		# Enemy adding steps
		EnemyX[i]+=Enemy_changeX[i]
		if EnemyX[i]<=0:
			Enemy_changeX[i]+=1
			EnemyY[i]+=Enemy_changeY[i]
		elif EnemyX[i]>=736:
			Enemy_changeX[i]+=-1
			EnemyY[i]+=Enemy_changeY[i]
		if BulletY <=0:
			BulletY=480
			Bullet_state='Ready'
		# collision
		collision = isCollision(BulletX,BulletY,EnemyX[i],EnemyY[i])
		if collision:
			BulletY=480
			Bullet_state='Ready'
			secore_value+=1
			EnemyX[i]=random.randint(0,736)
			EnemyY[i]=random.randint(50,150)
		EnemyFun(EnemyX[i],EnemyY[i],i)
	# Bullte Movment
	if Bullet_state is 'Fire':
		Fire_Bullet(BulletX,BulletY)
		BulletY-=Bullet_changeY


	showScore(textX,textY)
	PlayerFun(PlayerX,PlayerY)
	# update frame each time
	pygame.display.update()
