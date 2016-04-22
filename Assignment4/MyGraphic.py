# Rui Ma V00800795
# Nannan Zhang V00809956
# The reference we used is according to this video: https://www.youtube.com/watch?v=qNdqS9t5fXc
# We changed the image color, size, and added other seven itmes: 
# three flowers, a sun and its lights, a red mouth, and the drawing speed.
# In order to save marker's time, we promote the drawing speed to the max.
# If you want to examine the code,
# you can adjust the drawing speed in the "head" method
# The most difficult thing about this program is calculating points.

# This purpose of this statement is importing the turtle library
from turtle import*

# Main method conclude other class and methods
# Under the main method are other methods called by the main method
# The other methods are the components of the image
def main():
    pu()
    pd()
    head()
    shell()
    feet()
    tail()
    # sun, three flowers, mouth are the extra components we added
    sun()
    flower1()
    flower2()
    flower3()
    mouth()
    done()
    
# It is the first part of the image
# The function of head method is drawing a turtle head
# The comments in this method represent the same meaning in the following method
# So we will not mark every comment
def head():
    # speed means drawing speed, the range of speed is from int 0 to 10
    # 10 indicates max, 0 indicates min
    speed(10)
	# pu means pen up
    pu()
	# set point, then move pen to the point position of (150,50)
    goto(150,50)
    # pd means pen down
    pd()
    # set three atributes of pen, we changed the fill color and pen color
    pen(fillcolor='green yellow', pencolor='greenyellow', pensize=5)
    pd()
    # start to fill in color
    begin_fill()
    # move 90 degree to the right direction
    right(90)
    # draw a circle of 200 degrees clockwise with 100 as a diameter 
    circle(100,-200)
    # move 100 degree to the left direction
    left(100)
    # go forward with distance of 50
    fd(50)
    right(180)
    fd(35)
    right(145)
    fd(110)
    right(30)
    fd(70)
    # set point, then move pen to the point position
    goto(150,50)
    # stop fill in color
    end_fill()
	# start to call eye method as followed
    eye()

# It is the second part of the image, we changed eye color from white into black
def eye():
    pen(fillcolor='black',pencolor='black',pensize=5)
    begin_fill()
    right(165)
    pu()
    fd(150)
    pd()
    # draw a circle with 5 as a radius
    circle(5)
    end_fill()

# It is the third part of the image
def shell():
    pu()
    goto(150,50)
    # we changed shell color
    pen(fillcolor='burlywood', pencolor='saddlebrown', pensize=5)
    pd()
    begin_fill()
    left(95)
    circle(250,170)
    left(86)
    fd(510)
    goto(150,50)
    end_fill()

    shell_arrangement()
    
# This method concluded in the previous method
# In order to eliminate redundancy
# Python often use nest structure
def shell_arrangement():
    pu()
    goto(-300,30)
    pd()
    # The following commands are for loop
    # The output is the figures of the turtle shell
    # The loop will loop for 8 times
    # There are 6 situations
    for i in range(8):
    	# The first situation is that when i less than 3,
    	# there will be two figures
        if i < 3:
        	# Here calls another method
        	# It is still nest loop
        	# First, when calles the nest loop
        	# The python code will jump into the nest loop
            shell_pattern()
            # When the nest loop finished
        	# The python code will come back, 
        	# and continue to compile the following command
            pu()
            right(136)
            fd(110)
            pd()
        # When i = 3, there is another figure
        elif i==3:
            shell_pattern()
            pu()
            right(25)
            fd(90)
            right(90)
            pd()
        # When i = 4, there is another figure
        elif i==4:
            shell_pattern()
            pu()
            right(6)
            fd(120)
            right(120)
            pd()
        # When i = 5, there is another figure
        elif i==5:
            shell_pattern()
            pu()
            left(30)
            fd(60)
            pd()
        # When i = 6, there is another figure
        elif i==6:
            shell_pattern()
            pu()
            fd(40)
            pd()
        # When i is not less than 3, and not equal to 3 or 4 or 5 or 6
        # The python code will come into the else situation
        else:
            shell_pattern() 

# This part represent the shape of the shell
def shell_pattern():
    left(40)
    fd(50)
    right(45)
    fd(40)
    right(70)
    fd(40)
    right(70)
    fd(40)
    right(40)
    fd(30)
    right(38)
    fd(38)

# This part shows the four feet of the turtle
def feet():
    # we changed the feet color
    pen(fillcolor='greenyellow',pencolor='saddlebrown',pensize=5)
    pu()
    goto(-250,-20)
    right(207)
    pd()
    feet2()

    right(90)
    pu()
    fd(380)
    right(90)
    pd()
    feet2()

    pu()
    right(90)
    fd(120)
    right(90)
    fd(18)
    right(360)
    pd()
    feet1()

    pu()
    right(180)
    fd(280)
    right(270)
    pd()
    feet1()

