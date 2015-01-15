def main():
    '''This is the main operating function.'''
    # Import the necessary modules and functions.
    import numpy as np
    import Percolation as perc
    import matplotlib as mbl
    import matplotlib.pyplot as plt
    import pylab
        
    # Establish a Boolean tag to print the menu.
    again=1

    if again==1:
        # Offer two functionality options on a standard menu.
        print 'Welcome to the Direct Percolation Wizard!'
        print 'You have two options:'
        print '1) Visualize the flow of an NxN grid.'
        print '2) Produce a plot of percolation probability versus ' \
              'site vacancy probability.'
        choice=input('Which of the two would you like to do? Enter 1 or 2.')

        # Direct the user to the correct function.
        if choice==1:
            perc.visualize(np,mbl,plt)
            again=0
        elif choice==2:
            # Assign N a value specfic to this assignment.
            N=20
            # Run the plotting function.
            perc.plot(np,N,pylab)

main()