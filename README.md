# Wizard's Chess ♟️⚡

# Automated Chess Board Report
![board showcase](pictures/wizards-chess.gif)
## Introduction

### Description
Our idea is to allow chess players to play against a computer
 while keeping the charm of playing on a physical board.
 The player makes his move on the board and then confirms it.The computer then recognizes the movement and plays its turn,
 There's also a mode where you can watch two AIs play against each other.
 ![building the case image 1](/pictures/main.jpg)

### Components and supplies

 - Arduino UNO
 - Rasberry pi 3
 - Esp 32 cam
 - A usb to serial adapter
 - Motor driver
 - Stepper motor 2x
 - Stepper driver
 - electromagnet
 - 12V power supply
 - Wooden board 59cm x 59,7cm
 - Wooden board 62xm x12 cm 4x
 - Plexiglas board 59cm x 59,7cm
 - Linear Bearing Block 4x
 - Screen LCD
 - Screws
 - Wooden support esp32
 - 3d print of some pieces (see .stl files)

## General working

As said in the introduction the chessboard is designed to move the
adversary pieces on the chessboard by themself.
To do so, the chess pieces will be moved by an electro
magnet which is placed below the play board.
To move the electromagnet, linear bearings and the stepper motors
are placed under the chess board as shown on this schema :

![general working image 1](/pictures/gen_work1.PNG)

*Board and from side and top view closed*

![general working image 2](/pictures/gen_work2.PNG)

*First movement axis of the electromagnet*

![general working image 3](/pictures/gen_work2.PNG)

*Second movement axis of the electromagnet (laying on top of the first)*

## Building the case

The case is composed of the following material :
 - 1 wooden base plate of 59cm x 59,7cm the 59,7 cm are following the rodes  
 - 1 plate of plexiglas of 60cm x 60cm with holes for LCD screen and cabling
 - 10 3d printed T shaped piece to lay the plexiglas on it
 - 4 wooden wall of dimensions 62 x cm x 12 cm x 1,5cm
 - 4 3d printed corner inside pieces to lay the plexiglas on it
 - 8 3d printed corners outside pieces to maintain the wooden walls
 - middle size screws (30 mm M3 screws)
 - small sized crews (12 mm M3 screw)

First print the 10 T shaped, the 4 inside corners and the 8 outside corners. Then, the wooden and plexiglas pieces
should be cut at the right size.

1. To fix the walls here is the following steps:
2. Glue the sides of the bottom plate
3. Stick the wall on the bottom plate
4. Screw (using the small screws) the inside corners
5. Screw (using the medium screws) the outsides corners
6. Screw on the bottom plate the T shaped pieces.
7. Here is the schema the shows the layout of all those pieces :


![building the case image 1](/pictures/build_case1.PNG)

*The top (left) and side (right) view*

## Inserting the linear bearings, threaded shafts and stepper motor
![building the case image 1](/pictures/3d_design.PNG)
*Note : This part can be done before to put the plate inside the box.*

This part needs the following material :
 - 4 metal rodes
 - 2 threaded shafts
 - 4 linear bearings
 - 2 stepper motors
 - 2 nuts for the threaded shafts
 - 1 wooden parts of 21,6 cm x 2,5 cm x 3 mm
 - 1 wooden parts of 22,4 cm x 2,5 cm x 3 mm
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

### Wedges

In order to have everything at the right height, it is important to put some wedge between the bottom plate of the board and the rods and shafts holders. This is how it looks like :

 ![building the case image 2](/pictures/insert_bearing2.PNG)

 ![building the case image 3](/pictures/insert_bearing3.PNG)

## Camera box and support

This part is quite easy and needs very few material :
 - 1 ESP32 cam
 - 1 3D printed case for ESP32 cam
 - 2 3D angles for wooden stick
 - 3 wooden sticks of size 65 cm x 1 cm x 1 cm
 - 2 3D printed support
 - small screws

As this part is very easy, only a scheme will be provided.
Please, do not forget to glue the stick inside the angles.

![camera box image 1](/pictures/cam_box1.PNG)

*The 2 side views*

In green : the angles

In blue : the case

In black : the support

## Chess pieces
In order to be attracted by the electromagnet, we will put screws inside the chess pieces.
 - 3D printed chess pieces
 - 16 medium screws

Once everything is printed, it is just needed to screw on the bottom of each adversary’s piece.

*Note : If, due to the structure made by the 3D printer it is impossible to put in the screws, it also possible to gently redrill the pieces beforehand.*

## Electronic

For this part we will the following material:
 - 1 arduino
 - 1 raspberry pi 3B
 - 1 VNH2SP30 Motor Driver
 - 1 LCD screen
 - 2 button switches
 - 2 switches
 - 1 lm2596 regulator
 - 2 a4988 stepper motor driver
 - 3 resistances of 220 Ω
 - 1 alimentation 12v
 - different pieces of wiring


### Part 1 : fix the switches
To determine  and calibrate the position of the linear bearings on the axises 2 switches must be placed.
For the first switch (on the superior axis) it is placed directly on the 3D printed part that hold the superior stepper motor.

![electronic image 1](/pictures/electronic1.PNG)

For the second switch it is placed on the wooden board, next to the inferior stepper motor.
It is placed 102mm away from the wall of the chess board :

![electronic image 2](/pictures/electronic2.PNG)

### Part 2 : Wiring
To do this part please follow the schematic just below:

![electronic image 3 &](/pictures/electronic_schema.PNG)

## Raspberry PI and Arduino setup
*This step assumes that Linux, python 3 and git are already installed on the Raspberry PI.*

### Part 1 : Raspberry PI setup

Clone the git repo:
 1. Run the following command to download the repo:
`git clone https://github.com/Wizard-s-Chess/Wizards-Chess.git`

Install the packages:
1. cd in the directory of the downloaded repo
1. Run the following command to install all the packages
`pip install -r requirements.txt`

### Part 2 : Arduino setup
1. Upload the motors sketch (found in the directory /arduino/motors) on the arduino via the arduino IDE.

### Part 3 : ESP32 Cam setup
1. Connect the ESP32 Cam to the laptop via the USB to Serial adapter
2. Flash the ESP32 Cam (with the same software as the arduino).

### Part 4 : Connect the raspberry PI to the ESP32 cam wifi
Once the ESP32 Cam is set up a new wifi is available to connect on. Connect to this wifi on the raspberry PI.

### Part 5 : Connect the raspberry PI to arduino
You can connect the raspberry pi to the arduino either via a USB cable or directly the the pi's uart ports in the GPIO. Either way, you have to change the location of the chosen serial port in the 'PhysicalBoard.py' file.

## Run the project

Once everything is done, the program can be run via from the command line.
To launch the main program on the raspberry pi, you have to get in the "Main Firmware" directory and run

`python -O WizardsChess.py`

## Members :

| Name                | Email                       |
|---------------------|-----------------------------|
| Jules Maglione      | jules.maglione@epfl.ch      |
| Paul Nadal          | paul.nadal@epfl.ch          |
| Khalil Acheche      | khalil.acheche@epfl.ch      |
| Yassine Abdennadher | yassine.abdennadher@epfl.ch |
| Ambroise Borbely    | ambroise.borbely@epfl.ch    |
