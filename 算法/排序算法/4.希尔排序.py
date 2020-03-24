import numpy as np
import math

def xier(arr):
	i=math.floor(len(arr)/2)
	while(i>0):
		for j in range(0,i):
			for k in range(j+i,len(arr),i):
				for m in range(k-i,-1,-1):
					if arr[m]>arr[k]:
						arr[m],arr[k] = arr[k],arr[m]
		i=math.floor(i/2)

def shell_sort(arr):
	n = len(arr)
	step = n//2
	while step>0:
		for i in range(step,n):
			while i>=step and arr[i]<arr[i-step]:
				arr[i],arr[i-step] = arr[i-step],arr[i]
				i -= step
		step = step//2


if __name__ == '__main__':
	arr = np.random.randint(1,100,21)
	print(arr)
	shell_sort(arr)
	print(arr)
	np.random.shuffle(arr)
	print(arr)
	shell_sort(arr)
	print(arr)