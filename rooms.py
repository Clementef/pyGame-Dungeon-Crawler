from main import *
from mapReader import *
from maps import *

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

class Room():
	#lists of walls & enemies
	wall_list = None
	enemy_sprites = None

	def __init__(self):
		# constructor that creates wall lists
		self.wall_list = pygame.sprite.Group()
		self.enemy_sprites = pygame.sprite.Group()
		default_walls = [	[0, 0, 20, 250, BLACK],
						[0, 350, 20, 250, BLACK],
						[780, 0, 20, 250, BLACK],
						[780, 350, 20, 250, BLACK],
						[20, 0, 760, 20, BLACK],
						[20, 580, 760, 20, BLACK]	]

		for item in default_walls:
			wall = Wall(item[0],item[1],item[2],item[3],item[4])
			self.wall_list.add(wall)

class spawnRoom(Room):
    def __init__(self):
        Room.__init__(self)
 
        walls = [	[0    ,250  ,20  ,100  ,BLACK]	]

        # get walls from the chosen map
        readWalls = readMap(spawnMap)

        # add color to wall data, add walls to walls list
        for i in readWalls[0]:
        	i.append(BLACK)
        	walls.append(i)

 
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)

class Room1(Room):
	def __init__(self):
		Room.__init__(self)

		walls = []
		enemies = []

		# get walls from the chosen map
		positionsMap = readMap(firstMap)
		readWalls = positionsMap[0]
		readEnemies = positionsMap[1]

		# add color to wall data, add walls to walls list
		for i in readWalls:
			i.append(BLACK)
			walls.append(i)

		for item in walls:
	 		wall = Wall(item[0],item[1],item[2],item[3],item[4])
	 		self.wall_list.add(wall)

 		# add read enemies to enemies list, add that to master list
		for i in readEnemies:
			enemies.append(i)

		for item in enemies:
			enemySprite = Mob(item[0],item[1])
			self.enemy_sprites.add(enemySprite)

class RandRoom(Room):
	def __init__(self):
		Room.__init__(self)

		walls = []
		enemies = []

		# get walls from the chosen map
		positionsMap = readMap(firstMap)
		readWalls = positionsMap[0]
		readEnemies = positionsMap[1]

		# add color to wall data, add walls to walls list
		for i in readWalls:
			i.append(BLACK)
			walls.append(i)

		for item in walls:
	 		wall = Wall(item[0],item[1],item[2],item[3],item[4])
	 		self.wall_list.add(wall)

 		# add read enemies to enemies list, add that to master list
		for i in readEnemies:
			enemies.append(i)

		for item in enemies:
			enemySprite = Mob(item[0],item[1])
			self.enemy_sprites.add(enemySprite)