from Queue import PriorityQueue
import numpy
class graph:
  edges = {}
  shortest_path = [[]]
  num_vertices = 0
  # init
  def __init__(self,num_vertices):
    self.shortest_path = numpy.zeros((num_vertices,num_vertices),dtype=int) 
    self.num_vertices = num_vertices
    for i in range(0, num_vertices):
      for j in range(0, num_vertices):
        self.shortest_path[i][j] = 999999 # a big number


  # insert values
  def insert(self, key, value):
    self.edges[key] = value
  # find shortest path 
  # Too Slow for sparse graph
  def plan(self):
    # print self.edges[(0,13)]
    for i in range(0, self.num_vertices):
      self.shortest_path[i][i] = 0
    for edge in self.edges:
      self.shortest_path[edge[0]][edge[1]] = self.edges[edge]
    for k in range(0, self.num_vertices):
      print "iteration" + str(k)
      for i in range(0, self.num_vertices):
        for j in range(0, self.num_vertices):
          if self.shortest_path[i][j] > self.shortest_path[i][k] + self.shortest_path[k][j]:
            self.shortest_path[i][j] = self.shortest_path[i][k] + self.shortest_path[k][j]
    # Then negative cycle
    shortest = self.shortest_path[0][0]
    for i in range(0, self.num_vertices):
      for j in range(0, self.num_vertices):
        if self.shortest_path[i][j] < shortest:
          shortest = self.shortest_path[i][j]
    print "shortest: " + str(shortest)
    for i in range(0, self.num_vertices):
      if self.shortest_path[i][i] < 0:
        print "Report: there is negative cycle!"

 



def main():
  graph_def = open('g3.txt','r')
  info = graph_def.readline().split(' ',1)
  num_vertices = int(info[0])
  num_edges= int(info[1])
  graph_sparse = graph(num_vertices)
  for line in graph_def:
    content = line.split(' ',2)
    graph_sparse.insert( (int(content[0]) - 1, int(content[1]) - 1), int(content[2]) )
  graph_def.close()
  graph_sparse.plan()


if __name__ == "__main__":
    main()
