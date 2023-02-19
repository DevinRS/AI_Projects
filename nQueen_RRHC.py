import random
import math
import matplotlib.pyplot as plt

EVALS = 0

def metrop(dE, T):
  r=random()
  return (dE>0) or (r<math.exp(dE/T))

# returns 1 if queens q1 and q2 are attacking each other, 0 o.w.
def attacking(q1col, q1row, q2col, q2row):
  if q1col==q2col:
    return 1  # same column
  if q1row==q2row:
    return 1  # same row
  coldiff=q1col-q2col
  rowdiff=q1row-q2row
  if abs(coldiff)==abs(rowdiff):
    return 1  # same diagonal
  return 0 

# evaluates the fitness of an encoding, defined as the number of
# non-attacking pairs of queens (28 - number of attacking pairs)
#
# the global variable EVALS keeps track of the number of times called
def fitness(encoding):
  global EVALS
  EVALS += 1
  E = 28
  for i in range(1,8):
    for j in range(i+1,9):
      E -= attacking(i, encoding[i-1], j, encoding[j-1])
  return E

# Get random starting position
def randomRestart(N):
  enc = []
  for i in range(N):
      enc.append(random.randint(1,N))
  return enc

# main loop
# 1. Iterate through neighbour and search for best fitness
# 2a. If the fitness of the best neighbour is 28, break the for loop and print the solutions found
# 2b. If the fitness of the best neighbour is more than the fitness of the current config, replace the current config to the neighbour
# 2c. If the fitness of the best neighbour is less than or equal to the fitness of the current config, random restart with random board config
# Repeat
def RRHC(N: int):
  # Initial Starting Config
  enc = randomRestart(N)

  # Utility Variables
  counter = 0
  fitnessArr = []
  x = []

  # Main Iterating Loop
  while(1):
    best = enc.copy()
    temp = enc.copy()
    # 1. Find best neighbour
    for i in range(len(best)):
      for j in range(len(best)):
        val = enc[i]
        temp[i] = j+1
        print('Fitness Evaluation ' + (str)(counter) + ':')
        print(temp)
        print('Fitness = ' + (str)(fitness(temp)))
        counter += 1
        # 2a.
        if(fitness(temp) == 28):
          print('Solutions Found: ')
          print(temp)
          fitnessArr.append(28)
          for i in range(len(fitnessArr)):
            x.append(i)

          plt.scatter(x, fitnessArr)
          plt.title('Maximums In Each Local Search')
          #plt.show()
          return
        elif(fitness(temp) > fitness(best)):
          best = temp.copy()
      temp[i] = val

    # 2b.
    if(fitness(best) > fitness(enc)):
      fitnessArr.append(fitness(best))
      enc = best
    # 2c.
    else:
      enc = randomRestart(N)


RRHC(8)
print(EVALS)