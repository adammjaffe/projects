def main():
    ' ' 'This executes the PPM manipulating program.' ' '
    print 'Welcome to the Portable Pixmap (PPM) Editor.'
    infile=open(raw_input('Input file name:'), 'r')
    temp_file=open('temp.txt', 'w')
    
    # Copy the header with important information into the temp_file. Save the
    # important information for use in later functions and calculations.
    line1=infile.readline()
    line2=infile.readline()
    line3=infile.readline()
    columns_rows_list=line2.split()
    num_columns=int(columns_rows_list[0])
    num_rows=int(columns_rows_list[1])
    row_length=3*num_columns

    # Write the lines of the header.
    temp_file.write(line1)
    temp_file.write(line2)
    temp_file.write(line3)

    # The program will copy the input file piece by piece in sections called
    # buffers. The user can pick the size of the buffer.
    size=int(raw_input('How large should the buffer be?'))

    # Determine if the buffer size is big enough; if it is, proceed.
    if row_length > size:
        print 'Sorry, the buffer size is too small to support this file.'
    else: 
        # Create an interactive menu for the user and print the menu.
        print ' '
        print '         MENU   '
        print '1) Convert to greyscale'
        print '2) Flip horizontally'
        print '3) Negative of red'
        print '4) Negative of green'
        print '5) Negative of blue'
        print '6) Just the reds'
        print '7) Just the greens'
        print '8) Just the blues'
        print '9) Extreme contrast'
        print '10) Random noise'
        print ' '

        # Take several commands from the user at once. Break those commands
        # into a list; later, each command that appears in the list will 
        # call a certain function.
        choices=raw_input('Pick as many numbers as you want; '\
                          'separate your choices with a space:')
        choices_list=choices.split()

        # This section reads an entire row, performs the requested
        # transformations, and returns for the next row.

        # Two Boolean flags are created to ensure that the error message
        # prints only once. 
        boolean=False
        again=1

        for i in range(0,num_rows):
            # Create (or reset) an empty row to be filled with the data
            # from one horizontal row of pixels.
            whole_row=[]
            
            while len(whole_row)<row_length:
                # Read each line and convert it to a list.
                temp_line=infile.readline()
                temp_line=temp_line.split()
                
                # Add each piece in that list to the whole_row variable.
                for j in range(0,len(temp_line)):
                    whole_row.append(temp_line[j])

            # Once the row is filled, perform the requested functions.
            if '1' in choices_list:
                whole_row=grey_scale(whole_row,row_length)
                boolean=True
            if '2' in choices_list:
                whole_row=flip_horizontal(whole_row,row_length)
                boolean=True
            if '3' in choices_list:
                max_value=int(line3)
                whole_row=negate_red(whole_row,max_value)
                boolean=True
            if '4' in choices_list:
                max_value=int(line3)
                whole_row=negate_green(whole_row,max_value)
                boolean=True
            if '5' in choices_list:
                max_value=int(line3)
                whole_row=negate_blue(whole_row,max_value)
                boolean=True
            if '6' in choices_list:
                whole_row=flatten_blue(whole_row)
                whole_row=flatten_green(whole_row)
                boolean=True
            if '7' in choices_list:
                whole_row=flatten_red(whole_row)
                whole_row=flatten_blue(whole_row)
                boolean=True
            if '8' in choices_list:
                whole_row=flatten_red(whole_row)
                whole_row=flatten_green(whole_row)
                boolean=True
            if '9' in choices_list:
                max_value=int(line3)
                whole_row=extreme_contrast(whole_row,max_value)
                boolean=True
            if '10' in choices_list:
                max_value=int(line3)
                whole_row=random_noise(whole_row,max_value)
                boolean=True
            if boolean==False and again==1:
                print 'The program has shut down; formatting may be wrong.' \
                        ' Restart and make sure to at least one number 1-10.'
                again=0
                
            # To prevent warping on the right edge (which comes when the
            # characters aren't properly spaced), add separation between
            # the digits in the file. New line characters are not
            # necessary. Write the spaced form directly into the temp_file.
            for k in whole_row:
                temp_file.write(k+' ')
            
            # Reset the whole_row variable to be empty before the next row
            # is processed.
            whole_row=[]

        # Close the read and write files.
        infile.close()
        temp_file.close()

        # Change the name of the temp_file to the name specified by the
        # user.
        if again==1:
            name_changer()

def name_changer():
    ' ' 'This changes the name of the temporary file to the name chosen.' ' '
    import os
    os.rename('temp.txt',raw_input('Output file name:'))
    print 'The new file has been created.'

def grey_scale(whole_row,row_length):
    ' ' 'This converts the image to greyscale by averaging pixel values.' ' '
    # Create a list of three characters to differentiate pixels.
    pixel=[0,0,0]
    
    # Differentiate the row by pixels, find their average value, and replace
    # each component with the average.
    for n in range(0,row_length,3):
        pixel[0]=int(whole_row[n])
        pixel[1]=int(whole_row[n+1])
        pixel[2]=int(whole_row[n+2])
        average=str(int(sum(pixel)/3))
        whole_row[n]=average
        whole_row[n+1]=average
        whole_row[n+2]=average

    return whole_row

