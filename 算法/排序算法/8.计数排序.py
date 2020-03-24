import random
def Count_Sort(arr):
	cur = {i:0  for i in set(arr)}
	for i in range(len(arr)):
		cur[arr[i]]+=1
	b=[]
	cur = sorted(cur.items(),key = lambda x:x[0])
	for key,value in cur:
		while value>0:
			b.append(key)
			value-=1
	arr=b
	return b

if __name__ == '__main__':
    # arr = np.random.randint(1, 100, 20)
    arr = [random.randint(1,100) for i in range(20)]
    print(arr)
    arr = Count_Sort(arr)
    print(arr)