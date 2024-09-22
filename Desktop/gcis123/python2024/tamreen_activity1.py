from turtle import Turtle, Screen
 
""" we used the input function to to ask the user to enter the data they want,
     we used the int() function to convert the user's input to a whole number """

# user should write the color of the table

 # table color
table_color = input("enter the color of the table: ")


# size of table
table_width = int(input("please enter the width of the table which is the horizontal line(200-500): "))
table_length = int(input("please enter the length of the table, which is the vertical side of a table(10-100):"))
table_legs = int(input("enter the size of table legs: "))


# cake
length_cake = int(input("enter size of the length of cake, which is the vertical line(10-50) note that the cake should be smaller then the length of table: ")) 
width_cake = int(input("enter the width of your cake, which is the horizontal line(100-200): "))


# color of cake
layer1color = input("enter the color of layer 1 cake: ")
layer2color = input("enter the color of layer 2 cake: ")
layer3color = input("enter the color of layer 3 cake: ")


# color of decoration ball
size_of_decoration = input("enter the size of the ball of the cake ( 10 - 15 is recommended) ")
decoration = input("enter color of the decoration ball: ")

# global variables
message = "your cake is loading! Happy Birthday"
message2 = "press any key to exit"

# creates a Turtle object
t = Turtle()

""" def is used to define a function, which is the table in this case, inside the table is a lot of parameters that will combined
together to create a table"""

def table(t,width,height,color,length):
     t.fillcolor(color) # fills the color for the table
     t.begin_fill() # begins filling
     t.penup() # draws without tracing
     t.goto(0,0) # starting position
    
     """ t: The turtle object used to draw. width: The width of the table. height: The height of the table. 
        color: The color of the table. length: The length of the table legs. 
     """

     
     t.pendown() # starts drawing with tracing
     t.forward(width) # horizontal line for the table
     t.right(270) # turns to the other side
     t.forward(height) # vertical line for the table
     t.left(90)
     
     t.forward(width)
     t.left(90)
     t.forward(height)
     t.left(90)
     t.forward(width)
     t.right(90)
    
     t.forward(length) # thts when u draw the length of the legs of the table
     t.right(90)
     t.forward(20) # bottom horizontal line for table legs
     t.right(90)
     t.forward(length)
     t.end_fill()
     t.penup()
     t.goto(0,0) # the end leg is done, turtle comes back home

     t.left(180)
     t.pendown()
     t.fillcolor(color)
     t.begin_fill()
     t.forward(length)
     
     t.left(90)
     t.forward(20)
     t.left(90)
     t.forward(length)
     t.goto(0,0)
     t.forward(height)
     t.forward(length)
     t.right(90)
     t.forward(20)
     t.left(270)
     t.forward(length)
     t.end_fill()
     
     t.penup()
     t.right(90)
     t.forward(20)
     t.left(180)
     t.pendown()

     t.fillcolor(color)
     t.begin_fill()
     t.forward(width)
     t.left(90)
     t.forward(length)
     t.left(90)
     t.forward(20)
     t.right(270)
     t.forward(length)
     t.right(90)
     t.end_fill() 
     t.penup()
     t.goto(0,0)
     


# The candle function
def candle(t, width_of_cake): 
    """ the turtle will draw a candle on top of the cake.
    
    t: The turtle object used to draw.

    width_of_cake: The width of the cake is used here to position the candle, so the candle can be on top of the width of the cake,
    we did not specify the candle's location because the user will enter the width of the cake randomly, so since we need to make
    sure the candle is on the cake so we will place the candle by moving forward in the width of cake but it will be divided by 4,
    in order to place the candle."""
    
    t.fillcolor("yellow") # candle's color
    t.begin_fill()
    t.up()
    t.forward(width_of_cake // 4 )
    """ Position for the candle, since it is not mentioned about the specific location of candle in rubrics, we decide
     to place in any random place on the cake"""
   
    t.down()
    
    t.forward(20)  # Candle width
    t.left(90)
    t.forward(50)  # Candle height
    
   
    t.circle(10, -180)  # Rounded top of the candle
    t.forward(50)
    
    t.end_fill() 




# The flame function
def flame(t):
    t.penup()
    t.setheading(90)
    t.forward(50)  # Move to the top of the candle
    t.right(90)
    
    t.pendown()
    
    t.fillcolor("orange")
    t.begin_fill()
    
    # Draw the triangle (flame)
    for _ in range(3): # will draw the sides of the candle 3 times
        t.forward(20)  # Length of the flame side
        t.left(120)  # Turn 120 degrees to make an equilateral triangle
    
    t.end_fill()

"""Draws a layer of cake.
        t: The turtle object used to draw.
        width_of_cake: The width of the cake layer.
        length_of_cake: The length of the cake layer.
        color: The color of the cake layer.
"""

def cake_layer(t, width_of_cake, length_of_cake, color):
    t.fillcolor(color) 
    t.begin_fill()
    t.pendown()
    
    for _ in range(2):  # it will draw a rectangle for the cake layer, since rectangle has 2 widths and 2 length so in range it is wrotten 2
        t.forward(width_of_cake )  # horizontal line
        t.right(90)
        t.forward(length_of_cake) # vertical line of cake
        t.right(90)

    
    t.end_fill()
    

""" this function is used to make the program smaller and easier to read, we did not place it in the main because it will make the code
longer, and in case we decide to draw another cake or a candle, we just have to write the function name instead of rewriting all 
the parameters """

def drawing_time(t, width, height, color, length, width_of_cake, length_of_cake, layer1color, layer2color,layer3color,size_of_ball,
                 decoration_ball):
    
    table(t, width, height, color, length)
    
    #after table is done, the cake will be drawn

    # Draw layer 1
    t.penup()
    t.goto((width // 4), height)  # width of table is x axis, which is divided by 4 and height is table y axis 
    t.setheading(0)  # Face right 
    cake_layer(t, width_of_cake, length_of_cake, layer1color)

    # Draw layer 2 above layer 1
    t.penup()
    t.goto((width // 4) , height + length_of_cake)  # Move above the first layer
    t.setheading(0)  # Face right
    cake_layer(t, width_of_cake, length_of_cake, layer2color)

    t.penup()
    t.goto((width // 4), height + length_of_cake + length_of_cake)  # Move above the second layer
    t.setheading(0)  # Face right
    cake_layer(t, width_of_cake, length_of_cake, layer3color)
    t.forward(width_of_cake // 4)

    t.fillcolor(decoration_ball)
    t.begin_fill()
    t.circle(size_of_ball) # size of decoration ball
    t.end_fill()

    # candle(t,width_of_cake,locationcandle)
    candle(t,width_of_cake)
    flame(t)
    


# main function that will start drawing on the screen
def main():
    shapesscreen = Screen() # this will create a screen for drawing
    shapesscreen.screensize(500,500) # size of the screen
    print(message)
    drawing_time(t, table_width, table_length, table_color, table_legs, width_cake, length_cake, layer1color, layer2color, layer3color, 
           size_of_decoration, decoration)  # will draw all functions one by one in order
    print(message2) # this will print the message
    
    shapesscreen.exitonclick() # this will exist the screen after the user clicks

main() # runs the main function

