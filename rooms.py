from main import *

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
		base_walls = [	[0, 0, 20, 250, BLACK],
						[0, 350, 20, 250, BLACK],
						[780, 0, 20, 250, BLACK],
						[780, 350, 20, 250, BLACK],
						[20, 0, 760, 20, BLACK],
						[20, 580, 760, 20, BLACK]	]

		for item in base_walls:
			wall = Wall(item[0],item[1],item[2],item[3],item[4])
			self.wall_list.add(wall)

class spawnRoom(Room):
    """This creates all the walls in room 3"""
    def __init__(self):
        super().__init__()
 
        walls = [	[0    ,250  ,20  ,100  ,BLACK]	]
 
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)

class Room1(Room):
	#creates walls in room1
	def __init__(self):
		Room.__init__(self)

		walls = [	[20*8 ,20*3 ,20  ,20*8 ,BLACK],
					[20*8 ,20*17,20  ,20*8 ,BLACK],
					[20*17,20*8 ,20*8,20*13,BLACK],
					[20*28,20*10,20*4,20   ,BLACK],
					[20*28,20*11,20  ,20*7 ,BLACK],
					[20*28,20*18,20*4,20   ,BLACK]	]

		for item in walls:
	 		wall = Wall(item[0],item[1],item[2],item[3],item[4])
	 		self.wall_list.add(wall)

class RandRoom(Room):
    """This creates all the walls in room 2"""
    def __init__(self):
        super().__init__()

        walls = []

        for i in range(random.randint(0,10)):
        	walls.append([20*random.randint(2,37),20*random.randint(2,27),20*random.randint(1,3),20*random.randint(1,3),BLACK])
 
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)