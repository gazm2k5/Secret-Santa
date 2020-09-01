import numpy as np
from random import shuffle
from collections import Counter

def check_counter(tickets, num_gifts):
    """ Count how many times each person appears in the arrangement """

    cnt = Counter()
    for ticket in tickets: # for each person
        for person in ticket[1]: # tally who they're giving gifts to
            cnt[person] += 1

    # Check that each person has 5 tally marks
    for person in cnt:
        if cnt[person] != num_gifts:
            print("Error: Person {cnt[person]} is not receiving {num_gifts} gifts.")
            return
    print(f"Everyone has been counted {num_gifts} times.")
    return True

def check_self(tickets):
    """ Check no one has been assigned themselves """
    
    for ticket in tickets:
        if ticket[0] in ticket[1]:
            print("Error: Person {ticket[0]} has been assigned to gift themselves.")
            return False
    print("No one has been assigned themselves.")
    return True
        

def secretSanta(num_people, num_gifts):
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
    for i in range(1, num_people + 1):
        tickets.append((i, [i] * num_gifts)) # A tuple with head + list

    # Shuffle tickets
    shuffle(tickets)

    # Create shift amount
    shift = []
    for _ in range(1, num_gifts + 1):
        while (num := np.random.randint(num_people-1) + 1) in shift: # no dupes. -1 so we don't shift back to the start (ie. no one gifts themselves)
            num = np.random.randint(num_people-1) + 1
        shift.append(num)
    
    # Shift tickets along
    for i in range(0,num_gifts):
        buffer = [] # create temporary buffer to hold values
        for ticket in tickets:
            buffer.append(ticket[1][i]) # copy row of tickets
        
        for j in range(0, num_people): # shift this row of tickets by shift amount
            tickets[j][1][i] = buffer[(j + shift[i]) % num_people]

    # Sort tickets back into order
    tickets.sort()
    
    # Print arrangement
    for ticket in tickets:
        print(f"Person {ticket[0]} gifts: \t{ticket[1]}")
    print("")

    # Perform checks and return True if successful
    return check_counter(tickets, num_gifts) * check_self(tickets)

secretSanta(12, 5) # 12 people giving 5 gifts each
