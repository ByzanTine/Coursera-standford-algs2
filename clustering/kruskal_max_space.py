import numpy
import heapq
from Queue import PriorityQueue
class unionFind:
  container = []
  count = None
  # Initialize the data
  def __init__(self, size):
    for i in range(0, size):
      self.container.append(i)
    self.count = size
  def connected(self, i, j):
    return self.container[i] == self.container[j]
  # Replace the component i by j
  def union(self, i, j):
    if self.connected(i, j):
      pass
    else:
      pid = self.container[i]
      for k in range(0, len(self.container)):
        if self.container[k] == pid:
          self.container[k] = self.container[j]
      self.count -= 1


class KruskalPlan:
  edges = [[]]
  cluster = None
  edge_heap = PriorityQueue()
  def __init__(self,num_vertices):
    #Create a adjacent matrix to record edges
    self.edges = numpy.zeros((num_vertices,num_vertices),dtype=int) 
    #Init the cluster by union find data structure
    self.cluster = unionFind(num_vertices)

  def append(self, node1, node2, edge):
    self.edges[node1-1][node2-1] = edge
    self.edge_heap.put((edge, (node1-1, node2-1,edge))) 
  def plan(self):
    
    # For all vertices that are not in spanning tree
    # put edge into the heap
    while self.cluster.count > 3 and not self.edge_heap.empty():
      print "Cur cluster count " + str(self.cluster.count)

      #! Find the edge in the binary heap and ensure it's not a circle
      while not self.edge_heap.empty():
        heap_val = self.edge_heap.get()
        node1 =  int(heap_val[1][0])
        node2 =  int(heap_val[1][1])
        
        print heap_val[0]
	if self.cluster.connected(node1, node2):
          pass
        else:
          self.cluster.union(node1, node2)
          break
    # Print the final result
    
def main():
  edges_def = open('clustering1.txt','r')
  info = edges_def.readline().split(' ',1)
  kruskal_plan = KruskalPlan(int(info[0]))
  for line in edges_def:
    content = line.split(' ',2)
    # print content[0] + ' '+content[1]+' ' + content[2]
    kruskal_plan.append(int(content[0]),int(content[1]),int(content[2]))
  edges_def.close()
  kruskal_plan.plan()

if __name__ == "__main__":
    main()

