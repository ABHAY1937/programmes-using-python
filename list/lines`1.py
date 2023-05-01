import turtle
import colorsys

#create window to display pattern
t=turtle.Turtle()
s=turtle.Turtle()

#setting backgroud colour
s.color('black')

#speed of turtle to draw pattern
t.speed(0)

n=36
h=0

#loop for drawing pattern
for i in range(460):
    c=colorsys.hsv_to_rgb(h,1,0.9)
    h+=1/n
    t.color(c)
    t.left(145)
    for j in range(5):
        t.forward(300)
        t.left(150)

# keep the window open until the user closes it
turtle.done()
