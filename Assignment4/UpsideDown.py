# Rui Ma V00800795
# Nannan Zhang V00809956

# This purpose of this statement is importing the turtle library
import turtle

# The program use "def" to statement a method called "drawTriangle"
# In this method, there are three parameters: points, color, myTurtle 
def drawTriangle(points,color,myTurtle):
    # The function of this statement is filling color
    myTurtle.fillcolor(color)
    # THe function of this statement is let myTurtle go up
    myTurtle.up()
    # The function of this statement is let myTurtle
    # go to the points from [0][0] to [0][1]
    # [0][0] means index of an array, it is not the real points
    # the original real points of [0][0] is (200,100)
    # the original real points of [0][1] is (100,-200)
    # With the change of the triangle's position, the points will always change.
    myTurtle.goto(points[0][0],points[0][1])
    # THe function of this statement is let myTurtle go down
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1][0],points[1][1])
    myTurtle.goto(points[2][0],points[2][1])
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.end_fill()

# The program use "def" to statement a method called "getMid"
# In this method, there are two parameters: p1 and p2
# This method calculates the middle points of each sides of triangle
def getMid(p1,p2):
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)

# The program use "def" to statement a method called "sierpinski"
# In this method, there are three parameters: points, degree, myTurtle 
# The function of this method is that draw sierpinski triangle recursively 
def sierpinski(points,degree,myTurtle):
    # The function of this statement is that 
    # assign the value in the bracket to colormap
    colormap = ['deeppink','lawngreen','yellow','dodgerblue','yellow',
                'violet','orange']
    # The method of "drawTriangle" contains three parameters: points, colormap, myTurtle
    # The function of this method is calliing the previous method of "def drawTriangle(points,color,myTurtle):"
    drawTriangle(points,colormap[degree],myTurtle)
    # The if statement define a situation of when degree large than 0
    # The python code will compile as followed
    if degree > 0:
        # The first sierpinski is the small first triangle of the top right corner
        sierpinski([points[0],
                        getMid(points[0], points[1]),
                        getMid(points[0], points[2])],
                   degree-1, myTurtle)
        # The second sierpinski is the small second triangle on the bottom of the big triangle
        sierpinski([points[1],
                        getMid(points[0], points[1]),
                        getMid(points[1], points[2])],
                   degree-1, myTurtle)
        # The third sierpinski is the small third triangle on the top left corner
        sierpinski([points[2],
                        getMid(points[2], points[1]),
                        getMid(points[0], points[2])],
                   degree-1, myTurtle)

def main():
   myTurtle = turtle.Turtle()
   myWin = turtle.Screen()
   # The function of this statement is that 
   # define the three vertices of three triangle in the big one
   # in the bracket to myPoints in the main method
   myPoints = [[200,100],[0,-200],[-200,100]]
   # The method sierpinski contains three parameters myPoints, 3 and myTurtle
   # They are indicate to the method above (points,degree,myTurtle)
   # The function is calling the previous method of "def sierpinski(points,degree,myTurtle):"
   sierpinski(myPoints,3,myTurtle)
   myWin.exitonclick()

main()
