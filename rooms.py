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