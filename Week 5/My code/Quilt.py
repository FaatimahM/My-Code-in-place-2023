from graphics import Canvas

##1fbfb8, #05716c, #1978a5, #031163
# each patch is a square with this width and height:
PATCH_SIZE = 100
CANVAS_WIDTH = PATCH_SIZE * 4
CANVAS_HEIGHT = PATCH_SIZE * 2

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    # draw the first row of patches
    draw_square_patch(canvas, 0, 0)
    draw_circle_patch(canvas, PATCH_SIZE, 0)
    draw_square_patch(canvas, PATCH_SIZE*2, 0)
    draw_circle_patch(canvas, PATCH_SIZE*3, 0)
    # TODO: your code here
    
    # draw second row of patches
    draw_circle_patch(canvas, 0, PATCH_SIZE)
    draw_square_patch(canvas, PATCH_SIZE, PATCH_SIZE)
    draw_circle_patch(canvas, PATCH_SIZE*2, PATCH_SIZE)
    draw_square_patch(canvas, PATCH_SIZE*3, PATCH_SIZE)    
    
    draw_small_square_patches(canvas,0,0 )
    draw_small_square_patches(canvas, PATCH_SIZE*2, 0)
    draw_small_square_patches(canvas, PATCH_SIZE, PATCH_SIZE)
    draw_small_square_patches(canvas, PATCH_SIZE*3, PATCH_SIZE)
    
    draw_heart(canvas,0,0)
    
def draw_circle_patch(canvas, start_x, start_y):
    
    end_x =start_x + PATCH_SIZE
    end_y = start_y + PATCH_SIZE
    canvas.create_oval(start_x, start_y,end_x, end_y, '#aed6dc'  )
    

def draw_square_patch(canvas, start_x, start_y):
    # draws a purple frame at (start_x, start_y)
    end_x = start_x + PATCH_SIZE
    end_y = start_y + PATCH_SIZE
    inset = 20
    # first draw a purple square over the entire patch
    canvas.create_rectangle(start_x, start_y, end_x, end_y, '#00154f')
    # then draw a smaller white square on top
    canvas.create_rectangle(start_x+inset, start_y+inset, 
        end_x-inset, end_y-inset, '#aed6dc')

def draw_small_square_patches(canvas, start_x, start_y):
    inset = 20
    
    #top left small square
    tl_end_x = start_x + inset
    tl_end_y = start_y + inset
    canvas.create_rectangle(start_x, start_y, tl_end_x, tl_end_y, '#f4898b')
    
    #bottom right small square
    bl_start_x = start_x + inset*4
    bl_start_y = start_y + inset*4
    
    bl_end_x = start_x + inset *5
    bl_end_y = start_y + inset *5
    canvas.create_rectangle(bl_start_x, bl_start_y,bl_end_x,bl_end_y, '#f4898b')

def draw_heart(canvas,start_x, start_y):
    canvas.create_text(start_x + 45, start_y+45, '❤')
    
    
if __name__ == '__main__':
    main()