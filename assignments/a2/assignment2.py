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

	reward = 0 				# Reward when the student starts the exam
	policy = tasks # Order of tasks didn't change becaus of policy

	print 'Expected reward following policy A: '	
	print get_value(policy, reward, 1, False)

def exercise2_3_2(tasks):
	
	reward = 0 				# Reward when the student starts the exam
	tasks2 = sorted(tasks, key=lambda task: task[1]) # Sort on solution prob.

	policy2 = []

	# Revert the array, our policy is trying to solve easy tasks first.
	for i in range(len(tasks2) - 1, -1, -1):
		policy2.append(tasks2[i])


	print 'Expected reward following policy B: '	
	print get_value(policy2, reward, 1, False)

def exercise2_4(tasks):
	
	reward = 0 				# Reward when the student starts the exam
	tasks3 = sorted(tasks, key=lambda task: task[0]) # Sort on points.
	
	policy3 = []

	# Revert the array, our policy is trying to solve tasks with more points first.
	for i in range(len(tasks3) - 1, -1, -1):
		policy3.append(tasks3[i])

	print 'Expected reward following policy C: '	
	print get_value(policy3, reward, 1, False)

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
	
	exercise2_3_1(tasks)
	exercise2_3_2(tasks)
	exercise2_4(tasks)



if __name__ == "__main__":
    main()