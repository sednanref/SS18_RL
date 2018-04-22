import random
import matplotlib.pyplot as plt

# function to return best arm (q*(a))
def getBest(q):
	k = 0
	for i in range(1, len(q)):
		if q[i][-1] > q[k][-1]:
			k = i

	return k

def exercise1_2(arms):

	acum = 0

	for i in range(0,20):
		# Uniform arm selection
		k = random.randrange(0, len(arms))
		# print 'Arm selected: ' + str(k)
		reward = random.uniform(arms[k][0], arms[k][1])
		# print 'Reward: ' + str(reward)
		acum = acum + reward

	print '1.2) Average reward after 20 uniformly chosen action: '
	print acum/20

def exercise1_3(arms):



	# Expected Values
	q = [[0], [0], [0], [0], [0], [0], [0]]
	# Times selected
	ks = [0, 0, 0, 0, 0, 0, 0]
	ks_hundred = [[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]]
	hundred = 1
	# Epsilon
	eps = 0.1

	avg = [0]

	# take random 
	best = random.randrange(0, len(arms))

	for i in range(0,2000):

		# Get arm selection percentage
		if (i % 100 == 0):
			if i != 0:
				for j in range(0, len(ks)):
					ks_hundred[j].append(0)

				hundred = hundred + 1
					

		selection = random.random()
		#print selection
		# Exploration case
		if selection < eps:
			# arm selected
			k = random.randrange(0, len(arms))
			# reward
			reward = random.uniform(arms[k][0], arms[k][1])
			# take last q_k
			last = q[k][-1]
			# Obtain new  expected value for arm k
			qk = last + (1.0 / (ks[k] + 1)) * (reward - last)
			# Append new reward for selected arm
			q[k].append(qk)
			# update number of times arm k was selected
			ks[k] = ks[k] + 1
			ks_hundred[k][hundred] = ks_hundred[k][hundred] + 1
			
			# Get general avg
			new_avg = avg[-1] + (1.0 / (i + 1) * (reward - avg[-1]))
			avg.append(new_avg)
			# Update best arm:
			best = getBest(q)
			
		else:
			# reward
			reward = random.uniform(arms[best][0], arms[best][1])
			# take last q_k
			last = q[best][-1]
			# Obtain new  expected value for arm k
			qk = last + (1.0 / (ks[best] + 1)) * (reward - last)
			# Append new reward for selected arm
			q[best].append(qk)
			# update number of times arm k was selected
			ks[best] = ks[best] + 1
			ks_hundred[best][hundred] = ks_hundred[best][hundred] + 1
			
			# Get general avg
			new_avg = avg[-1] + (1.0 / (i + 1) * (reward - avg[-1]))
			avg.append(new_avg)
			# Update best arm:
			best = getBest(q)


	# legend = [] 
	# for i in range(len(q)):
	# 	plt.plot(q[i])
	# 	legend.append('Arm ' + str(i + 1))


	# plt.legend(legend, loc='lower right')


	plt.plot(avg)
	plt.title('Average Reward after 2000 chosen actions.')
	plt.xticks(range(0, 2000, 100))	
	#plt.show()
	plt.savefig('1_3_1_Avg_Reward')
	plt.close()

	legend = []
	### Plot usage percentages
	xaxis = range(0,2100, 100)
	for i in range(len(ks_hundred)):
	 	plt.plot(xaxis, ks_hundred[i])
	 	legend.append('Arm ' + str(i + 1))


	plt.title('Usage percentage every 100 steps')
	plt.xticks()
	plt.ylabel('Usage percentage')
	plt.xlabel('Number of Actions taken')
	plt.legend(legend, loc='lower right')
	plt.xticks(range(0, 2000, 100))	
	#plt.show()
	plt.savefig('1_3_2_Usage_Percentage')
	plt.close()

def exercise1_4(arms):

	# Expected Values
	q = [[0], [0], [0], [0], [0], [0], [0]]
	# Times selected
	ks = [0, 0, 0, 0, 0, 0, 0]
	ks_hundred = [[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]]
	hundred = 1
	# Epsilon
	eps = 0.1

	avg = [0]

	# take random 
	best = random.randrange(0, len(arms))

	for i in range(0,2000):

		if (i == 1000):
			arms[3] = [6,8]

		# Get arm selection percentage
		if (i % 100 == 0):
			if i != 0:
				for j in range(0, len(ks)):
					ks_hundred[j].append(0)

				hundred = hundred + 1
					

		selection = random.random()
		#print selection
		# Exploration case
		if selection < eps:
			# arm selected
			k = random.randrange(0, len(arms))
			# reward
			reward = random.uniform(arms[k][0], arms[k][1])
			# take last q_k
			last = q[k][-1]
			# Obtain new  expected value for arm k
			qk = last + (1.0 / (ks[k] + 1)) * (reward - last)
			# Append new reward for selected arm
			q[k].append(qk)
			# update number of times arm k was selected
			ks[k] = ks[k] + 1
			ks_hundred[k][hundred] = ks_hundred[k][hundred] + 1
			
			# Get general avg
			new_avg = avg[-1] + (1.0 / (i + 1) * (reward - avg[-1]))
			avg.append(new_avg)
			# Update best arm:
			best = getBest(q)
			
		else:
			# reward
			reward = random.uniform(arms[best][0], arms[best][1])
			# take last q_k
			last = q[best][-1]
			# Obtain new  expected value for arm k
			qk = last + (1.0 / (ks[best] + 1)) * (reward - last)
			# Append new reward for selected arm
			q[best].append(qk)
			# update number of times arm k was selected
			ks[best] = ks[best] + 1
			ks_hundred[best][hundred] = ks_hundred[best][hundred] + 1
			
			# Get general avg
			new_avg = avg[-1] + (1.0 / (i + 1) * (reward - avg[-1]))
			avg.append(new_avg)
			# Update best arm:
			best = getBest(q)


	# legend = [] 
	# for i in range(len(q)):
	# 	plt.plot(q[i])
	# 	legend.append('Arm ' + str(i + 1))


	# plt.legend(legend, loc='lower right')


	plt.plot(avg)
	plt.title('Average Reward after 2000 chosen actions.')
	plt.xticks(range(0, 2000, 100))	
	plt.show()
	plt.savefig('1_4_1_Avg_Reward')
	plt.close()

	legend = []
	### Plot usage percentages
	xaxis = range(0,2100, 100)
	for i in range(len(ks_hundred)):
	 	plt.plot(xaxis, ks_hundred[i])
	 	legend.append('Arm ' + str(i + 1))


	plt.title('Usage percentage every 100 steps')
	plt.xticks()
	plt.ylabel('Usage percentage')
	plt.xlabel('Number of Actions taken')
	plt.legend(legend, loc='lower right')
	plt.xticks(range(0, 2000, 100))	
	plt.show()
	plt.savefig('1_4_2_Usage_Percentage')
	plt.close()




def main():

	arms = [[-2,3], [1,4], [2,3], [-1,5], [0,4],[1,4], [3,7]]

	exercise1_2(arms)

	exercise1_3(arms)

	exercise1_4(arms)

	exercise1_5(arms)
	

if __name__ == "__main__":
    main()