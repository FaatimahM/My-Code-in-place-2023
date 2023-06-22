from karel.stanfordkarel import *

"""
File: PuzzleKarel.py
--------------------
Karel should finish the puzzle by picking up the last beeper 
(puzzle piece) and placing it in the right spot. Karel should 
end in the same position Karel starts in -- the bottom left 
corner of the world.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    move_and_pick_up()
    put_piece_in_place()
    return_to_original_position()
    
    
    
def move_and_pick_up():
    for i in range(2):
        move()
    pick_beeper()    
        
def put_piece_in_place():
    move()
    turn_left()
    move_2_times()
    put_beeper()
    
        
def turn_right():
    for i in range(3):
        turn_left()

def return_to_original_position():   
    turn_left()
    turn_left()
    move()
    turn_right()
    move_2_times()
    move()
    turn_left()
    move()
    turn_left()

        


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()