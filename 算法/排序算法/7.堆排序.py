import numpy as np

length = 0
def build(arr ):
	for i in range(length//2-1,-1,-1):
		swap(arr,i)

def swap (arr,index):
	left,right = index*2+1,index*2+2
	maxindex = index
	if left<length and arr[left]>arr[maxindex]:
		maxindex = left
	if right<length and arr[right]>arr[maxindex]:
		maxindex = right
	if maxindex!=index:
		arr[maxindex],arr[index] = arr[index],arr[maxindex]
		swap(arr,maxindex)

def duipaixu(arr):
	global length
	build(arr)
	for i in range(length-1,0,-1):
		arr[i],arr[0] = arr[0],arr[i]
		length=i
		swap(arr,0)

if __name__ == '__main__':
    arr = np.random.randint(1, 100, 20)
    print(arr)
    length = len(arr)
    duipaixu(arr)
    print(arr)
