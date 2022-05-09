#stop sign
import turtle
tr = turtle.Turtle()
tr.fillcolor('Red')
tr.begin_fill()
for i in range(6):
   tr.forward(70)           
   tr.right(60) 
tr.end_fill()
tr.penup()
tr.goto(35,-70)
tr.pendown()
tr.color('white')
tr.write("STOP", move=True,align='center',font=('Times New Roman',18,'bold'))
turtle.done()


