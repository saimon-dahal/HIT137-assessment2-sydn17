import turtle

lamim = turtle.Turtle()
# To change the starting position and pen color
lamim.penup()
lamim.goto(-200,-200)
lamim.pencolor("red")
lamim.pendown()

#To make the design as given in the task
def rec_func(length, depth):
    if(depth == 0):
        lamim.forward(length)
        return
    segment = length / 4
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

int_polygon(edge_number, side_length, poly_angle, rec_depth)

turtle.done()



#References
#https://www.youtube.com/watch?v=pxKu2pQ7ILo  [Date: 04-01-2026]
#https://docs.python.org/3.3/library/turtle.html. [Date: 04-01-2026]
#https://www.w3schools.com/python/ref_module_turtle.asp. [Date: 04-01-2026]