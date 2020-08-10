#Author: Mariano Leonel Acosta
#Github: mlacosta
#mail: marianoacosta.003@gmail.com
#date: Aug 3rd 2020
#
#Implement a greedy algorithm for job scheduling
#

### HEADER ###
def loadJobs(name):
    
    with open(name) as file:
        data = file.readlines()
    
    data.pop(0) #remove irrelevant info
    
    data = list(map(lambda a : a.split(),data))
    
    return data


class Job:
    
    def __init__(self,job):
        
        self.weight = int(job[0])
        self.length = int(job[1])
        self.ctime = 0
        self.score = None
    
    def set_ctime(self,prevCt):
        self.__ctime = prevCt + self.__length
    
    def set_score(self, option = 'diff'):
        
        if option == 'diff':
            self.score = self.weight - self.length
        elif option == 'ratio':
            self.score = self.weight / self.length
        else:
            raise Exception("Not a valid option")
     

class Schedule:
    
    def __init__(self,jobs):
        
        self.jobs = []
        self.weightScore = 0

        for job in jobs:
             self.jobs.append(Job(job))           
    
    def set_scores(self, option = 'diff'):
        
        for job in self.jobs:
                job.set_score(option)
    
    def get_jobs (self):
        return self.jobs
    
    def set_schedule(self, option = 'diff'):
        self.set_scores(option)
        self.jobs = sorted(self.jobs, key=lambda a:a.score, reverse=True)  
        
        queue = []
        finalSchedule = []
        
        for job in self.jobs:
            if (len(queue) !=0):
                if (queue[-1].score != job.score):
                    queue = sorted(queue, key=lambda a:a.weight, reverse=True)  
                    finalSchedule += queue
                    queue = []
            
            queue.append(job)
            
        queue = sorted(queue, key=lambda a:a.weight, reverse=True) 
        finalSchedule += queue
        
        self.jobs = finalSchedule
        cumsum = []
        
        for inx in range(len(self.jobs)):
            if inx != 0:
                cumsum.append(cumsum[inx-1] + self.jobs[inx].length)
            
            else:
                cumsum.append(self.jobs[inx].length)
        
        for inx in range(len(self.jobs)):
            self.jobs[inx].ctime = cumsum[inx]
        
    
    def get_score(self):
        
        for job in self.jobs:
            self.weightScore += job.ctime*job.weight
            
        return self.weightScore
            

## IMPLEMENTATION ##
          
data = loadJobs('jobs.txt') #load jobs
sch = Schedule(data) 
sch.set_schedule(option = 'diff') #obtains an schedule using weight - length as score
print("The cumulative weighted score with (w - l) is: %d"%(sch.get_score()))


sch = Schedule(data)
sch.set_schedule(option = 'ratio')
print("The cumulative weighted score with (w / l) is: %d"%(sch.get_score())) 
    
    
        
        