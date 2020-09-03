
from GraphImplementationUsingList import Graph,vertex

# ------------- GRAPH INITIALIZATION------------------------------
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