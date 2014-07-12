'''Prim Algorithm with input edge.txt'''
import numpy
import heapq
class PrimPlan:
  vertices = []
  edges = [[]]
  cur_vertices = []
  edge_heap = []
  def __init__(self,num_vertices):
    #Create a adjacent matrix to record edges
    self.edges = numpy.zeros((num_vertices,num_vertices)) 
    #Create a vertex array to record if the vertex is used
    self.vertices = numpy.zeros(num_vertices)
  def append(self, node1, node2, edge):
    self.edges[node1-1][node2-1] = edge
  
  def plan(self):
    heapq.heappush(self.edge_heap, 5)
    heapq.heappush(self.edge_heap, 3)
    heapq.heappush(self.edge_heap, 2)
    heapq.heappush(self.edge_heap, 4)
    print heapq.heappop(self.edge_heap)

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

