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
greatest = 150


# method to climb hill
def hill_climb(hill : list[int], n :int) -> int:
    
    # selects a random state
    current_state = r.randint(0,len(hill)-1)
    
    
    
    # while in range in n
    for _ in range(n) :
        
        #selects the random direction
        rand_direction = r.sample([-1,1],1)
        
        #if the current_state is 0 or len(hill)-1 only check the right or left of it respectively
        if(current_state == 0):
            if (hill[current_state] <= hill[current_state+1]):
                current_state = current_state+1
        elif(current_state == len(hill)-1):
                if (hill[current_state] <= hill[current_state-1]):
                    current_state = current_state-1
        
        #else check both sides of the state (the neighbors)
        else:
            #If the current state is less than or equal to the state to the right and greater or equal to then the state to the left move to the right
            if(hill[current_state] <= hill[current_state+1] and hill[current_state] >= hill[current_state-1]):
                current_state = current_state+1
            # if the current state is greater than or equal to the state to the right and less or equal to then the state to the left move to the left
            elif(hill[current_state] >= hill[current_state+1] and hill[current_state] <= hill[current_state-1]):
                current_state = current_state -1
            #if both neightboring states are greater than or equal to the current state move in a random direction
            elif(hill[current_state] <= hill[current_state+1] and hill[current_state] <= hill[current_state-1]):
                current_state = current_state + rand_direction[0]
        # print(f"Solution: ({current_state},{hill[current_state]})")        
        
        
    return current_state
    





# for i in range(199):
#     n = r.randint(n-3,n+3)
#     hill.append(n)
#     if(n >= greatest): greatest = n



solution = hill_climb(hill,100)

x = np.arange(0,len(hill)) 
hill = np.array(hill)
plt.title("Hill")
plt.xlabel("Index")
plt.ylabel("Height")
plt.plot(x,hill, color="blue")
plt.plot(solution,hill[solution],color="red",marker="o")

print(f"Solution: ({solution},{hill[solution]})\nNeighbors: ({solution-1},{hill[solution-1]}) and ({solution+1},{hill[solution+1]})")

plt.show()


    
# print(f"hill = {hill}")
# print(f"greatest = {greatest}")