def flip_horizontal(whole_row,row_length):
    ' ' 'This flips the image horizontally by rearranging pixels.' ' '
    # Create an empty list for each pixel and an empty list for the row.
    pix=[0,0,0]
    empty_row=[]
    # Write the pixels into the new row as strings of three integers.
    for n in range(0,row_length,3):
        pix[0]=str(int(whole_row[n]))
        pix[1]=str(int(whole_row[n+1]))
        pix[2]=str(int(whole_row[n+2]))
        pixel=' '.join(pix)
        empty_row.append(pixel)
        
    # Once the row is full, swap positions of the pixels, write the
    # row to the temporary file, and reset the whole_row variable.
    max_pos=len(empty_row)-1
    for m in range(0,(len(empty_row)/2)):
        new_pos=max_pos-m
        temp_store_one=empty_row[m]
        temp_store_two=empty_row[new_pos]
        empty_row[m]=temp_store_two
        empty_row[new_pos]=temp_store_one

    # Reassign the whole_row variable as the flipped version empty_row
    whole_row=empty_row

    # Convert the whole_row back into a list of strings for use in other
    # functions.
    whole_row=' '.join(whole_row)
    whole_row=whole_row.split()
    
    return whole_row
        
def negate_red(whole_row,max_value):
    ' ' 'This negates the red value of each pixel.' ' '
    for n in range(0,len(whole_row),3):
        # Every third value, compare to the max_value, negate it,
        # remove the original and replace it with a negated one.
        replacement_value = max_value - int(whole_row[n])
        whole_row[n]=str(replacement_value)

    return whole_row

def negate_green(whole_row,max_value):
    ' ' 'This negates the green value of each pixel.' ' '
    # Works the same as negate_red, just with minor adjustments for position.
    for n in range(1,len(whole_row),3):
        # Every third value, compare to the max_value, negate it,
        # remove the original and replace it with a negated one.
        replacement_value = max_value - int(whole_row[n])
        whole_row[n]=str(replacement_value)

    return whole_row

def negate_blue(whole_row,max_value):
    ' ' 'This negates the blue value of each pixel.' ' '
    # Works the same as negate_red, just with minor adjustments for position.
    for n in range(2,len(whole_row),3):
        # Every third value, compare to the max_value, negate it,
        # remove the original and replace it with a negated one.
        replacement_value = max_value - int(whole_row[n])
        whole_row[n]=str(replacement_value)

    return whole_row

def flatten_red(whole_row):
    ' ' 'This sets the red value of each pixel to 0.' ' '
    for n in range(0,len(whole_row),3):
        # Every third value (starting with the first red value) is set to 0.
        whole_row[n]=str(0)

    return whole_row

def flatten_green(whole_row):
    ' ' 'This sets the green value of each pixel to 0.' ' '
    for n in range(1,len(whole_row),3):
        # Every third value (starting with the first green value) is set to 0.
        whole_row[n]=str(0)

    return whole_row

def flatten_blue(whole_row):
    ' ' 'This sets the blue value of each pixel to 0.' ' '
    for n in range(2,len(whole_row),3):
        # Every third value (starting with the first blue value) is set to 0.
        whole_row[n]=str(0)

    return whole_row

def extreme_contrast(whole_row,max_value):
    ' ' 'This maximizes all color values above half the maximum and sets' ' ' \
      ' ' 'all other values to zero.' ' '
    # Make variables that describe relevant values.
    half_max=max_value/2
    string_max=str(max_value)

    # Compare each value to the half_max and set it to an extreme.
    for i in range(0,len(whole_row)):
        if int(whole_row[i])>half_max:
            whole_row[i]=string_max
        else:
            whole_row[i]='0'

    return whole_row

def random_noise(whole_row,max_value):
    ' ' 'This adds a random value to each color value.' ' '
    # Import the random function.
    import random as r

    new_max=max_value+1
    
    # Pick a random value between 0 and the maximum to serve as the range.
    max_random=r.randrange(0,new_max,1)

    # For each value in the row, calculate a random noise value and a value
    # to determine whether to add or subtract. 
    for i in range(0,len(whole_row)):
        noise_value=r.randrange(0,new_max,1)
        add_or_subtract=r.randrange(0,2)
        if add_or_subtract==0:
            whole_row[i]=str(int(whole_row[i])+noise_value)
            # If the new value is greater than the max value, the
            # new value resets to the max value.
            if int(whole_row[i])>max_value:
                whole_row[i]=str(max_value)
        if add_or_subtract==1:
            whole_row[i]=str(int(whole_row[i])-noise_value)
            # If the new value is less than zero, the new value resets to zero.
            if int(whole_row[i])<0:
                whole_row[i]='0'

    return whole_row
            
# Call the main executing function.
main()
