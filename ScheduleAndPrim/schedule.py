from Queue import PriorityQueue


class job:
  dif = 0
  ratio = 0.0
  weight = 0
  length = 0
  def __init__(self, weight, length):
    self.weight = weight
    self.length = length
    self.dif =  self.weight - self.length
    self.ratio = float(self.weight)/float(self.length)

class jobs:
  container = PriorityQueue()
  cur_time = 0
  weight_sum = 0
  def append(self, job):
    # self.container.put((-job.dif,-job.weight,job))
    self.container.put((-job.ratio,job))
  def schedule(self):
    '''Find the Highest val of diff'''
    while not self.container.empty():
    	cur_job = self.container.get()
        print str(cur_job[1].weight)+' '+str(cur_job[1].length)+' '+str(cur_job[1].ratio)
        self.cur_time = self.cur_time + cur_job[1].length
        self.weight_sum = self.weight_sum + cur_job[1].weight*self.cur_time
    print self.weight_sum

def main():
  jobs_def = open('jobs.txt','r')
  job_list = jobs()
  print jobs_def.readline()
  for line in jobs_def:
    content = line.split(' ',1)
    job_list.append( job(int(content[0]), int(content[1])) )
  jobs_def.close()
  job_list.schedule()


if __name__ == "__main__":
    main()
