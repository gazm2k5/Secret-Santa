import numpy as np
from random import shuffle
from collections import Counter

def check_counter(tickets, num_gifts):
    """ Count how many times each person appears in the arrangement """

    cnt = Counter()
    for ticket in tickets: # for each person
        for person in ticket[1]: # tally who's is receiving a gift
            if person != "x": # don't tally x's
                cnt[person] += 1

    # Check that each person has num_gifts tally marks
    for person in cnt:
        if cnt[person] < num_gifts:
            print(f"Person {person} is receiving {cnt[person]} gifts.")

    print(f"Everyone else has been counted {num_gifts} times.\n")
    return True

def check_self(tickets):
    """ Check no one has been assigned themselves """
    
    for ticket in tickets:
        if ticket[0] in ticket[1]:
            print(f"Error: Person {ticket[0]} has been assigned to gift themselves.")
            return False
    print("No one has been assigned themselves.\n")
    return True

def check_dupes(tickets):
    """ Check no one has been assigned to gift the same person twice """

    for ticket in tickets:
        cnt = Counter()
        for recipient in ticket[1]:
            if recipient != "x": #ignore x's
                cnt[recipient] += 1

        for recipient in cnt:
            if cnt[recipient] > 1:
                print(f"Error: {recipient} appears more than once for Person {ticket[0]}")
                return False
    print("No one is gifting the same person more than once.\n")
    return True

def shifter(my_list, shift_amount, num_people):
    """ Takes a list and shifts values along by the shift amount, ignoring "x" values """
    
    # create blank list
    shifted_list = [None] * num_people

    # Shift list along, including x's
    for i in range(num_people):
        shifted_list[i] = my_list[(i + shift_amount) % num_people]

    # remove x's from shifted list
    while "x" in shifted_list:
        shifted_list.remove("x")

    # copy shifted list to new list with original x positions
    i = 0
    final_shifted_list = []
    for value in my_list:
        if value == "x":
            final_shifted_list.append("x")
            continue
        else:
            final_shifted_list.append(shifted_list[i])
            i += 1

    return final_shifted_list

def secretSanta(num_people, num_gifts, *args):
    """ Everyone puts their name num_gifts +1 times on a ticket (that
    being the number of gifts to receive). The tickets are shuffled around
    and then cut up into num_gifts + 1 pieces. Each row is shifted along
    a random amount, and the tickets are stitched back up. Everyone picks
    a ticket telling them their number and num_gifts random people to gift.
    https://www.youtube.com/watch?v=5kC5k5QBqcc
    """

    # Input check
    if not type(num_people) == int or not type(num_gifts) == int or num_people < 1 or num_gifts < 1:
        print("Requires 2 positive integer values.")
        return False
    if num_gifts > num_people - 1:
        print("Currently only supports people giving 1 gift maximum per person.") 
        return False
    
    # Create tickets
    tickets = []
    num_awkward_peeps = len(args)
        
    for i in range(1, num_people + 1):
        # First add tickets for any people that don't have normal amount of gifts
        if i <= num_awkward_peeps:
            personal_num_gifts = args[i-1]
            tickets.append((i, [i] * personal_num_gifts + ["x"]*(num_gifts - personal_num_gifts) )) # Add their number for gifts, x for no gifts
            continue
            
        tickets.append((i, [i] * num_gifts)) # A tuple with head + list

    # Shuffle tickets
    shuffle(tickets)

    # Calcualte max shift amount (so no one gifts themselves)
    max_offset = [num_people-1] * num_gifts # Number of gifts per row

    # Adjust Max shift amount if some people have less than num_gifts
    #for gifts in args:
    #    rows_to_subtract = num_gifts - gifts # -1 for x rows. x is gift deficit for this person
    #    for i in range(len(max_offset), len(max_offset) - rows_to_subtract, -1): # Run backwards through offset list
    #        max_offset[i-1] -= 1                

    # Create shift amount
    shift = []
    for i in range(0, num_gifts):
        while (num := np.random.randint(max_offset[i]) + 1) in shift: # no duplicates
            num = np.random.randint(max_offset[i]) + 1
        shift.append(num)

    print(f"{shift=}")

    # Shift each row of tickets along
    for i in range(0,num_gifts):
        buffer = [] # create temporary buffer to hold values
        for ticket in tickets:
            buffer.append(ticket[1][i]) # copy row of ticket

        # Calculate shifted row values
        shifted_buffer = shifter(buffer, shift[i], num_people)

        # Adjust original tickets    
        for j in range(0, num_people):
            tickets[j][1][i] = shifted_buffer[j]

    # Sort tickets back into order
    tickets.sort()
    
    # Print arrangement
    for ticket in tickets:
        print(f"Person {ticket[0]} gifts: \t{ticket[1]}")
    print("") # new line

    # Perform checks and return True if successful
    return check_counter(tickets, num_gifts) * check_self(tickets) * check_dupes(tickets)

secretSanta(12, 5, 1, 3)
