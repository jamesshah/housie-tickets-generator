#    ------------------------------ DESCRIPTION -------------------------------

#    A ticket consists of a random distribution of 15 unique numbers between 1-90 in a
#    3x9 matrix.

#    RULE 1 -   Each row cannot have more than 5 numbers
#    RULE 2 -   Each column is assigned a range of numbers only:
#                1-10 can appear only in column 1
#                11-20 can appear only in column 2
#                81-90 can appear only in column 9
#    RULE 3 -   In a specific column, numbers must be arranged in ascending order
#                from top to bottom


import random
import numpy as np
import sys
from tabulate import tabulate


def getTickets():
    """
    #1 - Maintain array of total_numbers between 1 and 90. Initialize ticket_array as 3x9 array of 0s
    #2 - Generate 15 random indices from the array of total_indices. 
    #3 - Compute index to drop the value into based on RULE #1, RULE #2
    #4 - Remove values used in the ticket from the base array (RULE #1, RULE #2)
    #5 - Repeat till 15 numbers are populated into ticket
    #6 - Sort numbers in every column of the ticket based on RULE #3
    """

    # Create a 2D array [3x9] of 0s
    ticket_array = np.zeros((3, 9), dtype=int)
    # Create an a list of numbers from 1 to 90.
    total_numbers = [num for num in range(1, 90)]
    # Create a list of tupele of all the indices of 3x9 ticket_array . i.e (0,0),(0,1),...,(2,8)
    total_indices = [(i, j) for i in range(3) for j in range(9)]
    # Create an empty list to store 15 random indices to fill in the value.
    random_indices = []

    # Generate 15 random indices that satisfies RULE #1 and store them in random_indices array.

    first_row = random.sample(total_indices[:9], 5)
    second_row = random.sample(total_indices[9:18], 5)
    third_row = random.sample(total_indices[-9:], 5)

    for i in first_row:
        random_indices.append(i)

    for i in second_row:
        random_indices.append(i)

    for i in third_row:
        random_indices.append(i)

    # Populate values in the randomly generated indices such that it satisfies RULE #2 and replace the  value of the used value in total_numbers array by 0.

    for num in random_indices:
        if num[1] == 0:
            number = random.choice(total_numbers[:10])
            ticket_array[num] = number
            total_numbers[total_numbers.index(number)] = 0
        elif num[1] == 1:
            number = random.choice(total_numbers[10:20])
            ticket_array[num] = number
            total_numbers[total_numbers.index(number)] = 0
        elif num[1] == 2:
            number = random.choice(total_numbers[20:30])
            ticket_array[num] = number
            total_numbers[total_numbers.index(number)] = 0
        elif num[1] == 3:
            number = random.choice(total_numbers[30:40])
            ticket_array[num] = number
            total_numbers[total_numbers.index(number)] = 0
        elif num[1] == 4:
            number = random.choice(total_numbers[40:50])
            ticket_array[num] = number
            total_numbers[total_numbers.index(number)] = 0
        elif num[1] == 5:
            number = random.choice(total_numbers[50:60])
            ticket_array[num] = number
            total_numbers[total_numbers.index(number)] = 0
        elif num[1] == 6:
            number = random.choice(total_numbers[60:70])
            ticket_array[num] = number
            total_numbers[total_numbers.index(number)] = 0
        elif num[1] == 7:
            number = random.choice(total_numbers[70:80])
            ticket_array[num] = number
            total_numbers[total_numbers.index(number)] = 0
        elif num[1] == 8:
            number = random.choice(total_numbers[80:89])
            ticket_array[num] = number
            total_numbers[total_numbers.index(number)] = 0

    # Sort the ticket_array column wise to satisfy the RULE #3

    for col in range(9):
        # if all the rows are filled with random number
        if(ticket_array[0][col] != 0 and ticket_array[1][col] != 0 and ticket_array[2][col] != 0):
            for row in range(2):
                if ticket_array[row][col] > ticket_array[row+1][col]:
                    temp = ticket_array[row][col]
                    ticket_array[row][col] = ticket_array[row+1][col]
                    ticket_array[row+1][col] = temp

        # if 1st and 2nd row are filled by random number
        elif(ticket_array[0][col] != 0 and ticket_array[1][col] != 0 and ticket_array[2][col] == 0):
            if ticket_array[0][col] > ticket_array[1][col]:
                temp = ticket_array[0][col]
                ticket_array[0][col] = ticket_array[1][col]
                ticket_array[1][col] = temp

        # if 1st and 3rd row are filled by random number
        elif(ticket_array[0][col] != 0 and ticket_array[2][col] != 0 and ticket_array[1][col] == 0):
            if ticket_array[0][col] > ticket_array[2][col]:
                temp = ticket_array[0][col]
                ticket_array[0][col] = ticket_array[2][col]
                ticket_array[2][col] = temp

        # if 2nd and 3rd rows are filled with random numbers
        elif(ticket_array[0][col] == 0 and ticket_array[1][col] != 0 and ticket_array[2][col] != 0):
            if ticket_array[1][col] > ticket_array[2][col]:
                temp = ticket_array[1][col]
                ticket_array[1][col] = ticket_array[2][col]
                ticket_array[2][col] = temp

    return ticket_array


if __name__ == "__main__":
    numberOfTickets = sys.argv[1]
    tickets = []
    for i in range(int(numberOfTickets)):
        ticket = getTickets()
        tickets.append(ticket)
    for ticket in tickets:
        print(tabulate(ticket, tablefmt="fancy_grid", numalign="center"))
