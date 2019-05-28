# Status: GETTING THERE
# Purpose:
# Author: Imran Virani

# The array for the grid which is needed to display to the user and used to check if the solution is right.
grid = [["x", "x", "x", "x", "x", "x", "x", "x", "x"],
        ["x", "x", "x", "x", "x", "x", "x", "x", "x"],
        ["x", "x", "x", "x", "x", "x", "x", "x", "x"],
        ["x", "x", "x", "x", "x", "x", "x", "x", "x"],
        ["x", "x", "x", "x", "x", "x", "x", "x", "x"],
        ["x", "x", "x", "x", "x", "x", "x", "x", "x"],
        ["x", "x", "x", "x", "x", "x", "x", "x", "x"],
        ["x", "x", "x", "x", "x", "x", "x", "x", "x"],
        ["x", "x", "x", "x", "x", "x", "x", "x", "x"]]

# Functions which displays the grid


def gridRefresh():
    for i in range(10):
        print("")
    print(grid[0][0], grid[0][1], grid[0][2], grid[0][3], grid[0]
          [4], grid[0][5], grid[0][6], grid[0][7], grid[0][8])
    print(grid[1][0], grid[1][1], grid[1][2], grid[1][3], grid[1]
          [4], grid[1][5], grid[1][6], grid[1][7], grid[1][8])
    print(grid[2][0], grid[2][1], grid[2][2], grid[2][3], grid[2]
          [4], grid[2][5], grid[2][6], grid[2][7], grid[2][8])
    print(grid[3][0], grid[3][1], grid[3][2], grid[3][3], grid[3]
          [4], grid[3][5], grid[3][6], grid[3][7], grid[3][8])
    print(grid[4][0], grid[4][1], grid[4][2], grid[4][3], grid[4]
          [4], grid[4][5], grid[4][6], grid[4][7], grid[4][8])
    print(grid[5][0], grid[5][1], grid[5][2], grid[5][3], grid[5]
          [4], grid[5][5], grid[5][6], grid[5][7], grid[5][8])
    print(grid[6][0], grid[6][1], grid[6][2], grid[6][3], grid[6]
          [4], grid[6][5], grid[6][6], grid[6][7], grid[6][8])
    print(grid[7][0], grid[7][1], grid[7][2], grid[7][3], grid[7]
          [4], grid[7][5], grid[7][6], grid[7][7], grid[7][8])
    print(grid[8][0], grid[8][1], grid[8][2], grid[8][3], grid[8]
          [4], grid[8][5], grid[8][6], grid[8][7], grid[8][8])


# Counters which are used for the prompt and inputs
row1Counter = 1
row2Counter = 1
row3Counter = 1
row4Counter = 1
row5Counter = 1
row6Counter = 1
row7Counter = 1
row8Counter = 1
row9Counter = 1
countChecker = 1
# Used to check to make sure that every single row, column and box have no duplicates,
# each state is stored as True or False, if there is a false in teh array the solution
# is wrong as there are duplicates, if False is returned there are no duplicates
states = []
rowCounter = 0
gridRefresh()
# Iterates through the first row and collects inputs for each cell in the sudoku grid
for i in grid[0]:
    grid[0][row1Counter - 1] = int(
        input("Please enter the value for Row 1 Column " + str(row1Counter) + ": "))
    while grid[0][row1Counter - 1] <= 0 or grid[0][row1Counter - 1] > 9:
        grid[0][row1Counter - 1] = int(
            input("The value you entered is invalid please enter a number between 1 and 9 for Row 1 Column " + str(row1Counter) + ": "))
    row1Counter += 1
    gridRefresh()

rowCounter = 0
# Algorithm that checks for duplicates in a list and returns true if thre are duplicates and
while countChecker <= 9:
    # The count function returns the number times that a indice is repeated in a list. If there are more than 1 there are duplicates so the Algorithm returns true meaning that the solution entered is false
    if grid[0].count(countChecker) > 1:
        states.append(True)

    else:
        if grid[0].count(countChecker) == 1:
            states.append(False)
    countChecker += 1

# Resets counter to 1 so that the counter can be used again for the next check
# for duplicates for the next row. This is done for each row so that the counter can check for each number between 1 and 9. This is done 9 times, 1 once for each row
countChecker = 1

