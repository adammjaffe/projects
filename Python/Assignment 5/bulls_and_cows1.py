# Adam Jaffe
# amj2158
# February 21, 2013
# Professor Cannon
# file: bulls_and_cows.py

# This program plays the game "Bulls and Cows."

def number_generator():
    ' ' 'This creates a random 4-digit number/list with no repeating digits' ' '
    again=0
    import random as r
    while(again==0):
        w=r.randrange(1,10)
        x=r.randrange(0,10)
        y=r.randrange(0,10)
        z=r.randrange(0,10)

        # If there are repeated digits, the function generates a new number.
        
        if(w!=x and w!=y and w!=z and x!=y  and x!=z and y!=z):
            again=1
            return [str(w),str(x),str(y),str(z)]

def player_input(guess):
    ' ' 'This asks for player input and converts it to a list.' ' '
    guess_list=[]

    # The function turns the input into a list to make comparisons easier.
    for i in range(0,4):
        guess_list.append(guess[i])
    return guess_list

def bull_counter(number,guess):
    ' ' 'This counts the number of bulls after a guess.' ' '
    b=0

    # The function compares an object in the input list to the object in the
    # same position in the number list.
    
    for j in range(0,4):
        if number[j]==guess[j]:
            b=b+1
    return b

def cow_counter(number,guess):
    ' ' 'This counts the number of cows after a guess.' ' '
    c=0

    # The function compares an object in the input list to the objects in the
    # number list that are in every position besides the one in occupies.
    
    for k in range(0,4):
        for l in range(0,k):
            if number[k]==guess[l]:
                c=c+1
        for l in range(k+1,4):
            if number[k]==guess[l]:
                c=c+1
    return c
