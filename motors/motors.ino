#include <Stepper.h>
#include <EEPROM.h>


int powerPin = 10;
int power = 255;
int activatePin = 8;
int deactivatePin = 9;


const int stepsPerRevolution = 200;
const int stepsPerHalfSquare= 2000;
Stepper xStepper(stepsPerRevolution, 3, 2);
Stepper yStepper(stepsPerRevolution, 6, 5);
long semiTime = 650;
int incomingByte;
int speedMotor = 1500;
int pinMagnet = 7;
int ledPin = 13;
int xButton = 11;
int yButton = 12;
int x;
int y;
void setup() {
   xStepper.setSpeed(speedMotor);
   yStepper.setSpeed(speedMotor);
   pinMode(pinMagnet, OUTPUT);
   pinMode(ledPin, OUTPUT);
   pinMode(powerPin, OUTPUT);
   pinMode(activatePin, OUTPUT);
   pinMode(deactivatePin, OUTPUT);
   pinMode(xButton, INPUT);
   pinMode(yButton, INPUT);
   pinMode(A5, OUTPUT);
   digitalWrite(A5,HIGH);
   deactivateMagnet();
      
   Serial.begin(9600);
   delay(500);
   x = EEPROM.read(0);
   y = EEPROM.read(1);
   goHome();
   
}

void loop() {
  if (Serial.available() > 0) {
    incomingByte = Serial.read();
    if (incomingByte == '1') {
      goLeft();
    }
    if (incomingByte == '2') {
      goRight();
    }
    if (incomingByte == '3') {
      goDown();
    }
    if (incomingByte == '4') {
      goUp();
    }
    if (incomingByte == '5') {
      go_diagonal_up_right();
    }
    if (incomingByte == 'm') {
      activateMagnet();
    }
    if (incomingByte == 'n') {
      deactivateMagnet();  
    }
    if(incomingByte == 'f'){
      Serial.write("f");
    }
  }
}

void activateMagnet() {
  digitalWrite(activatePin, HIGH);
  digitalWrite(deactivatePin, LOW);
  analogWrite(powerPin, power);
  /*
  digitalWrite(pinMagnet, HIGH);*/
  digitalWrite(ledPin, HIGH);
}

void deactivateMagnet() {
  
  digitalWrite(activatePin, LOW);
  digitalWrite(deactivatePin, HIGH);
  analogWrite(powerPin, power);
  /*
  digitalWrite(pinMagnet, LOW);*/
  digitalWrite(ledPin, LOW);
}

void goRight() {
  xStepper.step(stepsPerHalfSquare);
  /*
  unsigned long begin = millis();
  for (long curr = millis(); curr - begin < semiTime; curr = millis())
  {
      xStepper.step(stepsPerRevolution);
  }*/
  x=x+1;
  EEPROM.write(0, x);
}
void go_diagonal_up_right(){
  xStepper.step(stepsPerHalfSquare);
  yStepper.step(stepsPerHalfSquare);
}

void goLeft() {
  /*
  if(digitalRead(xButton) == 0){
    return;
  }*/
  xStepper.step(-stepsPerHalfSquare);
  /*
  unsigned long begin = millis();
  for (long curr = millis(); curr - begin < semiTime; curr = millis())
  {
      xStepper.step(-stepsPerRevolution);
  }*/
  x=x-1;
  if(x<0){
    x =0;
  }
  EEPROM.write(0, x);
}

void goUp() {
  yStepper.step(stepsPerHalfSquare);
  /*
  unsigned long begin = millis();
  for (long curr = millis(); curr - begin < semiTime; curr = millis())
  {
      yStepper.step(stepsPerRevolution);
  }*/
  
  y=y+1;
  EEPROM.write(1, y);
}

void goDown() {/*
  if(digitalRead(yButton) == 0){
    return;
  }*/
  yStepper.step(-stepsPerHalfSquare);
  /*
  unsigned long begin = millis();
  for (long curr = millis(); curr - begin < semiTime; curr = millis())
  {
      yStepper.step(-stepsPerRevolution);
  }
  y = y-1;
  if(y<0){
    y=0;
  }*/
  EEPROM.write(1, y);
}
void goHome(){
  for(int state = digitalRead(xButton); state !=0 ;state = digitalRead(xButton)){
    xStepper.step(-stepsPerRevolution);
    delay(1);
  }
  for(int state = digitalRead(yButton); state !=0 ;state = digitalRead(yButton)){
    yStepper.step(-stepsPerRevolution);
    delay(1);
  }
}
