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
     
    def get_weight(self):
        return self.weight
    
    def get_score(self):
        return self.__score
        

class Schedule:
    
    def __init__(self,jobs):
        
        self.jobs = []

        for job in jobs:
             self.jobs.append(Job(job))           
    
    def set_scores(self, option = 'diff'):
        
        for job in self.__jobs:
                job.set_score(option)
    
    def get_jobs (self):
        return self.jobs
    
    def set_schedule(self, option = 'diff'):
        self.set_scores(option)
        self.jobs = sorted(self.jobs, key=lambda a:a.score, reverse=True)  
        

            
    
    
        
        