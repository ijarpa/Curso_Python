# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.


    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_width)
    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.

def draw_sky(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, scene_height /4, scene_width, scene_height, width=0, fill="coral2")

    sun_center_x = 400
    sun_bottom = scene_height/4
    sun_height = 390

    draw_sun(canvas, sun_center_x, sun_bottom, sun_height) 

# Clouds

    cloud_center_x = 700
    cloud_bottom = scene_height/1.5
    cloud_height = 200

    draw_clouds(canvas, cloud_center_x, cloud_bottom, cloud_height )
    
    cloud_center_x = 600
    cloud_bottom = scene_height/1.6
    cloud_height = 200

    draw_clouds(canvas, cloud_center_x, cloud_bottom, cloud_height )

    cloud_center_x = 750
    cloud_bottom = scene_height/1.7
    cloud_height = 200

    draw_clouds(canvas, cloud_center_x, cloud_bottom, cloud_height )

# Clouds 2

    cloud_center_x = 300
    cloud_bottom = scene_height/2.5
    cloud_height = 200

    draw_clouds(canvas, cloud_center_x, cloud_bottom, cloud_height )
    
    cloud_center_x = 200
    cloud_bottom = scene_height/2.6
    cloud_height = 200

    draw_clouds(canvas, cloud_center_x, cloud_bottom, cloud_height )

    cloud_center_x = 350
    cloud_bottom = scene_height/2.7
    cloud_height = 200

    draw_clouds(canvas, cloud_center_x, cloud_bottom, cloud_height )

# Clouds 3

    cloud_center_x = 400
    cloud_bottom = scene_height/1.3
    cloud_height = 200

    draw_clouds(canvas, cloud_center_x, cloud_bottom, cloud_height )
    
    cloud_center_x = 300
    cloud_bottom = scene_height/1.4
    cloud_height = 200

    draw_clouds(canvas, cloud_center_x, cloud_bottom, cloud_height )


def draw_ground(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, 0, scene_width, scene_height/5, width=0, fill="slateBlue4")
    
    # Draw a pine tree.   
    tree_center_x = 400
    tree_bottom = scene_height/5.05
    tree_height = 10

    for x in range (0, 500):
        draw_sun_reflect(canvas, tree_center_x,
                tree_bottom, tree_height)

        tree_center_x -= 2
        tree_bottom -= 1
        tree_height -= 2   


def draw_sun_reflect(canvas, center_x, bottom, height):
    trunk_width = bottom / 1.4
    trunk_height = height / 6
    trunk_left = center_x - trunk_width
    trunk_right = center_x + trunk_width
    trunk_top = bottom + trunk_height

    draw_rectangle(canvas, trunk_left, trunk_top, trunk_right, bottom, outline="orange", width=1, fill="orange")

def draw_sun(canvas, center_x, bottom, height):
    sun_width = height /3
    sun_height = height /1.7
    sun_left = center_x - sun_width
    sun_right = center_x + sun_width
    sun_top = bottom + sun_height

    draw_oval(canvas, sun_left, sun_top, sun_right, bottom, outline="orange", width=1, fill="orange")

def draw_clouds(canvas, center_x, bottom, height):
    cloud_width = height /6
    cloud_height = height /5
    cloud_left = center_x - cloud_width
    cloud_right = center_x + cloud_width
    cloud_top = bottom + cloud_height

    draw_oval(canvas, cloud_left, cloud_top, cloud_right, bottom, outline="red", width=1, fill="red")

    for x in range (0, 5):
        draw_oval(canvas, cloud_left, cloud_top, cloud_right, bottom, outline="red", width=1, fill="red")

        cloud_left -= 30
        cloud_right -= 30

     

# Call the main function so that
# this program will start executing.
main()


#    for x in range (0, 3):
#        draw_clouds(canvas, cloud_center_x, cloud_bottom, cloud_height)

#        cloud_center_x -= 50 