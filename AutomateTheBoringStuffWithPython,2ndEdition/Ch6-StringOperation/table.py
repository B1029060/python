tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(data):
    # Save the longest width of string in list
    colWidths = [0] * len(data)
    for x in range(len(data)):
        colWidths[x] = 0
        for y in range(len(data[x])):
            if len(data[x][y]) > colWidths[x]:
                colWidths[x] = len(data[x][y])

    # Output
    for x in range(len(data[0])):
        text = ''
        for y in range(len(data)):
            text += data[y][x].rjust(colWidths[y]) + ' '
        print(text)

printTable(tableData)
'''
  apples Alice  dogs 
 oranges   Bob  cats 
cherries Carol moose 
  banana David goose 
'''