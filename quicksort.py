# def partition(arr,start,stop):
# 	pivot = start 
# 	i = start + 1

# 	for j in range(start + 1, stop + 1):
#         # exchange left and right pointer if right pointer less than pivot
#         # i moves when it exhanges element
# 		if arr[j] <= arr[pivot]:
# 			arr[i] , arr[j] = arr[j] , arr[i]
# 			i = i + 1

# 	arr[pivot] , arr[i - 1] = arr[i - 1] , arr[pivot]
# 	pivot = i - 1
# 	return (pivot)

# def quickSort(array, start, stop):
# 	if start < stop:
# 		pi = partition(array, start, stop)
# 		quickSort(array, start, pi - 1)
# 		quickSort(array, pi + 1, stop)

# # Driver Code
# if __name__ == "__main__":
# 	array = [10, 7, 8, 9, 1, 5]
# 	quickSort(array, 0, len(array) - 1)
# 	print(array)


import random

# Function to find random pivot
def partitionrand(arr , start, stop):
	randpi = random.randrange(start, stop)
    # swapping starting element with random pivot
	arr[start], arr[randpi] = arr[randpi], arr[start]
	return partition(arr, start, stop)

# Function to find the partition position
def partition(arr,start,stop):
	pivot = start 
	i = start + 1
	
	for j in range(start + 1, stop + 1):
		if arr[j] <= arr[pivot]:
			arr[i] , arr[j] = arr[j] , arr[i]
			i = i + 1
	arr[pivot] , arr[i - 1] = arr[i - 1] , arr[pivot]
	pivot = i - 1
	return (pivot)

def quickSort(array, start , stop):
	if(start < stop):		
		pi = partitionrand(array, start, stop)
		quickSort(array, start, pi - 1)
		quickSort(array, pi + 1, stop)

# Driver Code
if __name__ == "__main__":
	array = [10, 7, 8, 9, 1, 5]
	quickSort(array, 0, len(array) - 1)
	print(array)
