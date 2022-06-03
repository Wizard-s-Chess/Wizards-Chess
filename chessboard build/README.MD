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

##Building the case

The case is composed of the following material :
 - 1 wooden base plate of 59cm x 59,7cm the 59,7 cm are following the rodes  
 - 1 plate of plexiglas of 60cm x 60cm with holes for LCD screen and cabling
 - 10 3d printed T shaped piece to lay the plexiglas on it
 - 4 wooden wall of dimensions 62 x cm x 12 cm x 1,5cm
 - 4 3d printed corner inside pieces to lay the plexiglas on it
 - 8 3d printed corners outside pieces to maintain the wooden walls 
 - middle size screws
 - small sized crews
 
First print the 10 T shaped, the 4 inside corners and the 8 outside corners. Then, the wooden and plexiglas pieces 
should be cut at the right size.

1. To fix the walls here is the following steps:
2. Glue the sides of the bottom plate
3. Stick the wall on the bottom plate
4. Screw (using the small screws) the inside corners
5. Screw (using the medium screws) the outsides corners
6. Screw on the bottom plate the T shaped pieces.
7. Here is the schema the shows the layout of all those pieces :


![building the case image 1 &](/chessboard%20build/pictures/build_case1.PNG)
*The top (left) and side (right) view*

##Inserting the linear bearings, threaded shafts and stepper motor
*Note : This part can be done before to put the plate inside the box.*

This part needs the following material :
 - 4 metal rodes
 - 2 threaded shafts
 - 4 linear bearings
 - 2 stepper motors
 - 2 nuts for the threaded shafts
 - 2 wooden parts of x mm x x mm
 - 4 stands for the rodes
 - 2 stands for the nuts 
 - 3D printed parts : 
    - Fixation for inferior motor
    - Fixation for superior motor
    - Support for the inferior nut
    - Support for the superior nut
    - Support the the electromagnet
    - Support facing the superior stepper motor (laying on the opposite rode)
 - Screws

For this one the only to do is to print the pieces and then to screw on the plate the 6 stands 
On the following scheme here are the different distances to respect for screwing.

|   | Measures |
|---|----------|
| A | 35mm     |
| B | 95mm     |
| C | 93mm     |
| D | 197mm    |
| E | 203mm    |
| F | 95mm     |

###Wedges

In order to have everything at the right height, it is important to put some wedge between the bottom plate of the
 board and the rods and shafts holders. This is how it looks like :

![building the case image 2 &](/chessboard%20build/pictures/build_case2.PNG)
![building the case image 3 &](/chessboard%20build/pictures/build_case3.PNG)

