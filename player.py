from main import *

class Player(pygame.sprite.Sprite):
	# set speed vector
	change_x = 0
	change_y = 0

	# constructor func
	def __init__(self):

		# call parent's constructor
		pygame.sprite.Sprite.__init__(self)

		# set height, width, set texture
		self.image = pygame.Surface([playerSize,playerSize])
		self.image.fill(WHITE)

		# set pos
		self.rect = self.image.get_rect()
		self.rect.x = 400-(self.rect.width/2)
		self.rect.y = 300-(self.rect.height/2)

	#change speed
	def changeSpeed(self,x,y):
		self.change_x += x
		self.change_y += y

	#calculate player's new position
	def update(self,walls):
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
		self.image.fill(PURPLE)

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