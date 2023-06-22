from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should have repaired 
each of the columns in the temple
"""

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    for i in range(2):
    
        turn_left()
        build_column()
        turn_right()
        put_beeper()
        
        move_4_times()
        
        turn_right()
        build_column()
        turn_left()
        put_beeper()
        
        if front_is_clear():
            move_4_times()
        else:
            pass
        
            
        
        # turn_left()
        # build_column()
        # turn_right()
        # put_beeper()
        
        # move_4_times()
    
        # turn_right()
        # build_column()
        # turn_left()
        # put_beeper()
        
    
    

    
    
def build_column():
    for i in range(4):
        put_beeper()
        move()
        
def move_4_times():
    for i in range(4):
        move()

def turn_right():
    for i in range(3):
        turn_left()
    
if __name__ == '__main__':
    main()