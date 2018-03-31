#创建堆
def createDui(arr):
    lenth = len(arr)
    if lenth == 0:
        return
    for i in range(lenth-1//2,-1,-1 ):
        treatChild(arr,i,lenth)

def treatChild(arr, nodeindex, curduilen):
    if curduilen == 0:
        return
    left = nodeindex*2 +1
    right = nodeindex*2 +2
    largestindex = nodeindex
    if left<curduilen and arr[largestindex]< arr [left]:
        largestindex = left
    if right<curduilen and arr[largestindex]< arr [right]:
        largestindex = right
    if largestindex != nodeindex:
        arr[largestindex], arr[nodeindex] = arr[nodeindex],  arr[largestindex]
        treatChild(arr, largestindex, curduilen)

def sortedByDui(arr):
    createDui(arr)
    for i in range(len(arr)-1,-1, -1):
        arr[0],arr[i] = arr[i],arr[0]
        treatChild(arr,0,i)

if __name__ == '__main__':
    arr = [2,3,2,6,8,1,3,5,6,9,1]
    sortedByDui(arr)
    print(arr)