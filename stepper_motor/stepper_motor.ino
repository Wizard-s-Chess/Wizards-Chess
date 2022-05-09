#include <Stepper.h>

const int stepsPerRevolution = 200;
Stepper xStepper(stepsPerRevolution, 3, 2);
Stepper yStepper(stepsPerRevolution, 6, 5);
int xTurn = 0;
unsigned long previousMillis = 0;
long semiTime = 650;

void setup() {
   // set the speed at 60 rpm:
   xStepper.setSpeed(1000);
   yStepper.setSpeed(1000);

   Serial.begin(9600);
   delay(3000);
}

void loop() {
   goDiagoRight();
}


void goDiagoRight() {
  delay(500);
   unsigned long begin = millis();
   for (long curr = millis(); curr - begin < semiTime; curr = millis())
   {
      goRight();
   }
   delay(500);
   begin = millis();
   for (long curr = millis(); curr - begin < semiTime; curr = millis())
   {
      goUp();
   }
}

void goRight() {
  xStepper.step(stepsPerRevolution);
}

void goLeft() {
   xStepper.step(-stepsPerRevolution);
}

void goUp() {
   yStepper.step(stepsPerRevolution);
}

void goDown() {
   yStepper.step(-stepsPerRevolution);
}
