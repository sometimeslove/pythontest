import numpy as np

'''
自己写的，不可取
'''
def charu(arr):
	for i in range(1,len(arr)):
		for j in range(0,i):
			if arr[i]<arr[j]:
				arr.insert(j-1,arr[i])
				break;

'''
参考网上的写的简洁版本
'''
def insert_sort(arr):
	l = len(arr)
	for i in range (1,l):
		while i>=1 and arr[i]<arr[i-1]:
			arr[i],arr[i-1]=arr[i-1],arr[i]
			i-=1



if __name__ == '__main__':
	arr = np.random.randint(1,100,20)
	print(arr)
	# charu(arr)
	# print(arr)
	# np.random.shuffle(arr)
	# print(arr)
	insert_sort(arr)
	print(arr)