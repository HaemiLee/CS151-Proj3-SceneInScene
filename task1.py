#This code will make a three scenes in three different sizes in three different locations.
# CS 151, Fall 2018
# September 25, 2018
# Project 3: Scenes Within Scenes


import better_shapelib as bsl
import sys

def threeScenes( ):
	#Draws a big version of desert, medium version of desert, and small version of a desert.
	bsl.desert1(-300, 0, .50)
	bsl.desert1(100, 0, .25)
	bsl.desert1(300, 0, .10)

threeScenes()

input( 'Press enter to continue' )