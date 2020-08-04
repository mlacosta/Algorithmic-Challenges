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
        
        self.__weight = int(job[0])
        self.__length = int(job[1])
        self.__ctime = 0
        self.__score = None
    
    def set_ctime(self,prevCt):
        self.__ctime = prevCt + self.__length
    
    def set_score(self, option = 'diff'):
        
        if option == 'diff':
            self.__score = self.__weight - self.__length
        elif option == 'ratio':
            self.__score = self.__weight / self.__length
        else:
            raise Exception("Not a valid option")
     
    def get_weight(self):
        return self.__weight
    
    def get_score(self):
        return self.__score
        
    def __lt__(self, other):
      self.__score < other.__score
    def __le__(self, other):
      self.__score <= other.__score
    def __eq__(self, other):
      self.__score == other.__score
    def __ne__(self, other):
      self.__score != other.__score
    def __gt__(self, other):
      self.__score > other.__score
    def __ge__(self, other):
      self.__score >= other.__score


class Schedule:
    
    def __init__(self,jobs):
        
        self.__jobs = []

        for job in jobs:
             self.__jobs.append(Job(job))           
    
    def set_scores(self, option = 'diff'):
        
        for job in self.__jobs:
                job.set_score(option)
    
    def get_jobs (self):
        return self.__jobs
    
    def set_schedule(self, option = 'diff'):
        self.set_scores(option)
        self.__jobs.sort(reverse = True)
        
        inx = 0
        
        while (inx<len(self.__jobs)):
            queue = [self.__jobs[inx]]
            
            innerInx = inx + 1;
            
            while (self.__jobs[innerInx].get_score == self.__jobs[inx].get_score):
                pass
            
            
    
    
        
        