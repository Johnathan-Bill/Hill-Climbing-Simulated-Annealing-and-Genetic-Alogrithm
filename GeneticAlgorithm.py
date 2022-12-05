from agent import Agent
import numpy as np
import random as r
import matplotlib.pyplot as plt
# determines the best candiates for repopulation
def fitness_function(population: list[Agent], goal : int) -> list[Agent]:
    
    top_agents = []
    values = []
    #subtracts all values by the goal to determine the distance from gaol
    temp_population = population.copy()
    for x in population:
        values.append(abs(x.value - goal))
    values = np.asarray(values)
 # picks the top 499 agents (smallest values)
    while len(top_agents) < 499:
        index = values.argmin()
        top_agents.append(temp_population.pop(index))
        values = np.delete(values,[index])
    return(top_agents)
       
def genetics(population : list[Agent],goal: int, n:int) -> list:
        averages = []
        numOfAgents = len(population)
        # runs for n generations
        for _ in range(n):
            avg = 0
            # generates values for each agent and finds the average of this generations
            for a in population:
                a.generateValue()
                avg += a.value
            averages.append(avg/len(population))
            #finds the best agents in this generations         
            best = fitness_function(population, goal)
            # generates the new population
            new_population = []
            while len(new_population) < numOfAgents:
                parent_1 = r.randint(0,len(best)-1)
                parent_2 = r.randint(0,len(best)-1)
                while parent_2 == parent_1:
                    parent_1 = r.randint(0,len(best)-1)
                    
                bounds = best[parent_1].cross_over(best[parent_2])
                new_population.append(Agent(bounds[0],bounds[1]))
            population = new_population
        # one final generation of values
        for a in population:
                a.generateValue()
        #returns the best agent and the averages
        return [min(population, key =lambda x:abs(goal-x.value)),averages]
    
    
# generates the starting generation         
def generate_starter_population(n : int) -> list[Agent]:
    population = []
    for _ in range(n):
        bounds = []
        bounds.append(r.randint(1,100000))
        bounds.append(r.randint(1,100000))
        bounds.sort()
        population.append(Agent(bounds[0],bounds[1]))
    return population

goal = r.randint(0,100000)
# goal = 93232
generations = 3000
goal_set = []

for i in range(generations):
    goal_set.append(goal)

results = genetics(generate_starter_population(1000),goal,generations)
print(f"{results[0]}\nGoal : {goal}")
plt.plot(np.arange(0,generations),results[1], color="blue")
plt.plot(np.arange(0,generations),goal_set,color="red", linestyle = 'dashed')
plt.show()