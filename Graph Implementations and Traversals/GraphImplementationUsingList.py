class vertex:
    def __init__(self,id):
        self.id=id
        self.adjacent={}
        self.visited=False
        #self.distance=sys.maxint
    
    def getConnections(self):
        return self.adjacent.keys()
    
    def getCosts(self,key):
        return self.adjacent[key]

    
    def addNeighbour(self,cost):
        pass

    def GetID(self):
        return self.id

    
class Graph:
    def __init__(self):
        self.vertices={}
        self.Numvertices=0
        print('Graph Initialled Successfully')
    def __iter__(self):
        return iter(self.vertices.values())
    
    def AddVertices(self,id):

        if id not in self.vertices:
            self.Numvertices+=1
            v=vertex(id)
            self.vertices[id]=v
            print('Added the vertices',id)
            return
        print('Vertices already present!!')
    def AddEgdes(self,frm,to,cost):
        if frm not in self.vertices:
            v=vertex(frm)
            self.vertices[frm]=v
        if to not in self.vertices:
            v=vertex(to)
            self.vertices[to]=v
        self.vertices[frm].adjacent[self.vertices[to]]=cost
        self.vertices[to].adjacent[self.vertices[frm]]=cost
        print('Added Successfully')
    def getEdges(self):
        edges=[]
        for k,v in self.vertices.items():
            #print(v.getConnections())
            for w in v.getConnections():
                edges.append((k,w.id,v.getCosts(w)))
        return edges



G=Graph()
al=['a','b','c','d','e']
for i in range(0,5):
    G.AddVertices(al[i])
#for i in range(0,5):
G.AddEgdes('a','b',4)
G.AddEgdes('a','c',1)
G.AddEgdes('b','e',4)
G.AddEgdes('c','d',4)
G.AddEgdes('d','e',4)
print(G.getEdges())

#------------------Output Sample----------------------------
'''
Graph Initialled Successfully
Added the vertices a
Added the vertices b
Added the vertices c
Added the vertices d
Added the vertices e
Added Successfully
Added Successfully
Added Successfully
Added Successfully
Added Successfully
[('a', 'b', 4), ('a', 'c', 1), ('b', 'a', 4), ('b', 'e', 4), ('c', 'a', 1), ('c', 'd', 4), ('d', 'c', 
4), ('d', 'e', 4), ('e', 'b', 4), ('e', 'd', 4)]
'''
