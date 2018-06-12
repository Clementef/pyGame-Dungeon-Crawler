import pygame,math,random

# Bullet vars
primaryBulletVel = 15
secondaryBulletVel = 5
bulletDist = (30*math.sqrt(2))/2+(15*math.sqrt(2))/2

#Time control
timeControl = 60

# Global Constants
BLACK = (0,0,0)
GRAY20 = (51,51,51)
WHITE = (255,255,255)
RED = (255,0,0)
SIXTH_PI = 0.523598776

class Wall(pygame.sprite.Sprite):
	# constructor function
	def __init__(self,x,y,width,height,color):
		# call parent's constructor
		pygame.sprite.Sprite.__init__(self)

		# make a blue wall using parameters
		self.image = pygame.Surface([width,height])
		self.image.fill(color)

		# set the position of the wall
		self.rect = self.image.get_rect()
		self.rect.y = y
		self.rect.x = x

class Player(pygame.sprite.Sprite):
	# set speed vector
	change_x = 0
	change_y = 0

	# constructor func
	def __init__(self,x,y):

		# call parent's constructor
		pygame.sprite.Sprite.__init__(self)

		# set height, width, set texture
		self.image = pygame.Surface([30,30])
		self.image.fill(WHITE)

		# set pos
		self.rect = self.image.get_rect()
		self.rect.x = x 
		self.rect.y = y

	#change speed
	def changeSpeed(self,x,y):
		self.change_x += x
		self.change_y += y

	#calculate player's new position
	def move(self,walls):

		# horizontal movement
		self.rect.x += self.change_x

		#check for collisions
		block_hit_list = pygame.sprite.spritecollide(self,walls,False)
		for block in block_hit_list:
			# set position if horiz collision
			if self.change_x > 0:
				self.rect.right = block.rect.left
			else:
				self.rect.left = block.rect.right

		# vert movement
		self.rect.y += self.change_y

		# get collisions
		block_hit_list = pygame.sprite.spritecollide(self,walls,False)
		for block in block_hit_list:
			# set position if vert collision
			if self.change_y > 0:
				self.rect.bottom = block.rect.top
			else:
				self.rect.top = block.rect.bottom

class Projectile(pygame.sprite.Sprite):

	vel_x = 0;
	vel_y = 0;

	def __init__(self,x,y,velx,vely):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.Surface([15,15])
		self.image.fill(RED)

		# set pos
		self.rect = self.image.get_rect()
		self.rect.x = x 
		self.rect.y = y
		self.vel_x = velx
		self.vel_y = vely

	#calculate player's new position
	def move(self,walls):

		#change position
		self.rect.x += self.vel_x
		self.rect.y += self.vel_y

		#kill if collides
		if pygame.sprite.spritecollide(self,walls,False):
			self.kill()

class Room():
	#lists of walls & enemies
	wall_list = None
	enemy_sprites = None

	def __init__(self):
		# constructor that creates wall lists
		self.wall_list = pygame.sprite.Group()
		self.enemy_sprites = pygame.sprite.Group()
		base_walls = [	[0, 0, 20, 250, BLACK],
						[0, 350, 20, 250, BLACK],
						[780, 0, 20, 250, BLACK],
						[780, 350, 20, 250, BLACK],
						[20, 0, 760, 20, BLACK],
						[20, 580, 760, 20, BLACK]	]

		for item in base_walls:
			wall = Wall(item[0],item[1],item[2],item[3],item[4])
			self.wall_list.add(wall)

class Room1(Room):
	#creates walls in room1
	def __init__(self):
		Room.__init__(self)

		walls = [	[390, 50, 20, 500, BLACK]	]

		for item in walls:
	 		wall = Wall(item[0],item[1],item[2],item[3],item[4])
	 		self.wall_list.add(wall)

class Room2(Room):
    """This creates all the walls in room 2"""
    def __init__(self):
        super().__init__()
 
        walls = [	[190, 50, 20, 500, BLACK],
	                [590, 50, 20, 500, BLACK]	]
 
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)
 
 
class Room3(Room):
    """This creates all the walls in room 3"""
    def __init__(self):
        super().__init__()
 
        walls = [		]
 
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)
 
        for x in range(100, 800, 100):
            for y in range(50, 451, 300):
                wall = Wall(x, y, 20, 200, BLACK)
                self.wall_list.add(wall)
 
        for x in range(150, 700, 100):
            wall = Wall(x, 200, 20, 200, BLACK)
            self.wall_list.add(wall)

def main():
	# initialize pygame
	pygame.init()

	# create window
	window = pygame.display.set_mode([800,600])
	pygame.display.set_caption("Platformer")

	#create player
	player = Player(50,50)
	movingsprites = pygame.sprite.Group()
	movingsprites.add(player)

	bullets = pygame.sprite.Group()

	# create room list
	rooms = []

	room = Room1()
	rooms.append(room)

	room = Room2()
	rooms.append(room)

	room = Room3()
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
		if player.rect.x < -30:
			for bullet in bullets:
				bullet.kill()

			if current_room_no == 0:
				current_room_no = len(rooms)-1
				current_room = rooms[current_room_no]
				player.rect.x = 770
			else:
				current_room_no -= 1
				current_room = rooms[current_room_no]
				player.rect.x = 770
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
