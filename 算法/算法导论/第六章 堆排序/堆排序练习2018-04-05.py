def duisort(arr):
    createdui(arr)
    for i in range(len(arr)-1,0,-1):
        arr[i],arr[0]= arr[0],arr[i]
        treatechilddui(arr,0,i)

def createdui(arr):
    lenth = len(arr)
    startindex = (lenth-2)//2
    for i in range(startindex,-1,-1):
        treatechilddui(arr,i,lenth)


#处理
def treatechilddui(arr,curindex,largeindex):
    left = 2*curindex+1
    right = 2*curindex +2
    tmp = curindex
    if left<largeindex and arr[left]<arr[tmp]:
        tmp =left
    if right<largeindex and arr[right]<arr[tmp]:
        tmp =right
    if tmp!=curindex:
        arr[curindex],arr[tmp] = arr[tmp],arr[curindex]
        treatechilddui(arr,tmp,largeindex)

if __name__ == '__main__':
    arr = [2,3,2,6,8,1,3,5,6,9,1]
    duisort(arr)
    print(arr)