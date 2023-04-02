# Import turtle package
import turtle
t = turtle.Turtle()
t.screen.bgcolor('black')


# Defining a method to draw curve
def curve():
	for i in range(200):

		# Defining step by step curve motion
		turtle.right(1)
		turtle.forward(1)

# Defining method to draw a full heart
def heart():

	# Set the fill color to red
	turtle.fillcolor("red")

	# Start filling the color
	turtle.begin_fill()

	# Draw the left line
	turtle.left(140)
	turtle.forward(113)

	# Draw the left curve
	curve()
	turtle.left(120)

	# Draw the right curve
	curve()

	# Draw the right line
	turtle.forward(112)

	# Ending the filling of the color
	turtle.end_fill()





# Draw a heart
heart()


# To hide turtle
turtle.ht()


import turtle
t = turtle.Turtle()
t.screen.bgcolor("black")
t.pensize(2)
t.color("green")
t.left(90)
t.backward(100)
t.speed(90000)
t.shape('turtle')

def tree(i):
    if i<10:
        return
    else:
        t.forward(i)
        t.color('orange')
        t.circle(2)
        t.color("brown")
        t.left(30)
        tree(3*i/4)
        t.right(60)
        tree(3*i/4)
        t.left(30)
        t.backward(i)
tree(100)


def text():

    t.up()
    t.setpos(-58 , -145 )
    t.down()
    t.color("white")
    t.write("I LOVE YOU ❤️ " , font = ("Verdana" , 12 , "normal"))

text()
t.ht()

turtle.done()