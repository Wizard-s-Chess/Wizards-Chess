#Automated Chess Board Report

##Introduction

###Description
Our idea is to allow chess players to play against a computer
 on a physical board. The pieces 
 are moved from underneath the board 
 using a magnet. The goal of the robot is to recognize the player moves 
 through computer vision. This will be explained deeper in the next 
 sections. The motivation behind the idea is to surpass ourselves and 
 face a robot implemented using Artificial intelligence that can be more 
 competitive than face a real human. We will implement three different 
 levels: Beginner, Intermediate, Expert.
 
###Components and supplies 

 - Arduino UNO
 - Rasberry pi 3 
 - Esp 32 cam
 - Motor driver
 - Stepper motor 2x
 - Stepper driver 
 - electromagnet
 - 12V power supply
 - Wooden board 59cm x 59,7cm
 - Wooden board 62xm x12 cm 4x
-  Plexiglas board 59cm x 59,7cm
 - Linear Bearing Block 4x 
 - Wires (male-male, male-female, female-female)
 - Screen LCD
 - Screws
 - Wooden support esp32
 - 3d print of some pieces (see .stl files) 
 
##General working

As said in the introduction the chessboard is designed to move the 
adversary pieces on the chessboard by themself.
To do so, the chess pieces will be moved by an electro 
magnet which is placed below the play board.
To move the electromagnet, linear bearings and the stepper motors 
are placed under the chess board as shown on this schema :

![general working image 1](/chessboard%20build/pictures/gen_work1.PNG)

*Board and from side and top view closed*

![general working image 2](/chessboard%20build/pictures/gen_work2.PNG)

*First movement axis of the electromagnet*

![general working image 3](/chessboard%20build/pictures/gen_work2.PNG)

*Second movement axis of the electromagnet (laying on top of the first)*