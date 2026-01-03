import turtle


lamim = turtle.Turtle()
count = 0
def rec_func(length, depth):
    global count
    count = count+1
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

def int_polygon(edge_number, side_length, poly_angle, rec_depth):
    if(edge_number == 0):
        return
    rec_func(side_length,rec_depth)
    lamim.left(poly_angle)
    edge_number = edge_number-1
    int_polygon(edge_number, side_length, poly_angle, rec_depth)

edge_number = int(input("Enter the number of sides:"))
side_length = int(input("Enter the side length: "))
rec_depth = int(input("Enter the recursion depth: "))
poly_angle = int(360/edge_number)

int_polygon(edge_number, side_length, poly_angle, rec_depth)
    
print(count)

# lamim.color('red', 'yellow')  # pen color, fill color
# lamim.begin_fill()
# x,y = lamim.pos()

# while True:
#     lamim.forward(edge_size)
#     lamim.left(edge_angle)
#     if (abs(lamim.pos()))< 1:  # pos() gives the current (x, y) position
#         break
# # lamim.done()
# lamim.end_fill()



turtle.done()