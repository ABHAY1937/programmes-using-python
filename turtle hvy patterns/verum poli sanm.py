import turtle
import colorsys

#create window to display pattern
t=turtle.Turtle()

#setting backgroud colour
t.color("black")

#speed of turtle to draw pattern
t.speed(0)

c = 0.0

#loop for drawing pattern
for i in range(100):
    p = pow(0.92, i)
    r = 3 * noise((i+c)*0.03) * 6.283185  # approximate TAU
    x += cos(r) * 8
    y += sin(r) * 8
    t.color((b+i*2)%255, y, x)
    t.pensize(10*p)
    t.begin_fill()
    t.rect(x-p*1168/2, y-p*834/2, x+p*1168/2, y+p*834/2)  # use left, top, right, bottom arguments
    t.end_fill()

# keep the window open until the user closes it
turtle.done()
