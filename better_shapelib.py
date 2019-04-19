#This code holds various shape and aggregate shape functions made from loops. 
# Haemi Lee
# CS 151, Fall 2018
# September 25, 2018
# Project 3: Scenes Within Scenes

import turtle 
import sys


turtle.tracer(False)
#Instantly draws the scene


def goto( x,y ):
	#Sends turtle pen to ( x,y )
	print('goto(): going to', x, y)
	turtle.up()
	turtle.goto( x,y )
	turtle.down()
		
	
def block( x, y, width, height, color, fill=True):
	#Draws a block at (x, y) of the given width and height. If fill is True, then the block will be filled in with the given color. If false, then the block will not be filled in.
	goto( x, y )

	if fill == True: 
		turtle.color( color )
		turtle.begin_fill() 
		for i in range(2):
			turtle.forward( width )
			turtle.left( 90 )
			turtle.forward( height )
			turtle.left( 90 )
		turtle.end_fill()
	else:
		for i in range(2):
			turtle.forward( width )
			turtle.left( 90 )
			turtle.forward( height )
			turtle.left( 90 )

def triangle( x, y, length, color, fill=True ):
	#Draws a triangle at (x, y) of the given length. If fill is True, then the triangle will be filled in with the given color. If false, then the triangle will not be filled in.
	goto( x, y )
	if fill == True:
		turtle.color( color )
		turtle.begin_fill() 
		for i in range(3):
			turtle.forward( length )
			turtle.left( 120 )
		turtle.end_fill()
	else:
		for i in range(3):
			turtle.forward( length )
			turtle.left( 120 )


def hexagon( x, y, length, color, fill=True ):
	#Draws a hexagon at (x, y) of the given length
	goto( x, y)

	if fill  == True:
		turtle.color( color )
		turtle.begin_fill() 
		for i in range(6):
			turtle.forward( length )
			turtle.right( 60 )
		turtle.end_fill()
	else:
		turtle.begin_fill() 
		for i in range(6):
			turtle.forward( length )
			turtle.right( 60 )

def diamond( x, y, length, color, fill):
	#Draws a diamond at (x, y) of the given length. If fill is True, then the diamond will be filled in with the given color. If false, then the diamond will not be filled in.
	goto( x, y )

	if fill == True: 
		turtle.color( color )
		turtle.begin_fill() 
		for i in range(2):
			turtle.forward( length )
			turtle.left( 120 )
			turtle.forward( length )
			turtle.left( 60 )
		turtle.end_fill()
	else:
		for i in range(2):
			turtle.forward( length )
			turtle.left( 120 )
			turtle.forward( length )
			turtle.left( 60 )

def star( x, y, length, color= "yellow", fill=True):
	#Draws a star at (x, y) of the given length. If fill is True, then the star will be filled in with the given color. If false, then the star will not be filled in.
	goto( x, y )

	if fill == True: 
		turtle.color( color )
		turtle.begin_fill() 
		for i in range(5):
			turtle.forward( length )
			turtle.left( 144 )
			turtle.forward( length )
			turtle.left( 72 )
		turtle.end_fill()
	else:
		for i in range(5):
			turtle.forward( length )
			turtle.left( 144 )
			turtle.forward( length )
			turtle.left( 72 )

def circle( x, y, radius, color, fill=True):
	#Draws a circle at (x, y) of the given radius.If fill is True, then the circle will be filled in with the given color. If false, then the circle will not be filled in.
	goto( x, y)

	if fill == True:
		turtle.color( color )
		turtle.begin_fill() 
		turtle.circle( radius )
		turtle.end_fill()
	else:
		turtle.circle( radius )



