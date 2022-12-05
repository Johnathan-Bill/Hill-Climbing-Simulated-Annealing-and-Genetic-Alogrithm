import random
class Agent:
    value = -1
    lower = -1
    upper = -1
    def __init__(self,l:int,u:int):
        self.lower = l
        self.upper = u
        self.value = 0
    def generateValue(self):
       self.value = random.randint(self.lower,self.upper)
    def cross_over(self,other_parent: 'Agent') -> list[int]:
        bounds = []
        
        lower = int((self.lower + other_parent.lower)/2)
        upper = int((self.lower + other_parent.lower)/2)
        
        if(random.uniform(0,1) <=.01):
            lower += random.randint(-10000,10000)
        if(random.uniform(0,1) <=.01):
            upper += random.randint(-10000,10000)
        
        
        
        bounds.append(lower)
        bounds.append(upper)
        bounds.sort()
        
        return bounds
    def __repr__(self) -> str:
        return f"Upper: {self.upper}. Lower: {self.lower}. Value: {self.value}"