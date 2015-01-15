# Adam Jaffe
# amj2158
# February 23, 2013
# Professor Cannon
# file: position_calculator.py

# This program calculates vertical position when given an initial vertical
# velocity and a time after launch.

def position_iteration():
    ' ' 'This iterates the position function and produces a final position.' ' '
    global pos
    pos=0
    global vel
    vel=input('What is the initial vertical velocity of the projectile?')
    global time
    time=input('How long has the projectile been in the air?')
    global bad_position
    bad_position=vel*time - 4.905*time**2

    # n represents the number of iterations necessary to calculate a final
    # height.
    
    n=int(time/.005)

    # The while loop allows the program to terminate early if the projectile
    # has already returned to the ground.
    
    again=0
    while(again==0):
        for t in range(0,n+1,1):
            acceleration(pos)
            grav=acceleration(pos)
            velocity(vel,grav)
            vel=velocity(vel,grav)
            position(pos,vel)
            pos=position(pos,vel)

            # When t%200=0, one full second has passed.
            
            if t!=0 and t%200==0:
                print pos

            # This accounts for when the projectile returns to the ground.
            
            if pos<=0:
                pos=0
                again=1
        again=1
        
def acceleration(pos):
    ' ' 'This calculates gravitational acceleration as it changes with height.' ' '
    return float(3.98439e14/((6371000+pos)**2))

def velocity(vel,grav):
    ' ' 'This calculates velocity based on acceleration and prior velocity.' ' '
    return vel-grav*.005

def position(pos,vel):
    ' ' 'This calculates height based on prior position and velocity.' ' '
    return pos+vel*.005

def main():
    ' ' 'This is the main operating function.' ' '
    position_iteration()
    print 'After',time,'second(s), the projectile is',pos,'meters above ground.'
    print 'A less accurate position estimate is',bad_position,'meters.'

# Call the main function.

main()
