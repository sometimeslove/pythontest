import  random
import numpy as np

'''
随机数生成函数
'''
def random_list(start,end ,size):
	random_list=[random.randint(start,end) for i in range(size)]
	return random_list

def maopao(arr):
	if len(arr)<2:
		return
	for i in range(len(arr)-1,0,-1):
		for j in range(0,i):
			if arr[j]>arr[j+1]:
				arr[j],arr[j+1]=arr[j+1],arr[j]


if __name__ == '__main__':
	arr= random_list(1,6,5)
	arr = np.random.randint(1,100,20)
	print(arr)
	maopao(arr)
	print(arr)
	np.random.shuffle(arr)
	print(arr)
	maopao(arr)
	print(arr)