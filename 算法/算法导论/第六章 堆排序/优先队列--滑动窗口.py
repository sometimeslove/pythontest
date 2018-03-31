
class Solution():
    def __init__(self,arr,winsize):
        self._size = winsize
        self.arr = arr
        if len(arr)<winsize:
            return
        self._minwin = arr[0:winsize]
        self._maxwin = arr[0:winsize]
        self._createMaxDui((self._size-1)//2)
        self._createMinDui((self._size-1)//2)

    def _printMaxAndMinValue(self):
        for i in range(0,len(self.arr)-self._size+1):
            print('%d %s %s'%(i+1, self._getmaxvalue(),self._getminvalue()))
            self._changeValue(i+self._size, i)

    def _getmaxvalue(self):
        if len(self._maxwin)>0:
            return self._maxwin[0]

    def _getminvalue(self):
        if len(self._minwin)>0:
            return self._minwin[0]

    def _changeValue(self,addvalue, delvalue):
        if len(self.arr)<=addvalue:
            return
        delindex = self._maxwin.index(arr[delvalue])
        self._maxwin[delindex] = arr[addvalue]
        if arr[delvalue]<arr[addvalue]:
            self._treateMaxChildUp(delindex)
        else:
            self._treateMaxChildDown(delindex)
        delindex = self._minwin.index(arr[delvalue])
        self._minwin[delindex] = arr[addvalue]
        if arr[delvalue]<arr[addvalue]:
            self._treateMinChildDown(delindex)
        else:
            self._treateMinChildUp(delindex)

    def _createMaxDui(self, startIndex):
        for i in range(startIndex,-1,-1):
            self._treateMaxChildDown(i)

    def _createMinDui(self, startIndex):
        for i in range(startIndex,-1,-1):
            self._treateMinChildDown(i)

    def _treateMinChildUp(self, nodeindex):
        # if nodeindex<=0:
        #     return
        # partent = (nodeindex-1)//2
        # if self._minwin[partent]> self._minwin[nodeindex]:
        #     self._minwin[partent], self._minwin[nodeindex] = self._minwin[nodeindex], self._minwin[partent]
        #     self._treateMinChildUp(partent)
        partent = (nodeindex-1)//2
        while partent>=0 and self._minwin[partent]>self._minwin[nodeindex]:
            self._minwin[partent], self._minwin[nodeindex] = self._minwin[nodeindex], self._minwin[partent]
            partent =  (partent-1)//2

    def _treateMaxChildUp(self, nodeindex):
        if nodeindex<=0:
            return
        partent = (nodeindex-1)//2
        if self._maxwin[partent]< self._maxwin[nodeindex]:
            self._maxwin[partent], self._maxwin[nodeindex] = self._maxwin[nodeindex], self._maxwin[partent]
            self._treateMaxChildUp(partent)

    def _treateMinChildDown(self, nodeindex):
        left = nodeindex*2+1
        right = nodeindex*2+2
        largeindex = nodeindex
        if left<self._size and self._minwin[left]< self._minwin[largeindex]:
            largeindex = left
        if right<self._size and self._minwin[right]< self._minwin[largeindex]:
            largeindex = right
        if largeindex != nodeindex:
            self._minwin[nodeindex],self._minwin[largeindex] = self._minwin[largeindex], self._minwin[nodeindex]
            self._treateMinChildDown(largeindex)

    def _treateMaxChildDown(self, nodeindex):
        left = nodeindex*2+1
        right = nodeindex*2+2
        largeindex = nodeindex
        if left<self._size and self._maxwin[left]> self._maxwin[largeindex]:
            largeindex = left
        if right<self._size and self._maxwin[right]> self._maxwin[largeindex]:
            largeindex = right
        if largeindex != nodeindex:
            self._maxwin[nodeindex],self._maxwin[largeindex] = self._maxwin[largeindex], self._maxwin[nodeindex]
            self._treateMaxChildDown(largeindex)

if __name__ == '__main__':
    arr = [5,8,23,9,0,1,4,7,8,5]
    winsize = int(input('请输入窗口大小：'))
    s = Solution(arr,winsize)
    s._printMaxAndMinValue()