def cactus(x, y, scale, color, fill=True):
	#Draws a cactus at (x, y) of the given scale. If fill is True, then the cactus will be filled in with the given color. If false, then the cactus will not be filled in.
	goto( x, y )

	if fill == True: 
		turtle.color( color )
		turtle.begin_fill()
		block( x, y, 60* scale , 250* scale, color, fill )
		turtle.end_fill()
		turtle.color( color )
		turtle.begin_fill()
		block( x-50*scale, y+170*scale, 30* scale, 50* scale, color, fill )
		turtle.end_fill()
		turtle.color( color )
		turtle.begin_fill()
		block( x-20*scale, y+170*scale, 20* scale, 30* scale, color, fill )
		turtle.end_fill()
		turtle.color( color )
		turtle.begin_fill()
		block( x+60*scale, y+100*scale, 20* scale, 30* scale, color, fill )
		turtle.end_fill()
		turtle.color( color )
		turtle.begin_fill()
		block( x+80*scale, y+100*scale, 30* scale, 50* scale, color, fill )
		turtle.end_fill()
		turtle.color( color )
		turtle.begin_fill()
		circle(x-35*scale, y+205*scale, 15*scale, color, fill)
		turtle.end_fill()
		turtle.color( color )
		turtle.begin_fill()
		circle(x+30*scale, y+220*scale, 30*scale, color, fill)
		turtle.end_fill()
		turtle.color( color )
		turtle.begin_fill()
		circle(x+95*scale, y+135*scale, 15*scale, color, fill)
		turtle.end_fill()
	else:
		block( x, y, 60* scale , 250* scale, color, fill )
		block( x-50*scale, y+170*scale, 30* scale, 50* scale, color, fill )
		block( x-20*scale, y+170*scale, 20* scale, 30* scale, color, fill )
		block( x+60*scale, y+100*scale, 20* scale, 30* scale, color, fill )
		block( x+80*scale, y+100*scale, 30* scale, 50* scale, color, fill )
		circle(x-35*scale, y+205*scale, 15*scale, color, fill)
		circle(x+30*scale, y+220*scale, 30*scale, color, fill)
		circle(x+95*scale, y+135*scale, 15*scale, color, fill)

def cloud( x, y, scale, color="white", fill=True):
	#Draws a cloud at (x, y) of the given scale. If fill is True, then the cloud will be filled in with the given color. If false, then the cloud will not be filled in.
	if fill == True:
		turtle.color( color )
		turtle.begin_fill()
		circle( x, y, 10*scale, color, fill )
		turtle.end_fill()
		turtle.color( color )
		turtle.begin_fill()
		circle( x+10*scale, y+10*scale, 10*scale, color, fill )
		turtle.end_fill()
		turtle.color( color )
		turtle.begin_fill()
		circle( x+30*scale, y+10*scale, 10*scale, color, fill )
		turtle.end_fill()
		turtle.color( color )
		turtle.begin_fill()
		circle( x+50*scale, y+10*scale, 10*scale, color, fill )
		turtle.end_fill()
		turtle.color( color )
		turtle.begin_fill()
		circle( x+60*scale, y, 10*scale, color, fill )
		turtle.end_fill()
		turtle.color( color )
		turtle.begin_fill()
		circle( x+50*scale, y-10*scale, 10*scale, color, fill )
		turtle.end_fill()
		turtle.color( color )
		turtle.begin_fill()
		circle( x+30*scale, y-10*scale, 10*scale, color, fill )
		turtle.end_fill()
		turtle.color( color )
		turtle.begin_fill()
		circle( x+10*scale, y-10*scale, 10*scale, color, fill )
		turtle.end_fill()
		turtle.color( color )
		turtle.begin_fill()
		block( x+10*scale, y, 40* scale, 20* scale, color, fill )
		turtle.end_fill()
	else:
		circle( x, y, 10*scale, color, fill )
		circle( x+10*scale, y+10*scale, 10*scale, color, fill )
		circle( x+30*scale, y+10*scale, 10*scale, color, fill )
		circle( x+50*scale, y+10*scale, 10*scale, color, fill )
		circle( x+60*scale, y, 10*scale, color, fill )
		circle( x+50*scale, y-10*scale, 10*scale, color, fill )
		circle( x+30*scale, y-10*scale, 10*scale, color, fill )
		circle( x+10*scale, y-10*scale, 10*scale, color, fill )
		block( x+10*scale, y, 40* scale, 20* scale, color, fill )

