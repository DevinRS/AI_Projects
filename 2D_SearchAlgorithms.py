class gridWorld:
    def __init__(self, inputArray) -> None:
        self.obs = inputArray
        self.sizeRow = len(inputArray)
        self.sizeCol = len(inputArray[0])

    def printArr(self):
        for i in self.obs:
            print(i)

    def traceback(self, arr, start: tuple, goal: tuple):
        solution = [[0]*self.sizeCol for _ in range(self.sizeRow)]
        currCoords = goal
        while(currCoords != start):
            currValue = arr[currCoords[0]][currCoords[1]]
            solution[currCoords[0]][currCoords[1]] = 1
            nextValue = []

            if(currCoords[1]-1>=0 and arr[currCoords[0]][currCoords[1]-1] != 0 and arr[currCoords[0]][currCoords[1]-1] < currValue):
                nextValue.append(arr[currCoords[0]][currCoords[1]-1])
            else:
                nextValue.append(10000)

            if(currCoords[0]-1>=0 and arr[currCoords[0]-1][currCoords[1]] != 0 and arr[currCoords[0]-1][currCoords[1]] < currValue):
                nextValue.append(arr[currCoords[0]-1][currCoords[1]])
            else:
                nextValue.append(10000)

            if(currCoords[1]+1<self.sizeCol and arr[currCoords[0]][currCoords[1]+1] != 0 and arr[currCoords[0]][currCoords[1]+1] < currValue):
                nextValue.append(arr[currCoords[0]][currCoords[1]+1])
            else:
                nextValue.append(10000)
                
            if(currCoords[0]+1<self.sizeRow and arr[currCoords[0]+1][currCoords[1]] != 0 and arr[currCoords[0]+1][currCoords[1]] < currValue):
                nextValue.append(arr[currCoords[0]+1][currCoords[1]])
            else:
                nextValue.append(10000)
                

            lowest = min(nextValue)
            index = nextValue.index(lowest)

            if(index == 0):
                newCoords = [currCoords[0], currCoords[1]-1]
            elif(index == 1):
                newCoords = [currCoords[0]-1, currCoords[1]]
            elif(index == 2):
                newCoords = [currCoords[0], currCoords[1]+1]
            elif(index == 3):
                newCoords = [currCoords[0]+1, currCoords[1]]
 
            currCoords = newCoords
            
        solution[currCoords[0]][currCoords[1]] = 1
        cost = 0
        for i in solution:
            print(i)
            cost += i.count(1)
        print("Cost: " + (str)(cost))
        return

    def BFS(self, start: tuple, goal: tuple):
        print("\n------------- BFS -------------")
        # PRINT OBSTACLE ARRAY
        print("Obstacle Array: ")
        self.printArr()
        print()

        # INITIALIZED VISITED ARRAY AND COORDINATE QUEUE
        visited = [[0]*self.sizeCol for _ in range(self.sizeRow)]
        queue = []
        path = [[0]*self.sizeCol for _ in range(self.sizeRow)]

        # APPEND THE START TO QUEUE
        queue.append(start)

        # CHECK IF START IS ALREADY AT GOAL
        if(start == goal):
            print("Already at Goal!")
            print("No traversal done!")
            return
        # CHECK IF START IS AT AN OBSTACLE (INVALID START)
        elif(self.obs[start[0]][start[1]] == 1):
            print("Invalid Start Location!")
            return

        visited[start[0]][start[1]] = 1
        count = 1
        print("Traversal:")
        while(queue):
            currRow = queue[0][0]
            currCol = queue[0][1]

            queue.pop(0)
            print([currRow, currCol])
            path[currRow][currCol] = count
            count += 1

            # CHECK SOLUTION CONDITION
            if(currRow == goal[0] and currCol == goal[1]):
                print("\nTraversal Order: ")
                for i in path:
                    print(i)
                print("Solutions Found!")
                print("Found After " + (str)(count-2) + " Steps")
                print("\nShortest Path: ")
                self.traceback(path, start, goal)
                reached = 0
                for i in visited:
                    reached += i.count(1)
                print("\nReached: " + (str)(reached))
                return

            # MOVE LEFT
            if((currCol-1>=0) and (visited[currRow][currCol-1]==0) and (self.obs[currRow][currCol-1]==0)):
                queue.append([currRow,currCol-1])
                visited[currRow][currCol-1] = 1
            # MOVE UP
            if((currRow-1>=0) and (visited[currRow-1][currCol]==0) and (self.obs[currRow-1][currCol]==0)):
                queue.append([currRow-1,currCol])
                visited[currRow-1][currCol] = 1
            # MOVE RIGHT
            if((currCol+1<self.sizeCol) and (visited[currRow][currCol+1]==0) and (self.obs[currRow][currCol+1]==0)):
                queue.append([currRow,currCol+1])
                visited[currRow][currCol+1] = 1
            # MOVE DOWN
            if((currRow+1<self.sizeRow) and (visited[currRow+1][currCol]==0) and (self.obs[currRow+1][currCol]==0)):
                queue.append([currRow+1,currCol])
                visited[currRow+1][currCol] = 1

        # EXHAUSTED QUEUE, NO SOLUTIONS FOUND
        print("\nTraversal Order: ")
        for i in path:
            print(i)
        print("No Solutions Found!")


    def GBFS(self, start: tuple, goal: tuple):
        print("\n------------- GBFS -------------")
        # PRINT OBSTACLE ARRAY
        print("Obstacle Array: ")
        self.printArr()
        print()

        # INITIALIZED VISITED ARRAY, COORDINATE QUEUE, AND HEURISTIC ARRAY
        visited = [[0]*self.sizeCol for _ in range(self.sizeRow)]
        queue = []
        heuristic = []
        path = [[0]*self.sizeCol for _ in range(self.sizeRow)]

        # APPEND THE START TO QUEUE
        queue.append(start)
        heuristic.append(abs(start[0]-goal[0])+abs(start[1]-goal[1]))

        # CHECK IF START IS ALREADY AT GOAL
        if(start == goal):
            print("Already at Goal!")
            print("No traversal done!")
            return
        # CHECK IF START IS AT AN OBSTACLE (INVALID START)
        elif(self.obs[start[0]][start[1]] == 1):
            print("Invalid Start Location!")
            return

        visited[start[0]][start[1]] = 1
        count = 1
        print("Traversal:")
        while(queue):
            # CHECK LOWEST HEURISTIC
            lowestScore = min(heuristic)
            index = heuristic.index(lowestScore)

            currRow = queue[index][0]
            currCol = queue[index][1]

            queue.pop(index)
            heuristic.pop(index)
            print([currRow, currCol]) 
            path[currRow][currCol] = count
            count += 1

            # CHECK SOLUTION CONDITION
            if(currRow == goal[0] and currCol == goal[1]):
                print("\nTraversal Order: ")
                for i in path:
                    print(i)
                print("Solutions Found!")
                print("Found After " + (str)(count-2) + " Steps")
                print("\nShortest Path: ")
                self.traceback(path, start, goal)
                reached = 0
                for i in visited:
                    reached += i.count(1)
                print("\nReached: " + (str)(reached))
                return

            # MOVE LEFT
            if((currCol-1>=0) and (visited[currRow][currCol-1]==0) and (self.obs[currRow][currCol-1]==0)):
                queue.append([currRow,currCol-1])
                heuristic.append(abs(currRow-goal[0])+abs(currCol-1-goal[1]))
                visited[currRow][currCol-1] = 1
            # MOVE UP
            if((currRow-1>=0) and (visited[currRow-1][currCol]==0) and (self.obs[currRow-1][currCol]==0)):
                queue.append([currRow-1,currCol])
                heuristic.append(abs(currRow-1-goal[0])+abs(currCol-goal[1]))
                visited[currRow-1][currCol] = 1
            # MOVE RIGHT
            if((currCol+1<self.sizeCol) and (visited[currRow][currCol+1]==0) and (self.obs[currRow][currCol+1]==0)):
                queue.append([currRow,currCol+1])
                heuristic.append(abs(currRow-goal[0])+abs(currCol+1-goal[1]))
                visited[currRow][currCol+1] = 1
            # MOVE DOWN
            if((currRow+1<self.sizeRow) and (visited[currRow+1][currCol]==0) and (self.obs[currRow+1][currCol]==0)):
                queue.append([currRow+1,currCol])
                heuristic.append(abs(currRow+1-goal[0])+abs(currCol-goal[1]))
                visited[currRow+1][currCol] = 1

        # EXHAUSTED QUEUE, NO SOLUTIONS FOUND
        print("\nTraversal Order: ")
        for i in path:
            print(i)
        print("No Solutions Found!")


    def Astar(self, start: tuple, goal: tuple):
        print("\n------------- A* -------------")
        # PRINT OBSTACLE ARRAY
        print("Obstacle Array: ")
        self.printArr()
        print()

        # INITIALIZED VISITED ARRAY, COORDINATE QUEUE, AND HEURISTIC ARRAY
        visited = [[0]*self.sizeCol for _ in range(self.sizeRow)]
        queue = []
        heuristic = []
        path = [[0]*self.sizeCol for _ in range(self.sizeRow)]

        # APPEND THE START TO QUEUE
        queue.append(start)
        # Heuristic = g(n) + h(n) (distance from start + distance from goal)
        heuristic.append((abs(start[0]-start[0])+abs(start[1]-start[1]))+(abs(start[0]-goal[0])+abs(start[1]-goal[1])))

        # CHECK IF START IS ALREADY AT GOAL
        if(start == goal):
            print("Already at Goal!")
            print("No traversal done!")
            return
        # CHECK IF START IS AT AN OBSTACLE (INVALID START)
        elif(self.obs[start[0]][start[1]] == 1):
            print("Invalid Start Location!")
            return

        visited[start[0]][start[1]] = 1
        count = 1
        print("Traversal:")
        while(queue):
            # CHECK LOWEST HEURISTIC
            lowestScore = min(heuristic)
            index = heuristic.index(lowestScore)

            currRow = queue[index][0]
            currCol = queue[index][1]

            queue.pop(index)
            heuristic.pop(index)
            print([currRow, currCol]) 
            path[currRow][currCol] = count
            count += 1

            # CHECK SOLUTION CONDITION
            if(currRow == goal[0] and currCol == goal[1]):
                print("\nTraversal Order: ")
                for i in path:
                    print(i)
                print("Solutions Found!")
                print("Found After " + (str)(count-2) + " Steps")
                print("\nShortest Path: ")
                self.traceback(path, start, goal)
                reached = 0
                for i in visited:
                    reached += i.count(1)
                print("\nReached: " + (str)(reached))
                return

            # MOVE LEFT
            if((currCol-1>=0) and (visited[currRow][currCol-1]==0) and (self.obs[currRow][currCol-1]==0)):
                queue.append([currRow,currCol-1])
                heuristic.append((abs(currRow-start[0])+abs(currCol-1-start[1]))+(abs(currRow-goal[0])+abs(currCol-1-goal[1])))
                visited[currRow][currCol-1] = 1
            # MOVE UP
            if((currRow-1>=0) and (visited[currRow-1][currCol]==0) and (self.obs[currRow-1][currCol]==0)):
                queue.append([currRow-1,currCol])
                heuristic.append((abs(currRow-1-start[0])+abs(currCol-start[1]))+(abs(currRow-1-goal[0])+abs(currCol-goal[1])))
                visited[currRow-1][currCol] = 1
            # MOVE RIGHT
            if((currCol+1<self.sizeCol) and (visited[currRow][currCol+1]==0) and (self.obs[currRow][currCol+1]==0)):
                queue.append([currRow,currCol+1])
                heuristic.append((abs(currRow-start[0])+abs(currCol+1-start[1]))+(abs(currRow-goal[0])+abs(currCol+1-goal[1])))
                visited[currRow][currCol+1] = 1
            # MOVE DOWN
            if((currRow+1<self.sizeRow) and (visited[currRow+1][currCol]==0) and (self.obs[currRow+1][currCol]==0)):
                queue.append([currRow+1,currCol])
                heuristic.append((abs(currRow+1-start[0])+abs(currCol-start[1]))+(abs(currRow+1-goal[0])+abs(currCol-goal[1])))
                visited[currRow+1][currCol] = 1

        # EXHAUSTED QUEUE, NO SOLUTIONS FOUND
        print("\nTraversal Order: ")
        for i in path:
            print(i)
        print("No Solutions Found!")  


obs = [[0]*100 for _ in range(100)]
for i in range(100):
    for j in range(100):
        if i < 50:
            d = abs(i-51) + abs(j-50)
            if d == 50:
                obs[i][j] = 1
        else:
            if j > 50:
                d = abs(i-50) + abs(j-75)
                if d == 24:
                    obs[i][j] = 1
            elif j < 50:
                d = abs(i-50) + abs(j-25)
                if d == 24:
                    obs[i][j] = 1

arr = [
    [0,0,0,0,0,0,0,0],
    [0,0,1,1,1,1,0,0],
    [0,0,0,0,0,1,0,0],
    [0,0,0,0,0,1,0,0],
    [0,0,0,0,0,1,0,0],
    [0,0,0,0,0,1,0,0],
    [0,0,0,0,0,1,0,0]
]

grid = gridWorld(obs)
grid.GBFS([75,70], [50,55])
