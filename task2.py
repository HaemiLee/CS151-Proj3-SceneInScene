#This code will make a scene within a scene through an art museum 
# CS 151, Fall 2018
# September 25, 2018
# Project 3: Scenes Within Scenes


import better_shapelib as bsl
import sys

def wholeScene(cactusColor="forest green"):
	#Draws an art museum with a Desert Art Exhibit
	#background
	bsl.block(-500, -250, 1000, 500, "burlywood")

	#exhibit1
	bsl.block(-295, -195, 390, 390, "brown")
	bsl.block(-275, -175, 350, 350, "sienna")
	bsl.desert1(-100, 0, .40, cactusColor=cactusColor)

	#exhibit2
	bsl.block(245, -5, 210, 210, "brown")
	bsl.block(255, 5, 190, 190, "sienna")
	bsl.desert2( 350, 100, .20, cactusColor=cactusColor )


	#railing
	bsl.block(-500, -100, 1000, 10, "dark gray")

	bsl.tourist(200, -195, 15)
	bsl.tourist(300, -195, 10)

	#sign
	bsl.block(-280, 205, 355, 30, "antique white")
	bsl.sign(-245, 200, 'Desert Art Exhibit', font = ('Times New Roman', 36, 'bold'))

	#description of painting
	bsl.block(-480, -60, 170, 220, "saddle brown")
	bsl.block(-470, -50, 150, 200, "antique white")
	bsl.descriptionHeader(-460, 125, 'A Lonely Camel', font = ('Times New Roman', 16, 'bold'))
	bsl.description(-460, 110, 'After traveling the desert ', font = ('Times New Roman', 10, 'bold'))
	bsl.description(-460, 95, 'for 37 days, the artist, ', font = ('Times New Roman', 10, 'bold'))
	bsl.description(-460, 80, 'Haemi Lee, painted some  ', font = ('Times New Roman', 10, 'bold'))
	bsl.description(-460, 65, 'of the most beautiful ', font = ('Times New Roman', 10, 'bold'))
	bsl.description(-460, 50, 'creatures she came across. ', font = ('Times New Roman', 10, 'bold'))
	bsl.description(-460, 20, 'She describes it as', font = ('Times New Roman', 10, 'bold'))
	bsl.description(-460, 5, 'a secret empty paradise.', font = ('Times New Roman', 10, 'bold'))
	bsl.description(-400, -20, 'A Oil Painting', font = ('Times New Roman', 10, 'bold'))
	bsl.description(-400, -30, 'by Haemi Lee', font = ('Times New Roman', 10, 'bold'))
	bsl.description(-400, -40, 'Painted 2018', font = ('Times New Roman', 10, 'bold'))



def sceneInsideScene():
	#Draws desert inside a desert inside a desert
	bsl.desert1(-100, 0, 1)
	bsl.desert1(-110, 0, .40)
	bsl.desert1(-120, 0, .10)

# wholeScene()
# sceneInsideScene()
# input( 'Press enter to continue' )

def main(argv):
	# we're assuming the command line parameter for cactus color is one word 
	cactusColor = "forest green"
	if len(argv) > 1:
		cactusColor = argv[1]

	wholeScene(cactusColor=cactusColor)


if __name__ == '__main__':
	main(sys.argv)
	input( 'Press enter to continue' )