def rocks( x, y, scale, color, fill=True):
	#Draws a pair of rocks at (x, y) at given scale. If fill is True, then the cloud will be filled in with the given color. If false, then the cloud will not be filled in.
	if fill == True:
		turtle.color( color )
		turtle.begin_fill()
		hexagon( x, y, 20*scale, color, fill )
		turtle.end_fill()
		turtle.color( color )
		turtle.begin_fill()
		hexagon( x+50*scale, y-20*scale, 10*scale , color, fill)
		turtle.end_fill()
	else:
		hexagon( x, y, 20*scale, color, fill )
		hexagon( x+50*scale, y-20*scale, 10*scale , color, fill)

def pyramids( x, y, scale, color, fill=True ):
	#Draws 3 pyramids at (x, y) at a given scale. The left and right pyramids are the same size. The middle pyramid is bigger. 
	#If fill is True, then the pyramids will be filled in with the given color. If false, then the pyramids will not be filled in.
	if fill == True:
		turtle.color( color )
		turtle.begin_fill()
		triangle( x, y, 100*scale, color, fill )
		turtle.end_fill()
		turtle.color( color)
		turtle.begin_fill()
		triangle( x+100*scale, y, 150*scale, color, fill )
		turtle.end_fill()
		turtle.color( color )
		turtle.begin_fill()
		triangle( x+250*scale, y, 100*scale, color, fill )
		turtle.end_fill()
	else:
		triangle( x, y, 100*scale, color, fill )
		triangle( x+100*scale, y, 150*scale, color, fill )
		triangle( x+250*scale, y, 100*scale, color, fill )

