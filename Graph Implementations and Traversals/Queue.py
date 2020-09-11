class Queue:
    def __init__(self):
        self.q=[]
    def enqueue(self,val):
        self.q.append(val)
    def dequeue(self):
        return self.q.pop(0)
    def IsQEmpty(self):
        return (len(self.q)==0)

#------------ Sample Queue---------------------
q1=Queue()
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
print(q1.q)
print(q1.dequeue())
print(q1.q)
