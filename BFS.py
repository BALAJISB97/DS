from GraphImplementationUsingList import Graph
from GraphImplementationUsingAdjMatrix import G1
from Queue import Queue

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
#---------------------- BFS Traversal-------------------
visited = [] # List to keep track of visited nodes.
queue = Queue()     #Initialize a queue
def bfs(visited, graph, node):
  visited.append(node)
  queue.enqueue(node)

  while(not  queue.IsQEmpty()):
    s = queue.dequeue() 
    print (s.id, end = " ") 

    for neighbour in s.getConnections():
      if neighbour not in visited:
        visited.append(neighbour)
        queue.enqueue(neighbour)

# Driver Code
for vertices in G:
    if vertices not in visited:
        bfs(visited, G, vertices)
#--------------------BFS for adjaceny Matrix-------------
print('\n---------BFS for Matrix-----------------------------')
visited = [] # List to keep track of visited nodes.
queue = Queue()     #Initialize a queue
def bfs(visited, graph, node):
  visited.append(node)
  queue.enqueue(node)

  while(not  queue.IsQEmpty()):
    s = queue.dequeue() 
    print (s.id, end = " ") 

    for neighbour in  graph.getNbr(node):
      if neighbour not in visited:
        visited.append(neighbour)
        queue.enqueue(neighbour)

for vertices in G1.Vertices:
    if vertices not in visited:
        bfs(visited, G1, vertices)