def camel( x, y, scale, color, fill=True ):
	#Draws a camel at (x, y) at given scale
	#If fill is True, then the camel will be filled in with the given color. If false, then the camel will not be filled in.
	if fill == True:
		
		#camelHead
		turtle.color( color )
		turtle.begin_fill()
		circle( x-60*scale, y+250*scale, 15*scale, color, fill )
		turtle.end_fill()
		turtle.color( color )
		turtle.begin_fill()
		triangle( x-10*scale, y+300*scale, 20*scale, color, fill )
		turtle.end_fill()
		turtle.color( color )
		turtle.begin_fill()
		block( x-60*scale, y+250*scale, 20* scale, 30* scale, color, fill )
		turtle.end_fill()
		turtle.color( color )
		turtle.begin_fill()
		block( x-40*scale, y+240*scale, 60* scale, 50* scale, color, fill )
		turtle.end_fill()
		turtle.color( color )
		turtle.begin_fill()
		block( x-50*scale, y+240*scale, 10* scale, 10* scale, color, fill )
		turtle.end_fill()
		turtle.color( color )
		turtle.begin_fill()
		block( x-20*scale, y+290*scale, 40* scale, 10* scale, color, fill )
		turtle.end_fill()
		turtle.color( color )
		turtle.begin_fill()
		block( x+20*scale, y+240*scale, 20* scale, 20* scale, color, fill )
		turtle.end_fill()
		
		#camelBody
		turtle.color( color )
		turtle.begin_fill()
		block( x-30*scale, y+170*scale, 70* scale, 70* scale, color, fill )
		turtle.end_fill()
		turtle.color( color )
		turtle.begin_fill()
		block( x+40*scale, y+170*scale, 20* scale, 60* scale, color, fill )
		turtle.end_fill()
		turtle.color( color )
		turtle.begin_fill()
		block( x+60*scale, y+170*scale, 20* scale, 40* scale, color, fill )
		turtle.end_fill()
		turtle.color( color )
		turtle.begin_fill()
		block( x+80*scale, y+170*scale, 20* scale, 50* scale, color, fill )
		turtle.end_fill()
		turtle.color( color )
		turtle.begin_fill()
		block( x+100*scale, y+170*scale, 40* scale, 80* scale, color, fill )
		turtle.end_fill()
		turtle.color( color )
		turtle.begin_fill()
		block( x+140*scale, y+170*scale, 20* scale, 90* scale, color, fill )
		turtle.end_fill()
		turtle.color( color )
		turtle.begin_fill()
		block( x+160*scale, y+170*scale, 80* scale, 100* scale, color, fill )
		turtle.end_fill()
		turtle.color( color )
		turtle.begin_fill()
		block( x+240*scale, y+170*scale, 10* scale, 100* scale, color, fill )
		turtle.end_fill()
		turtle.color( color )
		turtle.begin_fill()
		block( x+250*scale, y+170*scale, 30* scale, 70* scale, color, fill )
		turtle.end_fill()
		turtle.color( color )
		turtle.begin_fill()
		block( x+280*scale, y+170*scale, 10* scale, 40* scale, color, fill )
		turtle.end_fill()
		turtle.color( color )
		turtle.begin_fill()
		block( x-10*scale, y+140*scale, 300* scale, 30* scale, color, fill )
		turtle.end_fill()
		turtle.color( color )
		turtle.begin_fill()
		block( x+50*scale, y+110*scale, 180* scale, 30* scale, color, fill )
		turtle.end_fill()
		turtle.color( color )
		turtle.begin_fill()
		circle( x+200*scale, y+230*scale, 40*scale, color, fill )
		turtle.end_fill()
		
		#camelLegs
		turtle.color( color )
		turtle.begin_fill()
		block( x, y+10, 10* scale, 140* scale, color, fill )
		turtle.end_fill()
		turtle.color( color )
		turtle.begin_fill()
		block( x+30*scale, y+10*scale, 10* scale, 140* scale, color, fill )
		turtle.end_fill()
		turtle.color( color )
		turtle.begin_fill()
		block( x+240*scale, y+10*scale, 10* scale, 140* scale, color, fill )
		turtle.end_fill()
		turtle.color( color )
		turtle.begin_fill()
		block( x+270*scale, y+10*scale, 10* scale, 140* scale, color, fill )
		turtle.end_fill()
		
		#camelTail
		turtle.color( color )
		turtle.begin_fill()
		block( x+290*scale, y+190*scale, 20* scale, 10* scale, color, fill )
		turtle.end_fill()
		turtle.color( color )
		turtle.begin_fill()
		block( x+310*scale, y+130*scale, 10* scale, 70* scale, color, fill )
		turtle.end_fill()
		turtle.color( color )
		turtle.begin_fill()
		block( x+310*scale, y+110*scale, 10* scale, 20* scale, "dark goldenrod", fill )
		turtle.end_fill()
		
		#camelInnerEar
		turtle.color( color )
		turtle.begin_fill()
		triangle( x-5*scale, y+300*scale, 10*scale, "hot pink", fill )
		turtle.end_fill()
		
		#cameleyes
		turtle.color( color )
		turtle.begin_fill()
		circle( x-30*scale, y+270*scale, 5*scale, "black", fill )
		turtle.end_fill()
		
		#camelHooves
		turtle.color( color )
		turtle.begin_fill()
		block( x, y+10, 10* scale, 20* scale, "saddle brown", fill )
		turtle.end_fill()
		turtle.color( color )
		turtle.begin_fill()
		block( x+30*scale, y+10*scale, 10* scale, 20* scale, "saddle brown", fill )
		turtle.end_fill()
		turtle.color( color )
		turtle.begin_fill()
		block( x+240*scale, y+10*scale, 10* scale, 20* scale, "saddle brown", fill )
		turtle.end_fill()
		turtle.color( color )
		turtle.begin_fill()
		block( x+270*scale, y+10*scale, 10* scale, 20* scale, "saddle brown", fill )
		turtle.end_fill()
	else:
		#camelHead
		circle( x-60*scale, y+250*scale, 15*scale, color, fill )
		triangle( x-10*scale, y+300*scale, 20*scale, color, fill )
		block( x-60*scale, y+250*scale, 20* scale, 30* scale, color, fill )
		block( x-40*scale, y+240*scale, 60* scale, 50* scale, color, fill )
		block( x-50*scale, y+240*scale, 10* scale, 10* scale, color, fill )
		block( x-20*scale, y+290*scale, 40* scale, 10* scale, color, fill )
		block( x+20*scale, y+240*scale, 20* scale, 20* scale, color, fill )

		#camelBody
		block( x-30*scale, y+170*scale, 70* scale, 70* scale, color, fill )
		block( x+40*scale, y+170*scale, 20* scale, 60* scale, color, fill )
		block( x+60*scale, y+170*scale, 20* scale, 40* scale, color, fill )
		block( x+80*scale, y+170*scale, 20* scale, 50* scale, color, fill )
		block( x+100*scale, y+170*scale, 40* scale, 80* scale, color, fill )
		block( x+140*scale, y+170*scale, 20* scale, 90* scale, color, fill )
		block( x+160*scale, y+170*scale, 80* scale, 100* scale, color, fill )
		block( x+240*scale, y+170*scale, 10* scale, 100* scale, color, fill )
		block( x+250*scale, y+170*scale, 30* scale, 70* scale, color, fill )
		block( x+280*scale, y+170*scale, 10* scale, 40* scale, color, fill )
		block( x-10*scale, y+140*scale, 300* scale, 30* scale, color, fill )
		block( x+50*scale, y+110*scale, 180* scale, 30* scale, color, fill )
		circle( x+200*scale, y+230*scale, 40*scale, color, fill )
		
		#camelLegs
		block( x, y+10, 10* scale, 140* scale, color, fill )
		block( x+30*scale, y+10*scale, 10* scale, 140* scale, color, fill )
		block( x+240*scale, y+10*scale, 10* scale, 140* scale, color, fill )
		block( x+270*scale, y+10*scale, 10* scale, 140* scale, color, fill )
		
		#camelTail
		block( x+290*scale, y+190*scale, 20* scale, 10* scale, color, fill )
		block( x+310*scale, y+130*scale, 10* scale, 70* scale, color, fill )
		block( x+310*scale, y+110*scale, 10* scale, 20* scale, color, fill )
		
		#camelInnerEar
		triangle( x-5*scale, y+300*scale, 10*scale, color, fill )
		
		#cameleyes
		circle( x-30*scale, y+270*scale, 5*scale, color, fill )
		
		#camelHooves
		block( x, y+10, 10* scale, 20* scale, color, fill )
		block( x+30*scale, y+10*scale, 10* scale, 20* scale, color, fill )
		block( x+240*scale, y+10*scale, 10* scale, 20* scale, color, fill )
		block( x+270*scale, y+10*scale, 10* scale, 20* scale, color, fill )