for i in grid[1]:
    grid[1][row2Counter - 1] = int(
        input("Please enter the value for Row 2 Column " + str(row2Counter) + " as a value between 1 and 9: "))
    while grid[1][row2Counter - 1] <= 0 or grid[1][row2Counter] > 9:
        grid[1][row2Counter] = int(input(
            "The value you entered is invalid, please enter the number bewteen 1 and 9 for Row 2 Column " + str(row2Counter) + ": "))
    row2Counter += 1
    gridRefresh()


while countChecker <= 9:
    if grid[1].count(countChecker) > 1:
        countChecker += 1
        states.append(True)
    else:
        if grid[1].count(countChecker) == 1:
            states.append(False)
            countChecker += 1
for i in grid[2]:
    grid[2][row3Counter - 1] = int(
        input("Please enter the value for Row 3 Column " + str(row3Counter) + ": "))
    while grid[2][row3Counter - 1] <= 0 or grid[1][row3Counter] > 9:
        grid[2][row3Counter - 1] = int(
            input("The number you entered is invalid. Please enter the value for Row 3 Column " + str(row3Counter) + " as a number between 1 and 9: "))
    row3Counter += 1
    gridRefresh()
while countChecker <= 9:
    if grid[2].count(countChecker) > 1:
        countChecker += 1
        states.append(True)
    else:
        if grid[2].count(countChecker) == 1:
            states.append(False)
            countChecker += 1
countChecker = 1
print(states)
for i in grid[3]:
    grid[3][row4Counter - 1] = int(
        input("Please enter the value for Row 4 Column " + str(row4Counter) + ": "))
    row4Counter += 1
    while grid[1][row2Counter - 1] <= 0 or grid[1][row2Counter] > 9:
        grid[3][row4Counter - 1] = int(
            input("The number you entered is invalid. Please enter the value for Row 4 Column " + str(row4Counter) + " as a number between 1 and 9: "))
    gridRefresh()
while countChecker <= 9:
    if grid[3].count(countChecker) > 1:
        countChecker += 1
        states.append(True)
    else:
        if grid[3].count(countChecker) == 1:
            states.append(False)
            countChecker += 1
countChecker = 1

for i in grid[4]:
    grid[4][row5Counter - 1] = int(
        input("Please enter the value for Row 5 Column " + str(row5Counter) + ": "))
    while grid[4][row5Counter - 1] <= 0 or grid[4][row5Counter - 1] > 9:
        grid[4][row5Counter - 1] = int(
            input("The value you entered is invalid. Please enter the value for Row 5 Column " + str(row5Counter) + " as a number between 1 and 9: "))
    row5Counter += 1
    gridRefresh()
while countChecker <= 9:
    if grid[4].count(countChecker) > 1:
        countChecker += 1
        states.append(True)
    else:
        if grid[4].count(countChecker) == 1:
            states.append(False)
            countChecker += 1
countChecker = 1
print(states)
for i in grid[5]:
    grid[5][row6Counter - 1] = int(
        input("Please enter the value for Row 6 Column " + str(row6Counter) + ": "))
    while grid[5][row6Counter - 1] <= 0 or grid[5][row6Counter] > 9:
        grid[5][row6Counter - 1] = int(
            input("The value that you entered is invalid. Please enter the value for Row 6 Column " + str(row6Counter) + " as a number between 1 and 9: "))
    row6Counter += 1
    gridRefresh()
while countChecker <= 9:
    if grid[5].count(countChecker) > 1:
        countChecker += 1
        states.append(True)
    else:
        if grid[5].count(countChecker) == 1:
            states.append(False)
            countChecker += 1
countChecker = 1
for i in grid[6]:
    grid[6][row7Counter - 1] = int(
        input("Please enter the value for Row 7 Column " + str(row7Counter) + ": "))
    while grid[6][row7Counter - 1] <= 0 or grid[6][row7Counter] > 9:
        grid[6][row7Counter - 1] = int(
            input("The value that you entered is invalid. Please enter the value for Row 7 Column " + str(row7Counter) + " as a number between 1 and 9: "))
    row7Counter += 1
    gridRefresh()
while countChecker <= 9:
    if grid[6].count(countChecker) > 1:
        countChecker += 1
        states.append(True)
    else:
        if grid[6].count(countChecker) == 1:
            states.append(False)
            countChecker += 1
countChecker = 1
print(states)
for i in grid[7]:
    grid[7][row8Counter -
            1] = int(input("Please enter the value for Row 8 Column " + str(row8Counter) + ": "))
    row8Counter += 1
    gridRefresh()
