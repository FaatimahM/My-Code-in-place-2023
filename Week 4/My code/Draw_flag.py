from graphics import Canvas
import random

CANVAS_WIDTH = 450
CANVAS_HEIGHT = 300

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    # canvas.create_rectangle(0,0, CANVAS_WIDTH, CANVAS_HEIGHT/2, 'red')
    
    canvas.create_line(0,150,450,150)
    canvas.create_rectangle(0, 75, 50, 150)
    

if __name__ == '__main__':
    main()
    