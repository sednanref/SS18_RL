# Tasks: list of tasks to be solved yet, the current tasks is always the first.
# Reward: reward colected so far under certain probabilities.
# Attemp: number of total attempts the student had so far.
# Repeated: flag to identify if the student has tried to solve the current task unsuccesfully once.

def get_value(tasks, reward, attempt, repeated):

	# return zero reward after 10 attempts or when there are no tasks left.
	if (attempt > 10 or len(tasks) == 0):
		return reward


	if (not repeated):
		# In case the task has not been attempted before, return the obtained reward so far 
		# return get_value(tasks[1:], reward + tasks[0][0] * tasks[0][1], attempt + 1, False) + get_value(tasks, reward, attempt + 1, True)
		return tasks[0][1] * get_value(tasks[1:], reward + tasks[0][0], attempt + 1, False) +  (1.0 - tasks[0][1]) * get_value(tasks, reward, attempt + 1, True)
				# plus the expected reward after succeeding in this task
				
				# plus the expected reward after failing this task and trying it again
				

	else:
		# In case he is trying the same task a second time, return the obtained reward so far
		# return get_value(tasks[1:], reward + tasks[0][0] * tasks[0][1], attempt + 1, False) + get_value(tasks[1:], reward, attempt + 1, False)
		return tasks[0][1] * get_value(tasks[1:], reward + tasks[0][0], attempt + 1, False) + (1.0 - tasks[0][1]) * get_value(tasks[1:], reward, attempt + 1, False)
				# plus the expected reward after succeeding in this task
				
				# plus the expected reward after failing this task and trying nex one
				
		


def exercise2_3_1(tasks):
	reward = 0 				# Reward when the student hasn't started
	return get_value(tasks, reward, 1, False)

def main():
	
	tasks = [
		(8, 0.15), 
		(6, 0.4), 
		(10, 0.25),
		(2, 0.6),
		(7, 0.35),
		(3, 0.5),
		(20, 0.2)
		]
	
	reward_p1 = exercise2_3_1(tasks)

	print 'Expected reward following policy 1: '
	print reward_p1


if __name__ == "__main__":
    main()