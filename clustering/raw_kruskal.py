''' Handling Raw data by a hacking approach for clustering'''
class unionFind:
  container = []
  sz = []
  count = None
  # Initialize the data
  def __init__(self, size):
    for i in range(0, size):
      self.container.append(i)
      self.sz.append(i)
    self.count = size
  def connected(self, i, j):
    return self.find[i] == self.find[j]
  def find(self, p):
    while p is not self.container[p]:
      p = self.container[p];
    return p
  # Replace the component i by j
  def union(self, i, j):
    rootI = self.find(i)
    rootJ = self.find(j)
    if rootI == rootJ:
      pass
    else:
      if self.sz[rootI] < self.sz[rootJ] :
        self.container[rootI] = rootJ
        self.sz[rootJ] += self.sz[rootI]
      else:
        self.container[rootJ] = rootI
        self.sz[rootI] += self.sz[rootJ]
      self.count -= 1
         

def line2dec(content):
  num = 0
  for i in range(0, 24):
    num += int(content[i])
    num *= 2
  # divide by 2 since the final step should not mutiply 2
  return num/2
    
def main():
  
  edges_def = open('clustering_big.txt','r')
  info = edges_def.readline().split(' ')
  union_data = unionFind(int(info[0]))
  code_len = int(info[1])
  node_info = {} 
  k = 0
  for line in edges_def:
    if node_info.get(line2dec(line.split(' '))) is None:
      node_info[line2dec(line.split(' '))] = k
      k += 1
    else:
      union_data.count -= 1
  edges_def.close()
  edges_def = open('clustering_big.txt','r')
  edges_def.readline()
  for line in edges_def:
    content = line.split(' ')
    cur_index = node_info[line2dec(content)]
    print 'processing line ' + str(cur_index)
    print 'Progress: ' + str(float(cur_index)/float(info[0]))
    # First handle the hamming distance of 1
    for i in range(0, code_len):
      content[i] = (int(content[i]) is not 1)
      change_index = line2dec(content)
      if node_info.get(change_index) is not None:
        #Connect
        union_data.union(node_info[change_index], cur_index) 
      content[i] = (int(content[i]) is not 1)
    # Then for the hamming distance of 2
    for i in range(0, code_len):
      content[i] = (int(content[i]) is not 1)
      for j in range(i+1, code_len):
        content[j] = (int(content[j]) is not 1)
        
        if node_info.get(line2dec(content)) is not None:
          
          union_data.union(node_info[line2dec(content)], cur_index) 
        content[j] = (int(content[j]) is not 1)
      
      content[i] = (int(content[i]) is not 1)
    # Query the nearby 300 nodes if exist, then union
  print 'Final Cluster Count: '+ str(union_data.count)
  edges_def.close()

if __name__ == "__main__":
    main()