# This method represents the outer feet
# Also, the method here uses nesting structure
def feet1():
    begin_fill()
    for i in range (3):
        fd(50)
        right(90)
    end_fill()

# This method represents the inner feet
def feet2():
    begin_fill()
    fd(80)
    right(90)
    fd(50)
    right(90)
    fd(80)
    end_fill()

# This method represents the tail of the turtle
def tail():
    pu()
    goto(-340,20)
    right(210)
    pd()
    begin_fill()
    fd(40)
    right(150)
    fd(40)
    end_fill()
    ht()

# This method shows the sun and lights in the sky
# This method is the extra component we added
def sun():
	pu()
	goto(400, 200)
	pd()
	pen(fillcolor='yellow', pencolor='red', pensize=5)
	begin_fill()
	circle(70)
	end_fill()
	pu()
	goto(400, 175)
	pd()
	pen(fillcolor='red', pencolor='red', pensize=3)
	begin_fill()
	right(90)
	fd(35)
	end_fill()
	pu()
	goto(320,200)
	pd()
	pen(fillcolor='red', pencolor='red', pensize=3)
	begin_fill()
	right(45)
	fd(35)
	end_fill()
	pu()
	goto(480, 200)
	pd()
	pen(fillcolor='red', pencolor='red', pensize=3)
	begin_fill()
	left(90)
	fd(35)
	end_fill()

# This method represents the first flower on the ground	
# This method is the extra component we added	
def flower1():
	pu()
	goto(-300, -200)
	pd()
	pen(fillcolor='yellow', pencolor='dodgerblue', pensize=5)	
	begin_fill()
	right(30)
	fd(20)
	right(60)
	fd(20)
	right(60)
	fd(20)
	right(60)
	fd(20)
	right(60)
	fd(20)
	right(60)
	fd(20)
	right(60)
	fd(20)
	end_fill()
	pu()
	goto(-311, -235)
	pd()
	pen(fillcolor='greenyellow', pencolor='greenyellow', pensize=5)
	begin_fill()
	right(17)
	fd(30)
	end_fill()
	pu()
	goto(-311, -265)
	pd()
	pen(fillcolor='greenyellow', pencolor='greenyellow', pensize=5)
	begin_fill()
	right(135)
	fd(25)
	end_fill()
	pu()
	goto(-311, -265)
	pd()
	pen(fillcolor='greenyellow', pencolor='greenyellow', pensize=5)
	begin_fill()
	right(90)
	fd(25)
	end_fill()

# This method represents the second flower on the ground	
# This method is the extra component we added
def flower2():
	pu()
	goto(-200, -150)
	pd()
	pen(fillcolor='red', pencolor='yellow', pensize=5)	
	begin_fill()
	right(30)
	fd(30)
	right(60)
	fd(30)
	right(60)
	fd(30)
	right(60)
	fd(30)
	right(60)
	fd(30)
	right(60)
	fd(30)
	right(60)
	fd(30)
	end_fill()
	pu()
	goto(-180, -200)
	pd()
	pen(fillcolor='greenyellow', pencolor='greenyellow', pensize=5)
	begin_fill()
	right(102)
	fd(40)
	end_fill()
	pu()
	goto(-180, -240)
	pd()
	pen(fillcolor='greenyellow', pencolor='greenyellow', pensize=5)
	begin_fill()
	right(135)
	fd(25)
	end_fill()
	pu()
	goto(-180, -240)
	pd()
	pen(fillcolor='greenyellow', pencolor='greenyellow', pensize=5)
	begin_fill()
	right(100)
	fd(25)
	end_fill()

# This method represents the third flower on the ground	
# This method is the extra component we added	
def flower3():
	pu()
	goto(-90, -165)
	pd()
	pen(fillcolor='deeppink', pencolor='deepskyblue', pensize=5)	
	begin_fill()
	right(30)
	fd(30)
	right(60)
	fd(30)
	right(60)
	fd(30)
	right(60)
	fd(30)
	right(60)
	fd(30)
	right(60)
	fd(30)
	right(60)
	fd(30)
	end_fill()
	pu()
	goto(-70, -220)
	pd()
	pen(fillcolor='greenyellow', pencolor='greenyellow', pensize=5)
	begin_fill()
	right(102)
	fd(40)
	end_fill()
	pu()
	goto(-70, -260)
	pd()
	pen(fillcolor='greenyellow', pencolor='greenyellow', pensize=5)
	begin_fill()
	right(135)
	fd(25)
	end_fill()
	pu()
	goto(-70, -260)
	pd()
	pen(fillcolor='greenyellow', pencolor='greenyellow', pensize=5)
	begin_fill()
	right(100)
	fd(25)
	end_fill()

# The output of this part is the red mouth of the turtle
# This method is the extra component we added	
def mouth():
	pu()
	goto(343,15)
	pd()
	pen(fillcolor='red', pencolor='red', pensize=5)
	begin_fill()
	left(135)
	fd(10)
	end_fill()
	
# Recalling main method is to ensure the whole program can be compiled	
main()
