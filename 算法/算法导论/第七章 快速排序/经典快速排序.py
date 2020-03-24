import random
def quicksort(arr,startindex,endindex):
    if startindex>=endindex:
        return
    r = random.randint(startindex,endindex)
    arr[r],arr[endindex] = arr[endindex],arr[r]
    tmp = arr[endindex]
    flag = startindex-1
    for i in range(startindex,endindex):
        if arr[i]<tmp:
            flag=flag+1
            arr[flag],arr[i] = arr[i],arr[flag]
    arr[flag+1],arr[endindex] = arr[endindex],arr[flag+1]
    quicksort(arr,startindex,flag)
    quicksort(arr,flag+2,endindex)

if __name__ == '__main__':
    arr = [2,3,2,6,8,1,3,5,6,9,1]
    quicksort(arr,0,len(arr)-1)
    print(arr)