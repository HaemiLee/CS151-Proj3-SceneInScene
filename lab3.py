#Haemi Lee
#9/19/18
#lab3.py

import turtle
import random
import sys

# print(sys.argv)
# 
# print(sys.argv[0])
# print(sys.argv[3] * 3)
# print(int( sys.argv[3] ) * 3)

def star(x, y, size):
	turtle.up()
	turtle.goto(x, y)
	turtle.down()

	for i in range(5):
		turtle.forward(size)
		turtle.left(144)
		
def star2( rays, size ):
	# loop over the list returned by the range function
	for i in range(rays):
		turtle.setheading( i * 360 / rays )
		turtle.forward( size )
		turtle.backward( size )
		
if __name__=="__main__":
	turtle.tracer(False)
	turtle.color( 0.7, 0.7, 0.2 )
	print ("sys.argv is", sys.argv)
	if len( sys.argv ) > 1:
		N = int( sys.argv[1] )
	else:
		N=50
	# for i in range( N ):
#		star( random.randint(-300, 200), random.randint(0, 200), random.randint(5, 15) )



	
			
	star2(N, 50)

	turtle.update()
	input('Enter')	
	
	
				