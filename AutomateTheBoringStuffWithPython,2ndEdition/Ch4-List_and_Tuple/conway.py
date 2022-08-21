# Conway's Game of Life
import random, time, copy
import sys

WIDTH = 5
HEIGHT = 5

# Create a list of list for the cells:
nextCells = []
for x in range(WIDTH):
    column = [] # Create a new column.
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append('#')  # Adding a living cell.
        else:
            column.append(' ') # Add a dead cell.
    nextCells.append(column)    # nextCells is a list of column lists.

try:
    while True: # Main program loop.
        print('\n\n\n\n\n') # Separate each step with newlines.
        currentCells = copy.deepcopy(nextCells)
        aliveCells = 0

        # Print currentCells on the screen:
        for y in range(HEIGHT):
            for x in range(WIDTH):
                print(currentCells[x][y], end='')   # Print the # or space
            print() # Print a new line at the end of the row.

        # Calculate the next step's cells based on current step's cells
        for x in range(WIDTH):
            for y in range(HEIGHT):
                # Get neighboring coordinates:
                # '% WIDTH' ensures leftCoord is always between 0 and WIDTH - 1
                leftCoord = (x - 1) % WIDTH
                rightCoord = (x + 1) % WIDTH
                aboveCoord = (y - 1) % HEIGHT
                belowCoord = (y + 1) % HEIGHT

                # Count number of living neighbors:
                numNeighbors = 0
                if currentCells[leftCoord][aboveCoord] == '#':
                    numNeighbors += 1
                if currentCells[x][aboveCoord] == '#':
                    numNeighbors += 1
                if currentCells[rightCoord][aboveCoord] == '#':
                    numNeighbors += 1
                if currentCells[leftCoord][y] == '#':
                    numNeighbors += 1
                if currentCells[rightCoord][y] == '#':
                    numNeighbors += 1
                if currentCells[leftCoord][belowCoord] == '#':
                    numNeighbors += 1
                if currentCells[x][belowCoord] == '#':
                    numNeighbors += 1
                if currentCells[rightCoord][belowCoord] == '#':
                    numNeighbors += 1
                if currentCells[x][y] == '#':
                    aliveCells += 1

                # Set cell based on Conway's Game of Life rules:
                if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                    # Living cells with 2 or 3 neighbors stay alive
                    nextCells[x][y] = '#'
                elif currentCells[x][y] == ' ' and numNeighbors == 3:
                    # Dead cells with 3 neighbors become alive
                    nextCells[x][y] = '#'
                else:
                    nextCells[x][y] = ' '
        # Game end when no cells alive
        if aliveCells == 0:
            time.sleep(0.5)
            print('Game end!! None cells alive!!')
            break
        time.sleep(1)
except KeyboardInterrupt:
    sys.exit(0)