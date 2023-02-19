import random
import math
import matplotlib.pyplot as plt
import numpy as np

# FITNESS FUNCTION
def fitness(x):
    return 4 + 2*x + 2*math.sin(20*x) - 4*x**2

# WEIGHTED INDEX ROULETTE SELECTOR
def getSelectionIndex(weights):
    elements = list(range(len(weights)))
    return random.choices(elements, weights=weights, k=1)[0]

# CREATE GENERATION 0 AND PROBABILITY ARRAY
N = 10
gen = []
prob = []
epsilon = 0.01

for i in range(N):
    gen.append(random.choice(np.round_(np.linspace(0,1,100), decimals=2))) # INDIVIDUAL SATISFYING 0.01*k, k=0..100

totalFitness = sum(map(fitness, gen))
print(gen)
print(totalFitness)

for i in gen:
    prob.append(fitness(i)/totalFitness)

# PRINT GENERATION 0
print('\nGeneration 0:')
print(gen)
print('Current Total Fitness: ' + (str)(totalFitness))
print('Current Maximum Fitness: ' + (str)(fitness(max(gen, key=fitness))))

# Generation0 Graph Plot Points
x2 = gen
y2 = []
b = []
for i in gen:
    y2.append(fitness(i))

# RUN EVOLUTION!
individual = []
for j in range(1000):
    newGen = []
    newProb = []
    # Iterate through gen array:
    # 1. Select index r using the prob array
    # 2. If the fitness is higher or equal than the selected fitness, do slight change (+- epsilon) or keep the same
    # 3. Append the new x-value to the newGen array
    for i in gen:
        r = getSelectionIndex(prob)
        x = 0
        if(fitness(i) >= fitness(gen[r])): # FITNESS COMPARISON
            temp = random.uniform(0,1)
            if temp < 0.3:
                x = i - epsilon
                if(x < 0): # ADJUSTMENT
                    x = 0
            elif temp < 0.6:
                x = i + epsilon
                if(x > 1): # ADJUSTMENT
                    x = 1
            else:
                x = i
        else:
            x = random.choice(np.round_(np.linspace(0,1,100), decimals=2))

        newGen.append(round(x, 2))

    # Iterate through newGen array:
    # 1. Append new probability into newProb array for roulette selection
    totalFitness = sum(map(fitness, newGen))
    for i in newGen:
        newProb.append(fitness(i)/totalFitness)
    
    # Print Generation individuals, Total Fitness, and Current Maximum Fitness
    print('\nGeneration' + (str)(j+1) + ':')
    print(newGen)
    print('Current Total Fitness: ' + (str)(totalFitness))
    print('Current Maximum Fitness: ' + (str)(fitness(max(newGen, key=fitness))))

    # Update gen and prob array for next iteration
    gen = newGen
    prob = newProb

    # Graphing best individual
    b.append(fitness(max(newGen, key=fitness)))
    individual.append(max(newGen, key=fitness))
    x3 = gen
    y3 = []
    for i in gen:
        y3.append(fitness(i))

# Print the Maximum after running the algorithm
print('Maximum Found: ' + (str)(max(b)) + ', At X = ' + (str)(max(individual, key=fitness)))

# GRAPH 1
plt.figure(1)
x1=[]
y1 = []
for i in np.linspace(0,1,100):
    x1.append(i)

for i in range(len(x1)):
    y1.append(fitness(x1[i]))

plt.plot(x1, y1)
plt.scatter(x2, y2, color='green')
plt.scatter(x3, y3, color='red')
plt.xlabel('x') 
plt.ylabel('y')
plt.title('Generation 0 (Green) vs Generation 1000 (Red)')

# GRAPH 2
plt.figure(2)
a = []
for i in range(1000):
    a.append(i)

plt.scatter(a,b)
plt.xlabel('Generation') 
plt.ylabel('Best Individual')
plt.title('Graph 2')
plt.show()
