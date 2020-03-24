import random
import math
def getdata(arr,startindex, endindex, wantindex):
    if startindex>=endindex:
        return
    tmp = random.randint(startindex,endindex)
    arr[endindex], arr[tmp] = arr[tmp], arr[endindex]
    flag = startindex-1
    for i in range(startindex,endindex):
        if arr[i]<arr[endindex]:
            flag += 1
            arr[flag], arr[i] = arr[i], arr[flag]
    arr [flag+1],arr[endindex] = arr[endindex],arr[flag+1]
    if flag+1 == wantindex:
        return arr[wantindex]
    elif flag+1<wantindex:
        return getdata(arr,flag+2,endindex,wantindex)
    else:
        return getdata(arr,startindex,flag,wantindex)

if __name__ == '__main__':
    arr = [1,2,3,4,5,7]
    lenth = len(arr)
    if (lenth%2)==1:
        wantindex = lenth//2
        print(getdata(arr,0,lenth-1,wantindex))
    else:
        wantindex = lenth//2
        print((getdata(arr,0,lenth-1,wantindex)+getdata(arr,0,lenth-1,wantindex-1))/2)
