from turtle import  *
sides=4
colors=['red','yellow']
speed(0)
delay(0)
hideturtle()
bgcolor('black')
for i in range(500):
    color(colors[i%2])
    fd(i*3//sides+i)
    lt(360/sides+1)
    width(i * sides )
done()