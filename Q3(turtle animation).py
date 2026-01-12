import turtle

# Setup screen
screen = turtle.Screen()
screen.setup(width=600, height=600)


lamim = turtle.Turtle()
lamim.speed(0)
lamim.pencolor("red")

#To make the design as given in the task
def rec_func(length, depth):
    if(depth == 0):
        lamim.forward(length)
        return
    segment = length / 3
    rec_func(segment, depth - 1)
    lamim.left(60)
    rec_func(segment, depth - 1)
    lamim.right(120)
    rec_func(segment, depth - 1)
    lamim.left(60)
    rec_func(segment, depth - 1)

# Initial polygon for the design
def int_polygon(edge_number, side_length, poly_angle, rec_depth): 
    if(edge_number == 0):
        return
    rec_func(side_length,rec_depth)
    lamim.left(poly_angle)
    edge_number = edge_number-1
    int_polygon(edge_number, side_length, poly_angle, rec_depth)

# To check the value is int and it will keep asking input.
def check_input(value):
    input_data = input(value)
    if input_data.isdigit():
        return int(input_data)
    else:
        print("*** Please use a valid integer ***")
        return check_input(value)

edge_number = check_input("Enter the number of sides: ")
side_length = check_input("Enter the side length: ")
rec_depth = check_input("Enter the recursion depth: ")

# print (edge_number)
poly_angle = int(360/edge_number)

offset_x = -side_length / 2
offset_y = -side_length / 2

# To change the starting position and pen color
lamim.penup()
lamim.goto(offset_x, offset_y)
lamim.setheading(0)
lamim.pendown()

int_polygon(edge_number, side_length, poly_angle, rec_depth)

lamim.hideturtle()
turtle.done()



#References
#https://www.youtube.com/watch?v=pxKu2pQ7ILo  [Date: 04-01-2026]
#https://docs.python.org/3.3/library/turtle.html. [Date: 04-01-2026]
#https://www.w3schools.com/python/ref_module_turtle.asp. [Date: 04-01-2026]