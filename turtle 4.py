# import turtle library
import turtle             
my_wn = turtle.Screen()
my_wn.bgcolor("light blue")
my_wn.title("Turtle")
my_pen = turtle.Turtle()
my_pen.color("black")
def my_sqrfunc(size):
   for i in range(4):
      my_pen.fd(size)
      my_pen.left(90)
      size = size - 5
for x in range(0, 400, 20):
  my_sqrfunc(400 - x)
