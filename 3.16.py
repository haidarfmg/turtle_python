# import turtle library
import turtle             
tr = turtle.Turtle()
l = int(input("Enter the length of the shapes: "))
d=l+l/2
for i in range(3,8): 
    for j in range(i):
       tr.pendown()
       tr.forward(l)           
       tr.right(360 / i)
       tr.penup()
    tr.goto(d,0)
    d=d*2
turtle.done()
