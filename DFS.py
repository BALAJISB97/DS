
from GraphImplementationUsingList import Graph,vertex
from GraphImplementationUsingAdjMatrix import Graph as GM,Vertex as VM

# ------------- GRAPH INITIALIZATION USING ADJCENCY LIST-----------------------------
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
#--------------------------GRAPH INTIALIZATION USING MATRIX--------------------------
print('-------------Matrix Graph----------------------------------------------')
G1=GM(5)
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
print('-----------------End of Matrix Content--------------------------------')

#---------------------DFS Travesal made easy----------------------------------------
def dfs(g,vertex,visited):
    visited[vertex]=True
    print(vertex.id)
    for nbr in vertex.getConnections():
        if nbr not in visited:
            dfs(g,nbr,visited)

def DFSTraversal(g):
    visited={}
    for vertex in g:
        if vertex not in visited:
            dfs(g,vertex,visited)

DFSTraversal(G)
#Modifying the function names for Graph representation using matrix
#---------------------DFS for Adjacency Matrix----------------------------------------
print('----------------------------DFS of Matrix Graph------------------------------------')
def dfs(g,vertex,visited):
    visited[vertex]=True
    print(vertex.GetId())
    for nbr in g.getNbr(vertex):
        if nbr not in visited:
            dfs(g,nbr,visited)

def DFSTraversal(g):
    visited={}
    for vertex in G1.Vertices:
        if vertex not in visited:
            dfs(g,vertex,visited)

DFSTraversal(G1)