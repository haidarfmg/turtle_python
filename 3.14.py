#Draw an Olympic Symbol in Python
import turtle

# object tr for turtle
tr = turtle.Turtle()
r = int(input("enter the radius of circules: "))
# set thickness for each ring
tr.pensize(5)

tr.color("blue")
tr.penup()
tr.goto(-2*r-20, 0)
tr.pendown()
tr.circle(r)

tr.color("black")
tr.penup()
tr.goto(0, 0)
tr.pendown()
tr.circle(r)

tr.color("red")
tr.penup()
tr.goto(2*r+20, 0)
tr.pendown()
tr.circle(r)

tr.color("yellow")
tr.penup()
tr.goto(-r-10, -r-5)
tr.pendown()
tr.circle(r)

tr.color("green")
tr.penup()
tr.goto(r+10, -r-5)
tr.pendown()
tr.circle(r)
