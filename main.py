import pygame,math,random

# UNIVERSAL Constants
BLACK = (0,0,0)
GRAY20 = (51,51,51)
WHITE = (255,255,255)
RED = (255,0,0)
SIXTH_PI = 0.523598776

# import classes from other files
from rooms import *
from player import *

# Bullet vars
primaryBulletVel = 15
secondaryBulletVel = 5
bulletDist = (30*math.sqrt(2))/2+(15*math.sqrt(2))/2

#Time control
timeControl = 60



def main():
	# initialize pygame
	pygame.init()

	# create window
	window = pygame.display.set_mode([800,600])
	pygame.display.set_caption("Platformer")

	#create player
	player = Player()
	movingsprites = pygame.sprite.Group()
	movingsprites.add(player)

	bullets = pygame.sprite.Group()

	# create room list
	rooms = []

	room = spawnRoom()
	rooms.append(room)

	room = Room1()
	rooms.append(room)

	room = Room2()
	rooms.append(room)

	current_room_no = 0
	current_room = rooms[current_room_no]

	# create clock
	clock = pygame.time.Clock()

	timeControl = 60

	done = False

	while not done:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True

			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT or event.key == pygame.K_a:
					player.changeSpeed(-5,0)
				if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
					player.changeSpeed(5,0)
				if event.key == pygame.K_UP or event.key == pygame.K_w:
					player.changeSpeed(0,-5)
				if event.key == pygame.K_DOWN or event.key == pygame.K_s:
					player.changeSpeed(0,5)

				# slow time
				if event.key == pygame.K_LSHIFT:
					timeControl = 20

			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_a:
					player.changeSpeed(5,0)
				if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
					player.changeSpeed(-5,0)
				if event.key == pygame.K_UP or event.key == pygame.K_w:
					player.changeSpeed(0,5)
				if event.key == pygame.K_DOWN or event.key == pygame.K_s:
					player.changeSpeed(0,-5)

				# return time to normal
				if event.key == pygame.K_LSHIFT:
					timeControl = 60

			elif event.type == pygame.MOUSEBUTTONDOWN:
				# player shoots primary if left mouse pressed
				if event.button == 1:
					# get mouse position
					mouseX, mouseY = event.pos

					# calculate the angle created by player and mouse
					delta_x = mouseX - player.rect.x
					delta_y = mouseY - player.rect.y
					theta = math.atan2(delta_y,delta_x);

					# calculate polar coordinates for bullet vel
					newBulletVel_x = primaryBulletVel * math.cos(theta)
					newBulletVel_y = primaryBulletVel * math.sin(theta)

					# calculate polar coordinates for starting position
					startingPos_x = bulletDist * math.cos(theta) + player.rect.x
					startingPos_y = bulletDist * math.sin(theta) + player.rect.y

					# create bullet
					bullet = Projectile(startingPos_x+(15/2),startingPos_y+(15/2),newBulletVel_x, newBulletVel_y)
					movingsprites.add(bullet)
					bullets.add(bullet)

				# shoot secondary if right mouse pressed
				elif event.button == 3:
					# get mouse position
					mouseX, mouseY = event.pos

					# calculate the angle created by player and mouse
					delta_x = mouseX - player.rect.x
					delta_y = mouseY - player.rect.y
					theta = math.atan2(delta_y,delta_x);


					for i in range(5):
						#calculate a new angle with scatter
						scatterAngle = theta + random.uniform(-SIXTH_PI,SIXTH_PI)

						# calculate polar coordinates for bullet vel
						newBulletVel_x = secondaryBulletVel * math.cos(scatterAngle)
						newBulletVel_y = secondaryBulletVel * math.sin(scatterAngle)
						# calculate polar coordinates for starting position
						startingPos_x = bulletDist * math.cos(scatterAngle) + player.rect.x
						startingPos_y = bulletDist * math.sin(scatterAngle) + player.rect.y

						# create bullet
						bullet = Projectile(startingPos_x+(15/2),startingPos_y+(15/2),newBulletVel_x, newBulletVel_y)
						movingsprites.add(bullet)
						bullets.add(bullet)


		# player collisions for current room
		player.move(current_room.wall_list)


		# change walls and kill all bullets if going through door
		if player.rect.x < -player.rect.width:
			for bullet in bullets:
				bullet.kill()

			if current_room_no == 0:
				current_room_no = len(rooms)-1
				current_room = rooms[current_room_no]
				player.rect.x = 800-player.rect.width
			else:
				current_room_no -= 1
				current_room = rooms[current_room_no]
				player.rect.x = 800-player.rect.width
		if player.rect.x > 800:
			for bullet in bullets:
				bullet.kill()

			if current_room_no == len(rooms)-1:
				current_room_no = 0
				current_room = rooms[current_room_no]
				player.rect.x = 0
			else:
				current_room_no += 1
				current_room = rooms[current_room_no]
				player.rect.x = 0

		# Bullet Collisions
		for bullet in bullets:
			bullet.move(current_room.wall_list)

		# draw background and sprites, time goes forward
		window.fill(GRAY20)
		movingsprites.draw(window)
		current_room.wall_list.draw(window)
		pygame.display.flip()

		clock.tick(timeControl)

	pygame.quit()

if __name__ == "__main__":
	main()
