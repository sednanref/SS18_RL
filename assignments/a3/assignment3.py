import random
import sys

# Input: cell coordinates, gridworld
# Output: reward and boolean indicating posibility to move
def getReward(world, cell):

	# case when trying to leave the grid
	if (cell[0] < 0 or cell[0] > 8 or cell[1] < 0 or cell[1] > 8):
		return (-10, False)

	# Empty cell case
	if world[cell[0]][cell[1]] == ' ':
		return (-1, True)
	# X cell case
	elif world[cell[0]][cell[1]] == 'x':
		return (-20, False)
	# * cell case
	elif world[cell[0]][cell[1]] == '*':
		return (5, True)
	elif world[cell[0]][cell[1]] == 'G':
		return (100, 'stop')

def move_rand_31(cell):
	val = random.random()
	if val < 0.25: # move left
		return (cell[0], cell[1] - 1)
	elif val < 0.5: # move up
		return (cell[0] - 1, cell[1])
	elif val < 0.75: # move right
		return (cell[0], cell[1] + 1)
	else:	# move down
		return (cell[0] + 1, cell[1])

def reward_31(world, cell, reward, flag, count):

	gamma = 0.8

	if count > 10: 
		return 0
	elif flag == 'stop':
		return 0

	(rew_left, move_left) = getReward(world, (cell[0], cell[1] - 1))
	(rew_up, move_up) = getReward(world, (cell[0] - 1, cell[1]))
	(rew_right, move_right) = getReward(world, (cell[0], cell[1] + 1))
	(rew_down, move_down) = getReward(world, (cell[0] + 1, cell[1]))

	left = cell
	up = cell
	right = cell
	down = cell

	if move_left:
		left = (cell[0], cell[1] - 1)
	if move_up:
		up = (cell[0] - 1, cell[1])
	if move_right:
		right = (cell[0], cell[1] + 1)
	if move_down:
		left = (cell[0] + 1, cell[1])

	return 0.625 * (rew_right + gamma * reward_31(world, right, 0 , move_right, count + 1)) + 0.125 * (rew_up + gamma * reward_31(world, up, 0 , move_up, count + 1)) + 0.125 * (rew_left + gamma * reward_31(world, left, 0 , move_left, count + 1)) + 0.125 * (rew_down + gamma * reward_31(world, down, 0 , move_down, count + 1)) 


	



	# if val < 0.5:		# random case
	# 	new_cell = move_rand_31(cell)
	# 	(reward, flag) = getReward(world, new_cell)
	# 	if flag == 'stop' or count == 200: # Case it finishes
	# 		return reward
	# 	elif not flag: # Case it cannot move
	# 		return reward + gamma * reward_31(world, cell, count + 1)
	# 	elif flag: # Case it can move
	# 		return reward + gamma * reward_31(world, new_cell, count + 1)
	# else:				# move right case
	# 	new_cell = (cell[0] + 1, cell[1])
	# 	(reward, flag) = getReward(world, new_cell)
	# 	if flag == 'stop' or count == 200: # Case it finishes
	# 		return reward
	# 	elif not flag: # Case it cannot move
	# 		return reward + gamma * reward_31(world, cell, count + 1)
	# 	elif flag: # Case it can move
	# 		return reward + gamma * reward_31(world, new_cell, count + 1)


def t3_1(world):
	exp_val = []
	for i in range(len(world)):
		row_val = []
		for j in range(len(world[i])):
			if (world[i][j] == 'x'):
				row_val.append(-2000)
			elif (world[i][j] == 'G'):
				row_val.append(100)
			else:
				row_val.append(round(reward_31(world, (i, j), 0, 'going', 0), 2))
		exp_val.append(row_val)

	print ''
	print "3.1 Expected Values: "
	print ''
	for row in exp_val:
		print row
	return exp_val

	
def getDirection(cell, exp_val):
	best = -999
	char = u'\u2940'
	#char = 'N'

	# up
	if cell[0] - 1 >= 0:
		val = exp_val[cell[0] - 1][cell[1]]
		if val > best:
			char = u'\u2191'
			#char = 'U'
			best = val

	# left
	if cell[1] - 1 >= 0:
		val = exp_val[cell[0]][cell[1] - 1]
		if val > best:
			char = u'\u2190'
			#char = 'L'
			best = val

	# down
	if cell[0] + 1 < 9:
		val = exp_val[cell[0] + 1][cell[1]]
		if val > best:
			char = u'\u2193'
			#char = 'D'
			best = val

	# right
	if cell[1] + 1 < 9:
		val = exp_val[cell[0]][cell[1] + 1]
		if val > best:
			char = u'\u2192'
			#char = 'R'
			best = val

	return char

	


def t3_2(exp_val, world):
	
	policy = []
	for i in range(len(world)):
		polirow = []
		for j in range(len(world[i])):
			if world[i][j] == 'x' or world[i][j] == 'G':
				polirow.append('o')
			else:
				polirow.append(getDirection((i,j), exp_val))
		policy.append(polirow)

	print ''
	print '3.2 Policy: '
	print ''
	for row in policy:
		
		for elem in row:
			sys.stdout.write(elem)
		print ''



def t3_3(world):
	print '3.3'

def t3_4(world):
	print '3.4'

def main():
	
	world = [
			['*', '*', '*', ' ', ' ', ' ', ' ', '*', '*'],
			[' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', '*'],
			[' ', 'x', 'x', 'x', 'x', 'x', 'x', ' ', ' '],
			[' ', ' ', ' ', '*', '*', '*', ' ', 'x', ' '],
			[' ', ' ', 'x', 'x', 'x', 'x', 'x', ' ', 'G'],
			[' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' '],
			[' ', 'x', 'x', 'x', 'x', 'x', 'x', ' ', ' '],
			[' ', '*', '*', '*', '*', '*', '*', ' ', 'x'],
			[' ', '*', '*', '*', 'x', '*', '*', ' ', 'x']
		]

	exp_val = t3_1(world)
	t3_2(exp_val, world)
	# t3_3(world)
	# t3_4(world)

	# if flag == 'stop':
	# 	print 'ya'
	# elif not flag:
	# 	print 'no mueve'
	# else:
	# 	print 'mueve'


if __name__ == "__main__":
    main()