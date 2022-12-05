import math
import random as r
import numpy as np
import matplotlib.pyplot as plt



# array of varierty of heights simulates a hill
hill = [127, 125, 122, 121, 119, 118, 121, 119, 121, 124, 126, 125, 127, 130, 130, 127, 124, 123,
 126, 125, 122, 121, 124, 124, 123, 121, 124, 125, 126, 127, 127, 127, 129, 128, 130, 132,
 133, 133, 130, 132, 134, 133, 131, 130, 131, 128, 129, 129, 128, 129, 128, 129, 126, 123,
 125, 127, 126, 129, 127, 125, 123, 123, 120, 123, 123, 125, 126, 125, 127, 128, 129, 128,
 126, 125, 126, 128, 125, 123, 121, 119, 121, 118, 120, 117, 118, 117, 119, 117, 119, 122,
 122, 122, 122, 123, 125, 126, 127, 124, 125, 122, 120, 122, 122, 121, 119, 116, 116, 115,
 113, 113, 116, 118, 120, 119, 122, 119, 117, 120, 122, 124, 123, 125, 128, 130, 132, 134,
 131, 129, 126, 123, 122, 120, 122, 124, 126, 124, 124, 121, 124, 124, 126, 125, 126, 129,
 132, 129, 132, 135, 136, 138, 137, 135, 136, 137, 139, 142, 140, 143, 143, 140, 143, 144,
 144, 147, 146, 146, 143, 143, 145, 145, 146, 149, 150, 149, 150, 148, 145, 147, 150, 147,
 145, 145, 143, 140, 138, 138, 137, 140, 143, 142, 142, 139, 137, 139, 140, 139, 136, 137,
 140, 137]
# the largest value in the the simulation 
greatest = 150


# method for simulated annealing
def SimulatedAnnealing(hill: list[int], temp : float, cooling_rate : float, objective: int,step_size : int) -> int:
    # sets the current solution to a random state
    current_solution = hill[r.randint(0,len(hill)-1)]
    # sets the best solution to the current solution to start with
    
    best_solution = current_solution
    
    #while temp is greater than 0
    while temp > 0:
        # If the objective was found return the current solution (Does not need to be given hoever use -1 if you want to not use this option)
        if(hill[current_solution] == objective):
            return current_solution

        #sets next to an index around the current best solution (at most 19 away)
        next = int(np.floor(best_solution + step_size*r.randint(0,len(hill)-1)))
        # if the generated number happens to be greater than 200 continue generating until valid index appears
        while(next >= len(hill) ):
            next = int(np.floor(best_solution + step_size*r.randint(0,len(hill)-1)))
            
            
        # calculate delta    
        delta = hill[next] -  hill[current_solution] 
        
        #if delta is greater than 0 that means its a better state and move to it
        if(delta > 0):
            current_solution = next
        #Else roll a number from 0-1 and if its less than e^delta/temp move to it
        else:
            if(r.random() <= np.exp(delta/temp)):
                current_solution = next
        #if the current solution is better then the current best solution set the best solution to the current solution
        if(hill[current_solution] > hill[best_solution]):
            best_solution = current_solution
        
        
        # decrease temp
        temp = temp - cooling_rate
    return current_solution    
        

#sets the solution to the index returned by the ai
solution = SimulatedAnnealing(hill,10,.1,greatest,.1)

#sets x to be of length 200
x = np.arange(0,len(hill)) 
#sets hill (or y) to be the heights specified in the array
hill = np.array(hill)
#sets titles and labels
plt.title("Hill")
plt.xlabel("Index")
plt.ylabel("Height")

#plots the graph
plt.plot(x,hill, color="blue")
# plt.fill(x,hill,color="blue")
#plots the solution determined by the AI
plt.plot(solution,hill[solution],color="red",marker="o")

#prints the solution and its neighbors
print(f"Solution: ({solution},{hill[solution]})\nNeighbors: ({solution-1},{hill[solution-1]}) and ({solution+1},{hill[solution+1]})")
#shows the graph
plt.show()






