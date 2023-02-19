import random
import math

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

# Get the minimum conflict of a given column
def findMin(enc, col):
  temp = enc.copy()
  config = []
  for i in range(len(enc)):
    temp[col] = i+1
    config.append(temp.copy())

  maxFit = fitness(max(config, key=fitness))
  maxList = []
  for i in config:
    if fitness(i) == maxFit:
      maxList.append(i)
  return random.choice(maxList)


# Main Algorithm:
# If settings = 1:
# 1. Iterate up to maxSteps
# 2. Check if the current encoding has a fitness of 28
# 2a. If yes, print the solution
# 3. Change encoding to the min conflict encoding by calling findMin function on a random column
# REPEAT!

# If settings = 2:
# 1. Iterate up to maxSteps
# 2. Check if the current encoding has a fitness of 28
# 2a. If yes, print the solution
# 3. Change encoding to the min conflict encoding by calling findMin function on a cyclical basis of column
# REPEAT!

def minConflict(enc, maxSteps, settings):
  col = 0
  for i in range(maxSteps):
    print('Encoding ' + (str)(i+1) + ':')
    print(enc)
    print('Fitness: ' + (str)(fitness(enc)))

    if(fitness(enc) == 28):
      print('\nSolutions Found!')
      solution = ''
      for i in enc:
        solution = solution + (str)(i)
      print(solution)
      return
    
    if(settings == 1): 
      enc = findMin(enc, random.choice(range(0,len(enc))))
    elif(settings == 2):
      enc = findMin(enc, col)
      col += 1 
      col = col % len(enc)

  print('\nNo Solutions Found With ' + (str)(i+1) + ' Iterations')
  

enc = randomRestart(8)
minConflict(enc, 10000, 2)
print(EVALS)
