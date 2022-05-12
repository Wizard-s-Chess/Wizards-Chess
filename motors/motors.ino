#include <Stepper.h>

const int stepsPerRevolution = 200;
Stepper xStepper(stepsPerRevolution, 3, 2);
Stepper yStepper(stepsPerRevolution, 6, 5);
long semiTime = 400;
int incomingByte;
int speedMotor = 1500;
int pinMagnet = 13;

void setup() {
   xStepper.setSpeed(speedMotor);
   yStepper.setSpeed(speedMotor);
   pinMode(pinMagnet, OUTPUT);
   
   Serial.begin(9600);
   delay(500);
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
    if (incomingByte == 'm') {
      activateMagnet();
    }
    if (incomingByte == 'n') {
      deactivateMagnet();  
    }
  }
}

void activateMagnet() {
  digitalWrite(pinMagnet, HIGH);
}

void deactivateMagnet() {
  digitalWrite(pinMagnet, LOW);
}

void goRight() {
  unsigned long begin = millis();
  for (long curr = millis(); curr - begin < semiTime; curr = millis())
  {
      xStepper.step(stepsPerRevolution);
  }
  delay(500);
}

void goLeft() {
  unsigned long begin = millis();
  for (long curr = millis(); curr - begin < semiTime; curr = millis())
  {
      xStepper.step(-stepsPerRevolution);
  }
  delay(500);
}

void goUp() {
  unsigned long begin = millis();
  for (long curr = millis(); curr - begin < semiTime; curr = millis())
  {
      yStepper.step(stepsPerRevolution);
  }
  delay(500);
}

void goDown() {
  unsigned long begin = millis();
  for (long curr = millis(); curr - begin < semiTime; curr = millis())
  {
      yStepper.step(-stepsPerRevolution);
  }
  delay(500);
}
