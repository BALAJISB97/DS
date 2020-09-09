class minheap:
    def __init__(self):
        self.heap=[0]
        self.heaplen=0

    def push(self,data):
        self.heap.append(data)
        self.__floatup(len(self.heap)-1)

    def pop(self):
        if len(self.heap)>2:
            self.__swap(1,len(self.heap)-1)
            maxx=self.heap.pop()
            self.__bubbledown(1)
        elif len(self.heap)==2:
            maxx=self.heap.pop()
        else:
            maxx=False
        return maxx
    
    def peek(self):
        if len(self.heap)>=1:
            return self.heap[1]
        else:
            return False
        
    def __swap(self,i,j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __floatup(self,index):
        parent = index//2
        if index <= 1:
            return
        elif self.heap[index] < self.heap[parent]:
            self.__swap(index, parent)
            self.__floatup(parent)

    def __bubbledown(self,index):
        left = index * 2
        right = index * 2 + 1
        smallest = index
        if len(self.heap) > left and self.heap[smallest] > self.heap[left]:
            smallest = left
        if len(self.heap) > right and self.heap[smallest] > self.heap[right]:
            smallest = right
        if smallest != index:
            self.__swap(index, smallest)
            self.__bubbledown(smallest)
#--------------------------------------------------------------------------------------
myh=minheap()
myh.push(10)
myh.push(20)
myh.push(3)
myh.push(67)
print(str(myh.heap[0:len(myh.heap)]))
print(str(myh.pop()))
print(myh.peek())
print(myh.pop())
print(myh.pop())
print(myh.pop())
print(myh.pop())
print(myh.pop())