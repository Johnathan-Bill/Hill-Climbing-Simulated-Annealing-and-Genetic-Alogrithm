# Hill-Climbing-Simulated-Annealing-and-Genetic-Alogrithm

Assignment for my Intro to Artifical Intelligence Course (CS 472)
## Requirements ##
* Python 3
* numpy
* matplotlib


The purpose of these programs was to demostrate my understanding of 3 different algorithms used in AI:
* Hill Climbing
* Simulated Annealing 
* Basic Genetic Alogrithms

### Hill Climbing ###
The Hill Climbing alogrithm is a basic Algorithm in which that 'AI' will only climb the hill, generated using random [x,y] points on a graph. What this means is the 'AI'
will only attempt to go to higher points (in this implantation). Due to nature of the chosen data points it is common for the AI to never reach the largest point on the graph,
which is y = 150, instead getting stuck on local maximums in most cases.

### Simulated Annealing ###
The Simulated Annealing alogrithm tries to fix itself by instead of only going up generating a random point within a certain range of its current location and if the new
points is less lower than the current point give a small chance to move to said point. The way this is decided is by using a 'tempature' which will slowly decrease to 0. So
in the beginning it will have an increased chance of move to lower points but will continue to decrease this chance until the 'tempature' is 0.

### Basic Genetic Algorithm (INCOMPLETE) ###
For the genetic algorithm I decided to generate a random number from 0 to 100,000 and have the AI try to get as close to that value in its upper and lower bounds as possible.
Every generation will have the current agents generate a random number between its upper and lower bounds and those who generated values closest to the target value will be chosen
by the fitness function will be able to repopulate. The issue with this version of the code is that it does not take account the upper and lower bounds of the agents and solely
basis survival rates based on the random generated value which can cause issues if the number generated is too high for the agent to climb up to. Sometime in the future I wish
to update the genetic algorithm to take account the bounds of the agents in the fitness fuction so that it can more accurately get the target value.
