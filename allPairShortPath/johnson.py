from Queue import PriorityQueue
import numpy
class graph:
  edges = {}
  shortest_path = [[]]
  num_vertices = 0
  weight_update = []
  # init
  def __init__(self,num_vertices):
    
    self.num_vertices = num_vertices

  def add_empty_node(self):
    for i in range(0, self.num_vertices):
      self.edges[(self.num_vertices, i)] = 0

  # insert values
  def insert(self, key, value):
    self.edges[key] = value
  
  def bellford(self):
    source = self.num_vertices
    weight = []
    for i in range(0, self.num_vertices + 1):
      weight.append(999999)
    weight[self.num_vertices] = 0
    for i in range(1, self.num_vertices):
      for edge in self.edges:
        if self.edges[edge] + weight[edge[0]] < weight[edge[1]]:
          weight[edge[1]] = self.edges[edge] + weight[edge[0]]
    for edge in self.edges:
      if weight[edge[0]] + self.edges[edge] < weight[edge[1]]:
        print "ERROR: negative cycle!"

    self.weight_update = weight

  def updateWeight(self):
    for edge in self.edges:
      self.edges[edge] += self.weight_update[edge[0]] - self.weight_update[edge[1]]
      # print self.edges[edge]


  def dijkstra(self, source_vertex):
    dist = []
    edge_heap = PriorityQueue()
    for i in range(0, self.num_vertices):
      if i != source_vertex:
        dist.append[999999]
      else:
        dist.append[0]
      edge_heap.put(dist)
    
 



def main():
  # g1 g2 has negative cycle
  graph_def = open('g3.txt','r')
  info = graph_def.readline().split(' ',1)
  num_vertices = int(info[0])
  num_edges= int(info[1])
  graph_sparse = graph(num_vertices)
  
  for line in graph_def:
    content = line.split(' ',2)
    graph_sparse.insert( (int(content[0]) - 1, int(content[1]) - 1), int(content[2]) )
  graph_def.close()
  graph_sparse.add_empty_node()
  graph_sparse.bellford()
  graph_sparse.updateWeight()
  


if __name__ == "__main__":
    main()
