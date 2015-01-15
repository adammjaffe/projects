# Adam Jaffe
# amj2158
# Intro to Computer Science for Engineers
# Professor Cannon

# The program creates a graphical user interface for the Bulls and Cows game.

# Import the necessary module and gameplay file.
import Tkinter
import bulls_and_cows1 as bc

class MyGUI:
    total_guesses=0.0
    times_played=1
    guess_number=1
    other_guess_number=0
    bulls=0
    number = bc.number_generator()
    def __init__(self):
        # Create the main window widget.
        self.main_window = Tkinter.Tk()

        # Create the frames necessary to store the user's guesses, game stats,
        # notes to the user, and the buttons.
        self.welcome_frame = Tkinter.Frame(self.main_window)
        self.guess_frame = Tkinter.Frame(self.main_window)
        self.guess1_frame = Tkinter.Frame(self.main_window)
        self.guess2_frame = Tkinter.Frame(self.main_window)
        self.guess3_frame = Tkinter.Frame(self.main_window)
        self.guess4_frame = Tkinter.Frame(self.main_window)
        self.guess5_frame = Tkinter.Frame(self.main_window)
        self.guess6_frame = Tkinter.Frame(self.main_window)
        self.guess7_frame = Tkinter.Frame(self.main_window)
        self.guess8_frame = Tkinter.Frame(self.main_window)
        self.guess9_frame = Tkinter.Frame(self.main_window)
        self.guess10_frame = Tkinter.Frame(self.main_window)
        self.notes_frame = Tkinter.Frame(self.main_window)
        self.answer_frame = Tkinter.Frame(self.main_window)
        self.avg_guesses_frame = Tkinter.Frame(self.main_window)
        self.buttons_frame = Tkinter.Frame(self.main_window)

        # Create and pack the widgets for the welcome frame.
        self.welcome_label = Tkinter.Label(self.welcome_frame, \
                        text='Welcome to Bulls and Cows!')
        self.welcome_label.pack()

        # Create and pack the widgets for guess.
        self.guess_label= Tkinter.Label(self.guess_frame, \
                    text='Enter a four-digit number:')
        self.guess_entry = Tkinter.Entry(self.guess_frame, width=4)
        self.guess_label.pack(side='left')
        self.guess_entry.pack(side='left')

        # Create and pack the widgets for guess 1.
        self.guess1_label = Tkinter.Label(self.guess1_frame, text='Guess 1:')
        self.guess1 = Tkinter.StringVar()
        self.guess1_result_label = Tkinter.Label(self.guess1_frame, \
                        textvariable=self.guess1)
        self.guess1_label.pack(side='left')
        self.guess1_result_label.pack(side='left')

        self.bulls1_label = Tkinter.Label(self.guess1_frame, text='Bulls:')
        self.bulls1 = Tkinter.StringVar()
        self.bulls1_result_label = Tkinter.Label(self.guess1_frame, \
                        textvariable=self.bulls1)
        self.bulls1_label.pack(side='left')
        self.bulls1_result_label.pack(side='left')
        
        self.cows1_label = Tkinter.Label(self.guess1_frame, text='Cows:')
        self.cows1 = Tkinter.StringVar()
        self.cows1_result_label = Tkinter.Label(self.guess1_frame, \
                        textvariable=self.cows1)
        self.cows1_label.pack(side='left')
        self.cows1_result_label.pack(side='left')
        
        # Create and pack the widgets for guess 2.
        self.guess2_label = Tkinter.Label(self.guess2_frame, text='Guess 2:')
        self.guess2 = Tkinter.StringVar()
        self.guess2_result_label = Tkinter.Label(self.guess2_frame, \
                        textvariable=self.guess2)
        self.guess2_label.pack(side='left')
        self.guess2_result_label.pack(side='left')

        self.bulls2_label = Tkinter.Label(self.guess2_frame, text='Bulls:')
        self.bulls2 = Tkinter.StringVar()
        self.bulls2_result_label = Tkinter.Label(self.guess2_frame, \
                        textvariable=self.bulls2)
        self.bulls2_label.pack(side='left')
        self.bulls2_result_label.pack(side='left')
        
        self.cows2_label = Tkinter.Label(self.guess2_frame, text='Cows:')
        self.cows2 = Tkinter.StringVar()
        self.cows2_result_label = Tkinter.Label(self.guess2_frame, \
                        textvariable=self.cows2)
        self.cows2_label.pack(side='left')
        self.cows2_result_label.pack(side='left')

        # Create and pack the widgets for guess 3.
        self.guess3_label = Tkinter.Label(self.guess3_frame, text='Guess 3:')
        self.guess3 = Tkinter.StringVar()
        self.guess3_result_label = Tkinter.Label(self.guess3_frame, \
                        textvariable=self.guess3)
        self.guess3_label.pack(side='left')
        self.guess3_result_label.pack(side='left')

        self.bulls3_label = Tkinter.Label(self.guess3_frame, text='Bulls:')
        self.bulls3 = Tkinter.StringVar()
        self.bulls3_result_label = Tkinter.Label(self.guess3_frame, \
                        textvariable=self.bulls3)
        self.bulls3_label.pack(side='left')
        self.bulls3_result_label.pack(side='left')
        
        self.cows3_label = Tkinter.Label(self.guess3_frame, text='Cows:')
        self.cows3 = Tkinter.StringVar()
        self.cows3_result_label = Tkinter.Label(self.guess3_frame, \
                        textvariable=self.cows3)
        self.cows3_label.pack(side='left')
        self.cows3_result_label.pack(side='left')

        # Create and pack the widgets for guess 4.
        self.guess4_label = Tkinter.Label(self.guess4_frame, text='Guess 4:')
        self.guess4 = Tkinter.StringVar()
        self.guess4_result_label = Tkinter.Label(self.guess4_frame, \
                        textvariable=self.guess4)
        self.guess4_label.pack(side='left')
        self.guess4_result_label.pack(side='left')

        self.bulls4_label = Tkinter.Label(self.guess4_frame, text='Bulls:')
        self.bulls4 = Tkinter.StringVar()
        self.bulls4_result_label = Tkinter.Label(self.guess4_frame, \
                        textvariable=self.bulls4)
        self.bulls4_label.pack(side='left')
        self.bulls4_result_label.pack(side='left')
        
        self.cows4_label = Tkinter.Label(self.guess4_frame, text='Cows:')
        self.cows4 = Tkinter.StringVar()
        self.cows4_result_label = Tkinter.Label(self.guess4_frame, \
                        textvariable=self.cows4)
        self.cows4_label.pack(side='left')
        self.cows4_result_label.pack(side='left')

        # Create and pack the widgets for guess 5.
        self.guess5_label = Tkinter.Label(self.guess5_frame, text='Guess 5:')
        self.guess5 = Tkinter.StringVar()
        self.guess5_result_label = Tkinter.Label(self.guess5_frame, \
                        textvariable=self.guess5)
        self.guess5_label.pack(side='left')
        self.guess5_result_label.pack(side='left')

        self.bulls5_label = Tkinter.Label(self.guess5_frame, text='Bulls:')
        self.bulls5 = Tkinter.StringVar()
        self.bulls5_result_label = Tkinter.Label(self.guess5_frame, \
                        textvariable=self.bulls5)
        self.bulls5_label.pack(side='left')
        self.bulls5_result_label.pack(side='left')
        
        self.cows5_label = Tkinter.Label(self.guess5_frame, text='Cows:')
        self.cows5 = Tkinter.StringVar()
        self.cows5_result_label = Tkinter.Label(self.guess5_frame, \
                        textvariable=self.cows5)
        self.cows5_label.pack(side='left')
        self.cows5_result_label.pack(side='left')

        # Create and pack the widgets for guess 6.
        self.guess6_label = Tkinter.Label(self.guess6_frame, text='Guess 6:')
        self.guess6 = Tkinter.StringVar()
        self.guess6_result_label = Tkinter.Label(self.guess6_frame, \
                        textvariable=self.guess6)
        self.guess6_label.pack(side='left')
        self.guess6_result_label.pack(side='left')

        self.bulls6_label = Tkinter.Label(self.guess6_frame, text='Bulls:')
        self.bulls6 = Tkinter.StringVar()
        self.bulls6_result_label = Tkinter.Label(self.guess6_frame, \
                        textvariable=self.bulls6)
        self.bulls6_label.pack(side='left')
        self.bulls6_result_label.pack(side='left')
        
        self.cows6_label = Tkinter.Label(self.guess6_frame, text='Cows:')
        self.cows6 = Tkinter.StringVar()
        self.cows6_result_label = Tkinter.Label(self.guess6_frame, \
                        textvariable=self.cows6)
        self.cows6_label.pack(side='left')
        self.cows6_result_label.pack(side='left')

        # Create and pack the widgets for guess 7.
        self.guess7_label = Tkinter.Label(self.guess7_frame, text='Guess 7:')
        self.guess7 = Tkinter.StringVar()
        self.guess7_result_label = Tkinter.Label(self.guess7_frame, \
                        textvariable=self.guess7)
        self.guess7_label.pack(side='left')
        self.guess7_result_label.pack(side='left')

        self.bulls7_label = Tkinter.Label(self.guess7_frame, text='Bulls:')
        self.bulls7 = Tkinter.StringVar()
        self.bulls7_result_label = Tkinter.Label(self.guess7_frame, \
                        textvariable=self.bulls7)
        self.bulls7_label.pack(side='left')
        self.bulls7_result_label.pack(side='left')
        
        self.cows7_label = Tkinter.Label(self.guess7_frame, text='Cows:')
        self.cows7 = Tkinter.StringVar()
        self.cows7_result_label = Tkinter.Label(self.guess7_frame, \
                        textvariable=self.cows7)
        self.cows7_label.pack(side='left')
        self.cows7_result_label.pack(side='left')

        # Create and pack the widgets for guess 8.
        self.guess8_label = Tkinter.Label(self.guess8_frame, text='Guess 8:')
        self.guess8 = Tkinter.StringVar()
        self.guess8_result_label = Tkinter.Label(self.guess8_frame, \
                        textvariable=self.guess8)
        self.guess8_label.pack(side='left')
        self.guess8_result_label.pack(side='left')

        self.bulls8_label = Tkinter.Label(self.guess8_frame, text='Bulls:')
        self.bulls8 = Tkinter.StringVar()
        self.bulls8_result_label = Tkinter.Label(self.guess8_frame, \
                         textvariable=self.bulls8)
        self.bulls8_label.pack(side='left')
        self.bulls8_result_label.pack(side='left')
        
        self.cows8_label = Tkinter.Label(self.guess8_frame, text='Cows:')
        self.cows8 = Tkinter.StringVar()
        self.cows8_result_label = Tkinter.Label(self.guess8_frame, \
                        textvariable=self.cows8)
        self.cows8_label.pack(side='left')
        self.cows8_result_label.pack(side='left')

        # Create and pack the widgets for guess 9.
        self.guess9_label = Tkinter.Label(self.guess9_frame, text='Guess 9:')
        self.guess9 = Tkinter.StringVar()
        self.guess9_result_label = Tkinter.Label(self.guess9_frame, \
                        textvariable=self.guess9)
        self.guess9_label.pack(side='left')
        self.guess9_result_label.pack(side='left')

        self.bulls9_label = Tkinter.Label(self.guess9_frame, text='Bulls:')
        self.bulls9 = Tkinter.StringVar()
        self.bulls9_result_label = Tkinter.Label(self.guess9_frame, \
                        textvariable=self.bulls9)
        self.bulls9_label.pack(side='left')
        self.bulls9_result_label.pack(side='left')
        
        self.cows9_label = Tkinter.Label(self.guess9_frame, text='Cows:')
        self.cows9 = Tkinter.StringVar()
        self.cows9_result_label = Tkinter.Label(self.guess9_frame, \
                        textvariable=self.cows9)
        self.cows9_label.pack(side='left')
        self.cows9_result_label.pack(side='left')

        # Create and pack the widgets for guess 10.
        self.guess10_label = Tkinter.Label(self.guess10_frame, text='Guess 10:')
        self.guess10 = Tkinter.StringVar()
        self.guess10_result_label = Tkinter.Label(self.guess10_frame, \
                        textvariable=self.guess10)
        self.guess10_label.pack(side='left')
        self.guess10_result_label.pack(side='left')

        self.bulls10_label = Tkinter.Label(self.guess10_frame, text='Bulls:')
        self.bulls10 = Tkinter.StringVar()
        self.bulls10_result_label = Tkinter.Label(self.guess10_frame, \
                        textvariable=self.bulls10)
        self.bulls10_label.pack(side='left')
        self.bulls10_result_label.pack(side='left')
        
        self.cows10_label = Tkinter.Label(self.guess10_frame, text='Cows:')
        self.cows10 = Tkinter.StringVar()
        self.cows10_result_label = Tkinter.Label(self.guess10_frame, \
                        textvariable=self.cows10)
        self.cows10_label.pack(side='left')
        self.cows10_result_label.pack(side='left')

        # Create and pack the widgets for the notes to the user.
        self.notes = Tkinter.StringVar()
        self.notes_label = Tkinter.Label(self.notes_frame, \
                        textvariable=self.notes)
        self.notes_label.pack(side='bottom')

        # Create and pack the widgets for the answer label.
        self.answer_space = Tkinter.Label(self.answer_frame, \
                        text='The answer was:')
        self.answer = Tkinter.StringVar()
        self.answer_label = Tkinter.Label(self.answer_frame, \
                        textvariable=self.answer)
        self.answer_space.pack(side='left')
        self.answer_label.pack(side='left')
        
        # Create and pack the widgets for the average number of guesses.
        self.avg_guesses = Tkinter.StringVar()
        self.avg_guesses_label = Tkinter.Label(self.avg_guesses_frame, \
                        textvariable=self.avg_guesses)
        self.avg_guesses_name_label = Tkinter.Label(self.avg_guesses_frame, \
                        text='Average Guesses:')
        self.avg_guesses_name_label.pack(side='left')
        self.avg_guesses_label.pack(side='left')

        # Create and pack the widgets for the 'Guess,' 'Play Again,' and
        # 'Quit' buttons.
        self.guess_button = Tkinter.Button(self.buttons_frame, \
                        text='Guess',command=self.update_guess)
        self.guess_button.pack(side='left')
        self.play_again_button = Tkinter.Button(self.buttons_frame, \
                        text='Play Again',command=self.play_again)
        self.play_again_button.pack(side='left')
        self.quit_button = Tkinter.Button(self.buttons_frame, text='Quit', \
                        command=self.main_window.destroy)
        self.quit_button.pack(side='left')

        # Pack the frames.
        self.welcome_frame.pack()
        self.guess_frame.pack()
        self.guess1_frame.pack()
        self.guess2_frame.pack()
        self.guess3_frame.pack()
        self.guess4_frame.pack()
        self.guess5_frame.pack()
        self.guess6_frame.pack()
        self.guess7_frame.pack()
        self.guess8_frame.pack()
        self.guess9_frame.pack()
        self.guess10_frame.pack()
        self.notes_frame.pack()
        self.answer_frame.pack()
        self.avg_guesses_frame.pack()
        self.buttons_frame.pack()

        # Start the main loop.
        Tkinter.mainloop()

    # The update_guess function tells you how many bulls and cows a guess 
    # has and is the callback function for the guess_button widget.

    def update_guess(self):
        # Use functions from my old bulls and cows file to run the game.
        if self.guess_number==10:
            # Update the other_guess_number to keep track of how many guesses
            # have been made.
            self.other_guess_number=10
            # Find our what the guess was.
            guess = str(self.guess_entry.get())
            # Update the guess label.
            self.guess10.set(guess)
            guess = bc.player_input(guess)
            # Calculate the number of bulls and update the bulls label.
            self.bulls = str(bc.bull_counter(self.number,guess))
            self.bulls10.set(self.bulls)
            # Calculate the number of cows and update the cows label.
            cows = str(bc.cow_counter(self.number,guess))
            self.cows10.set(cows)
            
            if self.bulls=='4':
                # If they've won the game, go to the function that alerts them
                # and updates their stats.
                self.update_avg_guesses()
            else:
                # Otherwise, update their stats and tell them they've lost.
                self.answer.set(''.join(self.number))
                self.update_avg_guesses()
                self.notes.set('You lose! Play again!')
                
        elif self.guess_number==9:
            # Run the game as above.
            self.other_guess_number=9
            guess = str(self.guess_entry.get())
            self.guess9.set(guess)
            guess = bc.player_input(guess)
            self.bulls = str(bc.bull_counter(self.number,guess))
            self.bulls9.set(self.bulls)
            cows = str(bc.cow_counter(self.number,guess))
            self.cows9.set(cows)
            if self.bulls=='4':
                self.update_avg_guesses()
            else:
                # Go to the next guess label if an incorrect answer is given.
                self.guess_number=10
                
        elif self.guess_number==8:
            # Run the game as above.
            self.other_guess_number=8
            guess = str(self.guess_entry.get())
            self.guess8.set(guess)
            guess = bc.player_input(guess)
            self.bulls = str(bc.bull_counter(self.number,guess))
            self.bulls8.set(self.bulls)
            cows = str(bc.cow_counter(self.number,guess))
            self.cows8.set(cows)
            if self.bulls=='4':
                self.update_avg_guesses()
            else:
                self.guess_number=9
                
        elif self.guess_number==7:
            # Run the game as above.
            self.other_guess_number=7
            guess = str(self.guess_entry.get())
            self.guess7.set(guess)
            guess = bc.player_input(guess)
            self.bulls = str(bc.bull_counter(self.number,guess))
            self.bulls7.set(self.bulls)
            cows = str(bc.cow_counter(self.number,guess))
            self.cows7.set(cows)
            if self.bulls=='4':
                self.update_avg_guesses()
            else:
                self.guess_number=8
                
        elif self.guess_number==6:
            # Run the game as above.
            self.other_guess_number=6
            guess = str(self.guess_entry.get())
            self.guess6.set(guess)
            guess = bc.player_input(guess)
            self.bulls = str(bc.bull_counter(self.number,guess))
            self.bulls6.set(self.bulls)
            cows = str(bc.cow_counter(self.number,guess))
            self.cows6.set(cows)
            if self.bulls=='4':
                self.update_avg_guesses()
            else:
                self.guess_number=7
                
        elif self.guess_number==5:
            # Run the game as above.
            self.other_guess_number=5
            guess = str(self.guess_entry.get())
            self.guess5.set(guess)
            guess = bc.player_input(guess)
            self.bulls = str(bc.bull_counter(self.number,guess))
            self.bulls5.set(self.bulls)
            cows = str(bc.cow_counter(self.number,guess))
            self.cows5.set(cows)
            if self.bulls=='4':
                self.update_avg_guesses()
            else:
                self.guess_number=6
                
        elif self.guess_number==4:
            # Run the game as above.
            self.other_guess_number=4
            guess = str(self.guess_entry.get())
            self.guess4.set(guess)
            guess = bc.player_input(guess)
            self.bulls = str(bc.bull_counter(self.number,guess))
            self.bulls4.set(self.bulls)
            cows = str(bc.cow_counter(self.number,guess))
            self.cows4.set(cows)
            if self.bulls=='4':
                self.update_avg_guesses()
            else:
                self.guess_number=5
                
        elif self.guess_number==3:
            # Run the game as above.
            self.other_guess_number=3
            guess = str(self.guess_entry.get())
            self.guess3.set(guess)
            guess = bc.player_input(guess)
            self.bulls = str(bc.bull_counter(self.number,guess))
            self.bulls3.set(self.bulls)
            cows = str(bc.cow_counter(self.number,guess))
            self.cows3.set(cows)
            if self.bulls=='4':
                self.update_avg_guesses()
            else:
                self.guess_number=4
                
        elif self.guess_number==2:
            # Run the game as above.
            self.other_guess_number=2
            guess = str(self.guess_entry.get())
            self.guess2.set(guess)
            guess = bc.player_input(guess)
            self.bulls = str(bc.bull_counter(self.number,guess))
            self.bulls2.set(self.bulls)
            cows = str(bc.cow_counter(self.number,guess))
            self.cows2.set(cows)
            if self.bulls=='4':
                self.update_avg_guesses()
            else:
                self.guess_number=3
                
        elif self.guess_number==1:
            # Run the game as above.
            self.other_guess_number=1
            guess = str(self.guess_entry.get())
            self.guess1.set(guess)
            guess = bc.player_input(guess)
            self.bulls = str(bc.bull_counter(self.number,guess))
            self.bulls1.set(self.bulls)
            cows = str(bc.cow_counter(self.number,guess))
            self.cows1.set(cows)
            if self.bulls=='4':
                self.update_avg_guesses()
            else:
                self.guess_number=2

    def update_avg_guesses(self):
        # Tell the player he's won and update the average guesses stat.
        self.notes.set('You win!')
        self.answer.set(''.join(self.number))
        # Calculate the total number of guesses required to win all of the
        # games played this session by adding the guess counter from this
        # game to the total from previous games.
        self.total_guesses = self.total_guesses + self.other_guess_number
        avg_guesses = str(self.total_guesses / self.times_played)
        # Update the avg_guesses label.
        self.avg_guesses.set(avg_guesses)

    def play_again(self):
        # Reset the guesses, bulls calculations, cows calculations, and other
        # relevant variables, plus generate a new number. Do not reset the
        # total number of guesses.

        # Keep track of the number of games that have been played.
        self.times_played = self.times_played + 1
        
        # Reset the guesses, bulls, and cows.
        self.guess1.set('')
        self.guess2.set('')
        self.guess3.set('')
        self.guess4.set('')
        self.guess5.set('')
        self.guess6.set('')
        self.guess7.set('')
        self.guess8.set('')
        self.guess9.set('')
        self.guess10.set('')

        self.bulls1.set('')
        self.bulls2.set('')
        self.bulls3.set('')
        self.bulls4.set('')
        self.bulls5.set('')
        self.bulls6.set('')
        self.bulls7.set('')
        self.bulls8.set('')
        self.bulls9.set('')
        self.bulls10.set('')

        self.cows1.set('')
        self.cows2.set('')
        self.cows3.set('')
        self.cows4.set('')
        self.cows5.set('')
        self.cows6.set('')
        self.cows7.set('')
        self.cows8.set('')
        self.cows9.set('')
        self.cows10.set('')

        self.notes.set('')
        self.answer.set('')

        # Reset the number that keeps track of what guess the player is on
        # in this round and this round only. Reset the bulls count.
        self.guess_number=1
        self.other_guess_number=0
        self.bulls=0

        # Generate a new number for the new round.
        self.number=bc.number_generator()
        
# Instantiate the class.  
myGui=MyGUI()
