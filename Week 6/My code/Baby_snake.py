from graphics import Canvas
import time
import random
    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 420
SIZE = 20
INITIAL_VELOCITY = 20

START_X = 0
START_Y = 0

# if you make this larger, the game will go slower


def main():
    DELAY = 0.1 
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # draw the goal square
    x_random = random.randrange(0, 360, 20)
    y_random = random.randrange(0,360, 20)
    goal = canvas.create_rectangle(x_random, y_random, x_random + SIZE, y_random + SIZE, 'red')  
    
    
    x_velocity = INITIAL_VELOCITY
    y_velocity = INITIAL_VELOCITY
    
    square_x = START_X
    square_y = START_Y
    
    player = canvas.create_rectangle(square_x, square_y, square_x + SIZE,square_y + SIZE,'blue')
    
    x_direction = 1
    y_direction = 0
    
    score = 0
    
    # canvas.create_text(150,400,f'SCORE: {score}', font_size = 20)
    while True:
    
        
        # canvas.moveto(player, square_x, square_y)
        # time.sleep(DELAY)
        key = canvas.get_last_key_press()
        if key == 'ArrowDown':

            x_direction = 0
            y_direction = +1
        
        if key == 'ArrowRight':
            x_direction = +1
            y_direction = 0
        
        if key == 'ArrowLeft':
            x_direction = -1
            y_direction = 0
        
        if key == 'ArrowUp':
            x_direction = 0
            y_direction = -1
        
        canvas.move(player,x_direction*SIZE, y_direction*SIZE)
        x = canvas.get_left_x(player)
        y = canvas.get_top_y(player)
        
        # check if player hits the walls
        if x<0 or x>= 380:
            canvas.moveto(goal, -20, -20)
            canvas.moveto(player, -20, -20)
            text = canvas.create_text(50,150, text= 'GAME OVER 🥹', font_size = 40)
            break
        
        if y < 0 or y>= 380:
            canvas.moveto(goal, -20, -20)
            canvas.moveto(player, -20, -20)
            canvas.create_rectangle(x_random, y_random,x_random + SIZE, y_random + SIZE, 'white')
            text = canvas.create_text(50,180, text= 'GAME OVER 🥹', font_size = 40)
            break
        
        # if the player eats the goal
        if x == x_random and y == y_random:
            score += 20
            DELAY -= 0.001
            
            # generate a new goal
            x_random = random.randrange(0, 360, 20)
            y_random = random.randrange(0,360, 20)
            
            canvas.moveto(goal,x_random, y_random)
        
        canvas.create_rectangle(0,400,400,420,'white') 
        canvas.create_text(150,400,f'SCORE: {score}', font_size = 20)
        time.sleep(DELAY)
        
        

      
        
        

if __name__ == '__main__':
    main()