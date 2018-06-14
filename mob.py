from main import *
import random

class Mob(pygame.sprite.Sprite):

	def __init__(self,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((enemySize,enemySize))
		self.image.fill(RED)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.change_x = random.randint(-4,4)
		self.change_y = random.randint(-4,4)

	def update(self,walls,bullets):
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

		if (len(block_hit_list) > 0) or (self.rect.right >= 800-20) or (self.rect.left <= 20):
			self.change_x *= -1

		# vert movement
		self.rect.y += self.change_y

		block_hit_list = pygame.sprite.spritecollide(self,walls,False)
		for block in block_hit_list:
			# set position if vert collision
			if self.change_y > 0:
				self.rect.bottom = block.rect.top
			else:
				self.rect.top = block.rect.bottom

		if (len(block_hit_list) > 0):
			self.change_y *= -1

		# kill if hit by bullet
		if pygame.sprite.spritecollide(self,bullets,False):
			self.kill()