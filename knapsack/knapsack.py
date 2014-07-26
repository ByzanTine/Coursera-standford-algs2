import copy
import numpy
from Queue import PriorityQueue
import bisect # sorted list
class KnapsackPlan:
  
  container = []
  knapsack_size = 0
  max_value = 0

  def __init__(self, size):
    # init the size 
    self.knapsack_size = size
  def append(self, node1, node2):
    # store the container val
    self.container.append((node1,node2))
  # Recursive Version
  # Too slow...
  def recur_plan(self, elements, size, cost):
    print str(len(elements)) + ' ' + str(size) +' ' +str(cost)
    if len(elements) is 0 or size is 0:
      if cost > self.max_value:
        self.max_value = cost
      return

    last = elements.pop()
    value = last[0]
    weight = last[1]
    
    if size >= weight:
      self.plan(copy.deepcopy(elements), size - weight, cost + value)
    
    self.plan(copy.deepcopy(elements), size, cost)
  # Dynamic Programming solution
  def dp_plan(self):

    matrix = numpy.zeros((len(self.container), self.knapsack_size+1),dtype=int)
    for i in range(0, len(self.container)):
      matrix[i][0] = 0

    for i in range(0, len(self.container)):
      for j in range(1, self.knapsack_size+1):

        value = self.container[i][0]
        weight = self.container[i][1]
        if j >= weight:
          matrix[i][j] = max(matrix[i-1][j - weight] + value, matrix[i-1][j])
        else:
          matrix[i][j] = matrix[i-1][j]

    # for i in range(0, len(self.container)):
    #   for j in range(0, self.knapsack_size+1):
    #     print matrix[i][j],
    #   print
    print matrix[len(self.container)-1][self.knapsack_size]
  # Works, but still not fast enough
  def dp_plan_one_dimension(self):
    vector = numpy.zeros(self.knapsack_size+1,dtype=int)
    vector[0] = 0 
    for i in range(0, len(self.container)):
      print str(i) + "th iteration"
      value = self.container[i][0]
      weight = self.container[i][1]
      for j in range(self.knapsack_size,-1,-1):
        if j >= weight:
          vector[j] = max(vector[j - weight] + value, vector[j])
        else:
          break
    print vector[self.knapsack_size]
  # Using Sparse column, used hash-map for easily implementation
  # A sorted list solution maybe better
  def dp_plan_sparse(self):
    column = {}
    column[0] = 0
    for i in range(0, len(self.container)):
      print str(i) + "th iteration"
      value = self.container[i][0]
      weight = self.container[i][1]
      # For each elements in colum(sparse)
      cur_colum = copy.deepcopy(column)
      for key in cur_colum:
        tmp_weight = key
        tmp_value = cur_colum[key]
        if tmp_weight + weight > self.knapsack_size:
          continue
        if cur_colum.get(tmp_weight + weight) is None:
          column[tmp_weight + weight] = tmp_value + value
        elif cur_colum[tmp_weight + weight] < tmp_value + value:
          column[tmp_weight + weight] = tmp_value + value


      # print len(cur_colum)
      # for ele in column:
      #   print "weight:" + str(ele) + ' val: ' + str(column[ele])
    for key in column:
      if column[key] > self.max_value:
        self.max_value = column[key]
    
      
    

    

def getKey(item):
    return item[1]    
def main():
  edges_def = open('knapsack_big.txt','r')
  info = edges_def.readline().split(' ',1)
  Knapsack_Plan = KnapsackPlan(int(info[0]))
  for line in edges_def:
    content = line.split(' ',1)
    # print content[0] + ' '+content[1]+' ' + content[2]
    Knapsack_Plan.append(int(content[0]),int(content[1]))
  edges_def.close()
  Knapsack_Plan.dp_plan_sparse();
  print Knapsack_Plan.max_value

if __name__ == "__main__":
    main()
