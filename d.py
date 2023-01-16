import turtle

def draw_pentagon(size, fill_color):
    turtle.begin_fill()
    for i in range(5):
        turtle.forward(size)
        turtle.right(72)
    turtle.end_fill()

def draw_custom_flooring(size, rows, cols, fill_colors):
    for i in range(rows):
        for j in range(cols):
            turtle.color(fill_colors[(i+j) % len(fill_colors)])
            draw_pentagon(size, fill_colors[(i+j) % len(fill_colors)])
            turtle.penup()
            turtle.forward(size)
            turtle.pendown()
        turtle.penup()
        turtle.backward(size * cols)
        turtle.right(72)
        turtle.forward(size)
        turtle.left(72)
        turtle.pendown()

turtle.speed(0)
fill_colors = ['red', 'green', 'blue', 'purple', 'pink']
draw_custom_flooring(50, 5, 5, fill_colors) # size, rows, columns, fill color
turtle.exitonclick()
