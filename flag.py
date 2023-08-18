import turtle

def draw_rectangle(color, width, height):
    turtle.begin_fill()
    turtle.fillcolor(color)
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()

def afghan_flag():
    turtle.speed(1)
    turtle.penup()

    # Drawing the black stripe
    turtle.goto(-150, 100)
    draw_rectangle("black", 300, 40)

    # Drawing the red stripe
    turtle.goto(-150, 60)
    draw_rectangle("red", 300, 40)

    # Drawing the green stripe
    turtle.goto(-150, 20)
    draw_rectangle("green", 300, 40)

    # Writing "Happy Independence Day"
    turtle.goto(0, -50)
    turtle.color("black")
    turtle.write(" Happy Independence Day 104", align="center", font=("Arial",13, "bold"))
    '''turtle.goto(0, -70)
    turtle.color("black")
    turtle.write("an illiterate nation can never be independent", align="center", font=("Arial", 13, "bold"))
    turtle.goto(0, -90)
    turtle.color("black")
    turtle.write("Happy independence Day", align="center", font=("Arial", 16, "bold"))
    turtle.goto(0, -110)
    turtle.color("black")
    turtle.write("AbdulHai Qinaat", align="Center",font=("Arial", 13, "bold"))'''



    # Hide the turtle
    turtle.hideturtle()

    # Keep the window open until it's closed by the user
    turtle.done()

# Call the function to draw the flag
afghan_flag()

