'''Prim Algorithm with input edge.txt'''
import numpy
import heapq
from Queue import PriorityQueue
class PrimPlan:
  vertices = []
  edges = [[]]
  
  edge_heap = PriorityQueue()
  def __init__(self,num_vertices):
    #Create a adjacent matrix to record edges
    self.edges = numpy.zeros((num_vertices,num_vertices),dtype=int) 
    #Create a vertex array to record if the vertex is used
    self.vertices = numpy.zeros(num_vertices, dtype=int)

  def append(self, node1, node2, edge):
    self.edges[node1-1][node2-1] = edge
  
  def plan(self):
    # For all vertices that are not in spanning tree
    # put edge into the heap
    self.vertices[0] = 1
    cur_vertices = 0
    total_cost = 0
    while int(sum(self.vertices)) < len(self.vertices):
      print "Cur vertices: " + str(sum(self.vertices))

      for i in xrange(0,len(self.vertices)):
        
        if (int(self.vertices[i]) is 0 and 
          int(self.edges[cur_vertices][i]) is not 0):
          self.edge_heap.put((self.edges[cur_vertices][i], (cur_vertices,i))) 
        if (int(self.vertices[i]) is 0 and 
          int(self.edges[i][cur_vertices]) is not 0):
          self.edge_heap.put((self.edges[i][cur_vertices], (cur_vertices,i))) 
      # print "Cur Heapsize: " + str(self.edge_heap.qsize())
      # if int(self.edge_heap.qsize()) is 0:
      #   break

      #! Find the edge in the binary heap and ensure it's not a circle
      while not self.edge_heap.empty():
        heap_val = self.edge_heap.get()
        

        if (int(self.vertices[heap_val[1][0]]) is 1 and
         int(self.vertices[heap_val[1][1]]) is 0):
          total_cost += heap_val[0]
          self.vertices[heap_val[1][1]] = 1
          print "Edge choosed " + str(heap_val[1][0]) +' '+ str(heap_val[1][1])
          cur_vertices = heap_val[1][1]
          break
        print "jumped"
    # Print the final result
    print total_cost

def main():
  edges_def = open('edges.txt','r')
  info = edges_def.readline().split(' ',1)
  prim_plan = PrimPlan(int(info[0]))
  for line in edges_def:
    content = line.split(' ',2)
    print content[0] + ' '+content[1]+' ' + content[2]
    prim_plan.append(int(content[0]),int(content[1]),int(content[2]))
  edges_def.close()
  prim_plan.plan()

if __name__ == "__main__":
    main()

