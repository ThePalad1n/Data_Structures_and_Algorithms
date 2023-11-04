import random
import time

start_time = time.time()
# Function to do insertion sort
def insertionSort(arr):

	# Traverse through 1 to len(arr)
	for i in range(1, len(pool)):

		key = pool[i]

		# Move elements of arr[0..i-1], that are
		# greater than key, to one position ahead
		# of their current position
		j = i-1
		while j >=0 and key < pool[j] :
				pool[j+1] = pool[j]
				j -= 1
		pool[j+1] = key

#target and pool to generate numbers for tests
target = random.randint(1,10000)
pool=[]
n=10000

for i in range(n):
    pool.append(random.randint(1,10000))
k = len(pool)
    
insertionSort(pool)
lst = [] #empty list to store sorted elements
print("Sorted array is : ")
for i in range(len(pool)):
	lst.append(pool[i])	 #appending the elements in sorted order
print(lst)
print("--- %s seconds ---" % (time.time() - start_time))