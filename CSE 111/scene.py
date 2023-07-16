# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py library
    # which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)
    draw_pine_tree(canvas, 550, 150, 250)
    draw_pine_tree(canvas, 350, 100, 150)
    draw_pine_tree(canvas, 175, 125, 200)
    draw_pine_tree(canvas, 750, 100, 150)


    for x in range(50, 800, 100):
        draw_pine_tree(canvas, x, 0, 80)

    for i in range(100, 750, 100):
        draw_pine_tree(canvas, i, 50, 80)


    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.
def draw_sky(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, scene_height / 5, scene_width, scene_height, width=0, fill="deepSkyBlue")
    sun = draw_oval(canvas, 50, 100, 300, 200, outline="darkOrange1", fill="darkOrange1")
    moon = draw_oval(canvas, 700, 400, 800, 500, outline="ivory3", fill="ivory3")
    center_cloud = draw_oval(canvas, 250, 350, 350, 400, outline="ghostWhite", fill="ghostWhite")
    cloud_left = draw_oval(canvas, 225, 375, 325, 450, outline="ghostWhite", fill="ghostWhite")
    cloud_right = draw_oval(canvas, 300, 375, 375, 450, outline="ghostWhite", fill="ghostWhite")
    cloud_bottom = draw_oval(canvas, 275, 325, 325, 375, outline="ghostWhite", fill="ghostWhite")
   
   #Right screen cloud
    cloud_center2 = draw_oval(canvas, 550, 250, 650, 300, outline="ghostWhite", fill="ghostWhite")
    cloud_left2 = draw_oval(canvas, 550, 225, 600, 325, outline="ghostWhite", fill="ghostWhite")
    cloud_vertical2 = draw_oval(canvas, 575, 240, 640, 310, outline="ghostWhite", fill="ghostWhite")
    
def draw_pine_tree(canvas, center_x, bottom, height):
    #tree trunk
    trunk_width = height / 10
    trunk_height = height / 8
    left_trunk = center_x - trunk_width / 2
    bottom_trunk = bottom
    right_trunk = center_x + trunk_height / 2
    trunk_top = bottom + trunk_height
    draw_rectangle(canvas, left_trunk, bottom_trunk, right_trunk, trunk_top, fill="saddleBrown")


    #draw tree top
    skirt_width = height / 2
    skirt_left = center_x - skirt_width / 2
    skirt_bottom = trunk_top
    peak_x = center_x
    peak_y = bottom + height
    skirt_right = center_x + skirt_width / 2
    draw_polygon(canvas, skirt_left, skirt_bottom, peak_x, peak_y, skirt_right, skirt_bottom, fill="darkGreen")


def draw_ground(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, 0, scene_width, scene_height / 3, width=0, fill="green2")

# Call the main function so that
# this program will start executing.
main()