def tourist(x, y, scale):
	#Draws tourguide at given location and scale. 
	circle(x, y, .5*scale, "black")
	circle(x+ 4*scale, y, .5*scale, "black")
	block( x, y, 1*scale, 9*scale, "dark slate blue")
	block( x+ 3*scale, y, 1*scale, 9*scale, "dark slate blue")
	block( x, y, 1*scale, 1*scale, "black")
	block( x+ 3*scale, y, 1*scale, 1*scale, "black")
	block( x, y+ 9*scale, 4*scale, 7*scale, "dark blue")
	block( x+ -3*scale, y+ 15*scale, 3*scale, 1*scale, "royal blue")
	circle(x+ -3*scale, y+ 15*scale, .5*scale, "blanched almond")
	block( x+ 4*scale, y+ 12*scale, 1*scale, 4*scale, "royal blue")
	circle(x+ 4.5*scale, y+ 11*scale, .5*scale, "blanched almond")
	circle(x+ 2*scale, y+ 16*scale, 2*scale, "blanched almond")

	#face
	circle(x+ 1*scale, y+ 18*scale, .10*scale, "black")
	circle(x+ 2*scale, y+ 18*scale, .10*scale, "black")
	block( x+ 1.25*scale, y+ 17*scale, 1*scale, .20*scale, "hot pink")