while countChecker <= 9:
    if grid[7].count(countChecker) > 1:
        countChecker += 1
        states.append(True)
    else:
        if grid[7].count(countChecker) == 1:
            states.append(False)
            countChecker += 1
countChecker = 1
print(states)
for i in grid[8]:
    grid[8][row9Counter -
            1] = int(input("Please enter the value for Row 9 Column " + str(row9Counter) + ": "))
    row9Counter += 1
    gridRefresh()
while countChecker <= 9:
    if grid[8].count(countChecker) > 1:
        countChecker += 1
        states.append(True)
    else:
        if grid[8].count(countChecker) == 1:
            states.append(False)
            countChecker += 1
countChecker = 1
# The array is initialized for each column, containing the numbers that the
# user inputted previously
column1 = [grid[0][0],
           grid[1][0],
           grid[2][0],
           grid[3][0],
           grid[4][0],
           grid[5][0],
           grid[6][0],
           grid[7][0],
           grid[8][0]]
# The same Algorithm used for the rows is used. This is done for each column.
# The array is updated if there are any duplicates in each column.
while countChecker <= 9:
    if column1.count(countChecker) > 1:
        countChecker += 1
        states.append(True)
    else:
        if column1.count(countChecker) == 1:
            states.append(False)
            countChecker += 1
countChecker = 1

column2 = [grid[0][1],
           grid[1][1],
           grid[2][1],
           grid[3][1],
           grid[4][1],
           grid[5][1],
           grid[6][1],
           grid[7][1],
           grid[8][1]]
while countChecker <= 9:
    if column2.count(countChecker) > 1:
        countChecker += 1
        states.append(True)
    else:
        if column2.count(countChecker) == 1:
            states.append(False)
            countChecker += 1
countChecker = 1
column3 = [grid[0][2],
           grid[1][2],
           grid[2][2],
           grid[3][2],
           grid[4][2],
           grid[5][2],
           grid[6][2],
           grid[7][2],
           grid[8][2]]
while countChecker <= 9:
    if column3.count(countChecker) > 1:
        countChecker += 1
        states.append(True)
    else:
        if column3.count(countChecker) == 1:
            states.append(False)
            countChecker += 1
countChecker = 1

column4 = [grid[0][3],
           grid[1][3],
           grid[2][3],
           grid[3][3],
           grid[4][3],
           grid[5][3],
           grid[6][3],
           grid[7][3],
           grid[8][3]]
while countChecker <= 9:
    if column4.count(countChecker) > 1:
        countChecker += 1
        states.append(True)
    else:
        if column4.count(countChecker) == 1:
            states.append(False)
            countChecker += 1

column5 = [grid[0][4],
           grid[1][4],
           grid[2][4],
           grid[3][4],
           grid[4][4],
           grid[5][4],
           grid[6][4],
           grid[7][4],
           grid[8][4]]
while countChecker <= 9:
    if column5.count(countChecker) > 1:
        countChecker += 1
        states.append(True)
    else:
        if column5.count(countChecker) == 1:
            states.append(False)
            countChecker += 1

column6 = [grid[0][5],
           grid[1][5],
           grid[2][5],
           grid[3][5],
           grid[4][5],
           grid[5][5],
           grid[6][5],
           grid[7][5],
           grid[8][5]]
while countChecker <= 9:
    if column6.count(countChecker) > 1:
        countChecker += 1
        states.append(True)
    else:
        if column6.count(countChecker) == 1:
            states.append(False)
            countChecker += 1

column7 = [grid[0][6],
           grid[1][6],
           grid[2][6],
           grid[3][1],
           grid[4][6],
           grid[5][6],
           grid[6][6],
           grid[7][6],
           grid[8][6]]
while countChecker <= 9:
    if column7.count(countChecker) > 1:
        countChecker += 1
        states.append(True)
    else:
        if column7.count(countChecker) == 1:
            states.append(False)
            countChecker += 1

column8 = [grid[0][7],
           grid[1][7],
           grid[2][7],
           grid[3][7],
           grid[4][7],
           grid[5][7],
           grid[6][7],
           grid[7][7],
           grid[8][7]]
while countChecker <= 9:
    if column8.count(countChecker) > 1:
        countChecker += 1
        states.append(True)
    else:
        if column8.count(countChecker) == 1:
            states.append(False)
            countChecker += 1

