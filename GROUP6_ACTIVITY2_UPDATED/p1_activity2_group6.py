""" Done By Tamreen, Ziad, Ribbiyoon
This is part 1, part 2 of the main program where the user enters the text file 
to draw different grids is the second python file.
"""
from turtle import Screen, Turtle

PIXEL_SIZE = 30  # Size of each pixel
ROWS = 20  # Number of rows in the grid
COLUMNS = 20  # Number of columns in the grid
DEFAULT_PEN_COLOR = 'black'  # Default pen color for drawing
DEFAULT_PIXEL_COLOR = 'white'  # Default fill color for pixels

def initialization(turta):
    
    turta.speed(0)  # Set turtle drawing speed to the fastest
    turta.penup()  # Lift the pen to move without drawing
    turta.goto(-PIXEL_SIZE * COLUMNS / 2, PIXEL_SIZE * ROWS / 2)  # Start position
    turta.setheading(0)  # Point turtle to the right (default)
    turta.pendown()  # Lower the pen to start drawing
    turta.pencolor(DEFAULT_PEN_COLOR)  # Set the pen color
    turta.fillcolor(DEFAULT_PIXEL_COLOR)  # Set the default fill color for pixels

""" PART 1 DONE BY tamreen
return statement is used to send a value back when the function is called 
== used if both values are equal
if statement will only work if the condition is true, otherwise it will to to the other statements"""

def get_color(color):
    
    if color == '0':
        return 'black'
    elif color == '1':
        return 'white'
    elif color == '2':
        return 'red'
    elif color == '3':
        return 'yellow'
    elif color == '4':
        return 'orange'
    elif color == '5':
        return 'green'
    elif color == '6':
        return 'yellowgreen'
    elif color == '7':
        return 'sienna'
    elif color == '8':
        return 'tan'
    elif color == '9':
        return 'gray'
    elif color == 'A':
        return 'sienna'
    else:
        print("wrong color code")
        return 

""" done by Ziad and Ribbiyoon, this function draws the entire row of pixels filled with get colors"""
def pixels(turta):
    
    
    #Ziad: Loop that will run through each row, ROWS is a global variable which has 20 rows
    for line in range(ROWS):
        
        row_colors = "0123456789A0123456789A"  # Ziad: this is the string that holds the colors from get colors
        
        # Done By Ribbiyoon: a pixel shape will be drawn in each row
        for color_code in row_colors:
            color = get_color(color_code)  # will take the color from get_colors
            turta.fillcolor(color)  # to fill color for the pixel
            turta.begin_fill()  # Start filling the square
            turta.pendown()  # to put the pen down to draw
            
            # Draw a square pixel
            for _ in range(4): # a square has 4 sides
                turta.forward(PIXEL_SIZE) # size of the pixel
                turta.right(90)
            
            turta.penup()  # Lift the pen to stop drawing
            turta.end_fill()  # Finish filling the square
            turta.forward(PIXEL_SIZE)  # Move to the next pixel position
        
        
        turta.goto(-PIXEL_SIZE * COLUMNS / 2, turta.ycor() - PIXEL_SIZE)

        """ Done By Ziad: the turta.goto has been taken from the initialization, however we need to move to the 
            next row to draw a new set of pixels so we will subtract pixel size by moving 1 box down of pixels ( y coordinate) """


def main():
    turta = Turtle()  
    initialization(turta)  
    pixels(turta)  # pixels
    shapescreen = Screen()  # Create the screen
    shapescreen.exitonclick()  # Keep the window open until clicked

if __name__ == "__main__":
    main()
