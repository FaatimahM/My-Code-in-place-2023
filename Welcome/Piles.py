from karel.stanfordkarel import *

# File: piles.py
# -----------------------------
# The warmup program defines a "main"
# function which should make Karel
# pick up all the beepers in the world.
def main():
  move()
  pick_times_10()
  move()
  move()
  pick_times_10()
  move()
  move()
  pick_times_10()
  move()
   
    
    # your code here

def pick_times_10():
    for i in range(10):
        pick_beeper()
   
   
   
# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()