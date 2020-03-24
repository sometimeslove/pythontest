import  random
import numpy as np

def merge(left,right):
    l,r =  len(left),len(right)
    cur = []
    while l>0 and r>0:
        if  left[0]<= right[0]:
            cur.append(left[0])
            left.pop(0)
            l -=1
        else:
            cur.append(right[0])
            right.pop(0)
            r-=1
    if l==0:
        cur.extend(right)
    else:
        cur.extend(left)

def merge_sort(arr):
    if len(arr)<2:
        return arr
    middle = len(arr)//2
    left,right = arr[:middle],arr[middle:]
    return merge(merge_sort(left),merge_sort(right))


if __name__ == '__main__':
	arr = np.random.randint(1,100,20)
	print(arr)
	arr = merge_sort(arr)
	print(arr)
	np.random.shuffle(arr)
	print(arr)
	arr = merge_sort(arr)
	print(arr)