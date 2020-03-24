import  random
import numpy as np

def xuanzhe(arr):
	if len(arr)<2:
		return
	for i in range(0,len(arr)):
		for j in range(i,len(arr)):
			if arr[j]<arr[i]:
				arr[i], arr[j] = arr[j], arr[i]

if __name__ == '__main__':
	arr = np.random.randint(1,100,20)
	print(arr)
	xuanzhe(arr)
	print(arr)
	np.random.shuffle(arr)
	print(arr)
	xuanzhe(arr)
	print(arr)