column9 = [grid[0][8],
           grid[1][8],
           grid[2][8],
           grid[3][8],
           grid[4][8],
           grid[5][8],
           grid[6][8],
           grid[7][8],
           grid[8][8]]
while countChecker <= 9:
    if column9.count(countChecker) > 1:
        countChecker += 1
        states.append(True)
    else:
        if column9.count(countChecker) == 1:
            states.append(False)
            countChecker += 1
# Initializes each box as an array
box1 = [grid[0][0], grid[0][1], grid[0][2],
        grid[1][0], grid[1][1], grid[1][2],
        grid[1][0], grid[1][1], grid[1][2]]

# The Algorithm, it counts each number from 1-9 and then checks for
# duplicates. This is done for every box(repeated 9 times)
while countChecker <= 9:
    if box1.count(countChecker) > 1:
        countChecker += 1
        states.append(True)
    else:
        if box1.count(countChecker) == 1:
            states.append(False)
            countChecker += 1
countChecker = 1
box2 = [grid[0][3], grid[0][4], grid[0][5],
        grid[1][3], grid[1][4], grid[1][5],
        grid[2][3], grid[2][4], grid[2][5]]
while countChecker <= 9:
    if box2.count(countChecker) > 1:
        countChecker += 1
        states.append(True)
    else:
        if box2.count(countChecker) == 1:
            states.append(False)
            countChecker += 1
countChecker = 1
box3 = [grid[0][6], grid[0][7], grid[0][8],
        grid[1][6], grid[1][7], grid[1][8],
        grid[2][6], grid[2][7], grid[2][8]]
while countChecker <= 9:
    if box3.count(countChecker) > 1:
        countChecker += 1
        states.append(True)
    else:
        if box3.count(countChecker) == 1:
            states.append(False)
            countChecker += 1
countChecker = 1

box4 = [grid[3][0], grid[4][1], grid[4][2],
        grid[4][0], grid[5][1], grid[5][2],
        grid[5][0], grid[6][1], grid[6][2]]
while countChecker <= 9:
    if box4.count(countChecker) > 1:
        countChecker += 1
        states.append(True)
    else:
        if box4.count(countChecker) == 1:
            states.append(False)
            countChecker += 1
countChecker = 1

box5 = [grid[3][3], grid[4][4], grid[4][5],
        grid[4][0], grid[5][1], grid[5][2],
        grid[5][0], grid[6][1], grid[6][2]]
while countChecker <= 9:
    if box5.count(countChecker) > 1:
        countChecker += 1
        states.append(True)
    else:
        if box5.count(countChecker) == 1:
            states.append(False)
            countChecker += 1
countChecker = 1

box6 = [grid[3][6], grid[4][7], grid[4][8],
        grid[4][6], grid[5][7], grid[5][8],
        grid[5][6], grid[6][7], grid[6][8]]
while countChecker <= 9:
    if box6.count(countChecker) > 1:
        countChecker += 1
        states.append(True)
    else:
        if box6.count(countChecker) == 1:
            states.append(False)
            countChecker += 1
countChecker = 1

box7 = [grid[6][0], grid[4][1], grid[4][2],
        grid[7][0], grid[5][1], grid[5][2],
        grid[8][0], grid[6][1], grid[6][2]]
while countChecker <= 9:
    if box7.count(countChecker) > 1:
        countChecker += 1
        states.append(True)
    else:
        if box7.count(countChecker) == 1:
            states.append(False)
            countChecker += 1
countChecker = 1

box8 = [grid[6][3], grid[4][4], grid[4][5],
        grid[7][3], grid[5][4], grid[5][5],
        grid[8][3], grid[6][4], grid[6][5]]
while countChecker <= 9:
    if box8.count(countChecker) > 1:
        countChecker += 1
        states.append(True)
    else:
        if box8.count(countChecker) == 1:
            states.append(False)
            countChecker += 1
countChecker = 1

box9 = [grid[6][6], grid[6][7], grid[6][8],
        grid[7][6], grid[7][7], grid[7][8],
        grid[8][6], grid[8][7], grid[8][8]]
while countChecker <= 9:
    if box9.count(countChecker) > 1:
        countChecker += 1
        states.append(True)
    else:
        if box9.count(countChecker) == 1:
            states.append(False)
            countChecker += 1
# Checks to see if any part of the sudoku had any true which means duplicates. If there are none than the solution is solution
if True in states:
    print("Unfortunately you are incorrect. PLease reattempt")
else:
    print("Congratulations! The solution that you submitted is correct")