def sign(x, y, text, font = ('Times New Roman', 36, 'bold')):
	#Draws any text at a given location with the given message. 
	turtle.penup()
	turtle.goto (x, y)
	turtle.color( "black" )
	turtle.write (text, font = ('Times New Roman', 36, 'bold'))

def descriptionHeader(x, y, text, font = ('Times New Roman', 16, 'bold')):
	#Draws any text at a given location with the given message. 
	turtle.penup()
	turtle.goto (x, y)
	turtle.color( "black" )
	turtle.write (text, font = ('Times New Roman', 16, 'bold'))

def description(x, y, text, font = ('Times New Roman', 10, 'bold')):
	#Draws any text at a given location with the given message. 
	turtle.penup()
	turtle.goto (x, y)
	turtle.color( "black" )
	turtle.write (text, font = ('Times New Roman', 10, 'bold'))




def desert1( x, y, scale, cactusColor="forest green"):
	#Draws desert scene in the daytime at given location and scale. 
	block( x+ -400*scale, y, 800*scale, 400*scale, "light blue")
	block(x+ -400*scale, y+ -400*scale, 800*scale, 400*scale, "burlywood")
	cloud(x+ scale, y+ 330*scale, scale )
	cloud(x+ -200*scale, y+ 250*scale, scale)
	cloud(x+ -150*scale, y+ 100*scale, scale )
	cloud(x+ -380*scale, y+ 200*scale, scale )
	cloud(x+ -350*scale, y+ 350*scale, scale )
	cloud(x+ 100*scale, y+ 150*scale, scale )
	cloud(x+ 180*scale, y+ 280*scale, scale )
	cloud(x+ 300*scale, y+ 50*scale, scale )
	cactus(x+ -325*scale, y+ -300*scale, scale, cactusColor)
	cactus(x+ 225*scale, y+ -150*scale, 1.5*scale, cactusColor)
	cactus(x+ 150*scale, y*scale, .25*scale, cactusColor)
	cactus(x+ -325*scale, y*scale, .50*scale, cactusColor)
	camel(x+ -150*scale, y+ -200*scale, .95*scale, "goldenrod")
	rocks(x+ 200*scale, y+ -170*scale, 2*scale, "medium purple")
	rocks(x+ -100*scale, y+ -260*scale, 2.5*scale, "firebrick")

def desert2(x, y, scale, cactusColor="forest green"):
	#Draws desert scene in the night time at given location and scale. 
	block( x+ -400*scale, y, 800*scale, 400*scale, "midnight blue")
	block(x+ -400*scale, y+ -400*scale, 800*scale, 400*scale, "navajo white")
	star(x+ -200*scale, y+ 250*scale, 3*scale)
	star(x+ -150*scale, y+ 100*scale, 3*scale)
	star(x+ -380*scale, y+ 200*scale, 3*scale)
	star(x+ -350*scale, y+ 350*scale, 3*scale)
	star(x+ 100*scale, y+ 150*scale, 3*scale)
	star(x+ 180*scale, y+ 280*scale, 3*scale)
	star(x+ 300*scale, y+ 50*scale, 3*scale)
	pyramids(x, y, scale, "burlywood")
	cactus(x+ -325*scale, y+ -300*scale, scale, cactusColor)
	cactus(x+ 225*scale, y+ -180*scale, 1*scale, cactusColor)
	camel(x+ -150*scale, y+ -210*scale, .75*scale, "goldenrod")

# def colorfulDesert( x, y, scale, )

# if __name__=="__main__":

	# block( -300, -100, 20, 100, "green", False)
	# hexagon( -100, 100, 20, "yellow", True)
	# diamond( 0, 0, 50, "red", True)
	# star( 100, 100, 30, "blue", True)
	# circle( 200, -200, 20, "purple", False)
	# cactus(0, 0, 1, "forest green", False)
	# cloud(0, 0, 1, "steel blue", False)
	# rocks(0,0,1,"gray", True)
	# pyramids(0, 0, 1, "burlywood", True)
	# desert1(0, 0, .50)
