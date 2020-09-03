class Vertex:
    def __init__(self,id):
        self.id=id
        self.visited=False
    
    def SetId(self,val):
        self.id=val
    
    def GetId(self):
        return self.id

class Graph:
    def __init__(self,NumVertices):
        self.AdjMatrix=[[-1]*NumVertices for _ in range(NumVertices)]
        self.Vertices=[]
        self.NumVertices=NumVertices
        #Creating vertex 
        for i in range(NumVertices):
            v=Vertex(i)
            self.Vertices.append(v)
        print('Graph Initialed successfully..!!')
    
    def SetVertex(self,id,vtx):
        if 0 <= id < self.NumVertices:
            self.Vertices[id].SetId(vtx)
    
    def GetVertex(self,id):
        for i in range(self.NumVertices):
            if id == self.Vertices[i].GetId():
                return i
        return -1

    def AddEgde(self,frm,to,cost):
        if self.GetVertex(frm)!=-1 and self.GetVertex(to)!=-1:
            self.AdjMatrix[self.GetVertex(frm)][self.GetVertex(to)]=cost
            self.AdjMatrix[self.GetVertex(to)][self.GetVertex(frm)]=cost
            print('----- Added Edge successfully----------')
            return
        print('--Verex Not found !! Please double check')
    
    def printMatrix(self):
        print('---Printing Graph Matrix---------')
        for i in range(self.NumVertices):
            v=[]
            for j in range(self.NumVertices):
                v.append(self.AdjMatrix[i][j])
            print(v)


    def getConnections(self):
        edges=[]
        for i in range(self.NumVertices):
            for j in range(self.NumVertices):
                if self.AdjMatrix[i][j]!=-1:
                    iv=self.Vertices[i].GetId()
                    jv=self.Vertices[j].GetId()
                    edges.append((iv,jv,self.AdjMatrix[i][j]))
        return edges
#--------------GRAPH INITIALIZATION---------------------------------------
G1=Graph(5)
al=['a','b','c','d','e']
for i in range(0,5):
    G1.SetVertex(i,al[i])
G1.AddEgde('a','e',10)
G1.AddEgde('a','c',20)
G1.AddEgde('c','b',30)
G1.AddEgde('b','e',40)
G1.AddEgde('e','d',60)
G1.AddEgde('f','e',70)
G1.printMatrix()
print(G1.getConnections())

