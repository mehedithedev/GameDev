from turtle import *

# Page setup
setup(800, 500)
speed(0)

# Function to draw a rectangle with a specific color
def draw_rectangle(color):
    begin_fill()
    fillcolor(color)
    for _ in range(2):
        forward(800)
        right(90)
        forward(100)
        right(90)
    end_fill()

# Draw the flag
penup()
goto(-400, 250)  # Start at the top left
pendown()

# Draw the black stripe
draw_rectangle("black")
right(90)
forward(100)
left(90)

# Draw the white stripe
draw_rectangle("white")
right(90)
forward(100)
left(90)

# Draw the green stripe
draw_rectangle("green")
right(90)
forward(100)
left(90)

# Draw the red stripe
draw_rectangle("red")

# Draw the red triangle
penup()
goto(-400, 250)
pendown()
color("red")
begin_fill()
forward(200)
right(120)
forward(400)
right(120)
forward(200)
end_fill()

# Draw the star
penup()
goto(-300, 200)
pendown()
color("white")
begin_fill()
for _ in range(7):
    forward(30)
    right(150)
end_fill()

hideturtle()
done()
