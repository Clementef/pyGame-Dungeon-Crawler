from maps import *
import random

"""
18x13 tiles
One tile is 40x40 pixels

1 = wall
2 = enemy
3 = powerup
"""

# translates tile position to screen position
def tilesToScreen(tile_x,tile_y):
	screen_x = (tile_x*40)+40
	screen_y = (tile_y*40)+40
	return screen_x,screen_y

def readMap(map):
	walls = []
	enemies = []
	powerups = []

	# get the type of each tile on the map and append to list if sprite
	for i in range(len(map)):
		for j in range(len(map[i])):
			type = map[i][j]
			position = tilesToScreen(j,i)

			if type == 1:
				walls.append([position[0],position[1],40,40])
			if type == 2:
				pass
			if type == 3:
				pass

	# return map with sprite information
	return [walls,enemies,powerups]

# reads a random map
def readRandMap():
	rand = random.randint(0,len(mapsList)-1)
	return readMap(mapsList[rand])
	print(rand)