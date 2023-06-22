from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    
    #Walk along walls
    while front_is_clear():
    
        while facing_east():
            
            if beepers_present():
                pass
            else:
                put_beeper()
                
            move()
            
            if front_is_blocked():
                put_beeper()
                turn_left()
                turn_left()
            
        while facing_west():
            move()
            
            if front_is_blocked():
                turn_right()
                
                if front_is_clear():
                    move()
                    turn_right()
                else:    
                    turn_right()
                    while facing_east() and front_is_clear():
                        move()
        
        

    
def turn_right():
    for i in range(3):
        turn_left()


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()