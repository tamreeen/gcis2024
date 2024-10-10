"""Done By: Tamreen, Ribbiyoon, Ziad"""


from turtle import Screen, Turtle

PIXEL_SIZE = 30
ROWS = 20
COLUMNS = 20
DEFAULT_PEN_COLOR = 'black'
DEFAULT_PIXEL_COLOR = 'white'

def initialization(turta):
    '''Function which sets the speed, pencolor and the starting point of the turtle to start drawing'''
    turta.speed(0)
    turta.penup()
    turta.goto(-PIXEL_SIZE * COLUMNS / 2, PIXEL_SIZE * ROWS / 2) # initial coordinate of the turtle to begin drawing
    turta.setheading(0)
    turta.pendown()
    turta.pencolor(DEFAULT_PEN_COLOR)
    turta.fillcolor(DEFAULT_PIXEL_COLOR)




""" PART 1 DONE BY TAMREEN
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
        return 'none'  


""" Done By ribbiyoon:
This function is going to draw a pixel. turta represents the turtle object to draw the pixel, and color is used for filling the color of the pixel
we are not specifying the colors because we are going to use the get_colors
"""
def picture_pixel(turta, color):
    
  
    turta.fillcolor(color)  # Pixel fill color
    turta.begin_fill()  # Start filling the square
    turta.pendown()  # Lower the pen to draw

     #a pixel has 4 equal sides, so we will use the range function which only accept integers to draw 4 sides
    # Draw a square pixel
    for _ in range(4):  # Repeat 4 times (for 4 sides of the square)
        turta.forward(PIXEL_SIZE)
        turta.right(90)

    turta.penup()  # Lift pen up again
    turta.end_fill()  # Finish filling the square
    turta.forward(PIXEL_SIZE)  # Move the turtle to the right for the next pixel

""" Done By Ziad
This is the main function that will draw the pixels picture from the file, filename is used in the place of the name of the file"""

def picturefromfile(turta, filename):
    '''
    This function reads a file with color codes and draws the grid based on it.
    '''
    try: # try block is used to handle errors
        with open(filename, 'r') as file:  # r means the file will be in read mode
            for picture in file:  # Loop through each line in the file
                picture = picture.strip()  # Remove any extra whitespace or newlines

                for color in picture: # we want to fill the color of the pixel so we will use for loop so it runs thru each pixel
                    pixelcolor = get_color(color)  # Get the color for each pixel
                    picture_pixel(turta, pixelcolor)  # Draw the pixel with the turtle

                # Move to the next row
                turta.goto(-PIXEL_SIZE * COLUMNS / 2, turta.ycor() - PIXEL_SIZE)  
            """after one pixel is drawn, it will go to the x position and y coordinate - pixel size, to go one pixel down
            we didn't specify the ycoordinate because it is a fixed position"""
            
           
            # The except block specifies what to do if a particular error occurs in the try block.   
    except FileNotFoundError: # in this case it will use file found error
        print("Error: The file", filename, "was not found")

# Main function to initialize and start the drawing
def main():
    
    filename = input("Enter the file name: ")  # e.g: 'drawing01.txt'
    screen = Screen()  # Set up the screen
    turta = Turtle()  # Create turtle object

    initialization(turta)  
    picturefromfile(turta, filename)  # Draw the picture

    screen.exitonclick()  # Wait for a click to exit

if __name__ == "__main__":
    main()
