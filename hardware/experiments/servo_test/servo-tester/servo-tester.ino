#include <Servo.h>

Servo servo;

const int SERVO_PIN = 9;
const int REST_ANGLE = 90;
const int PRESS_ANGLE = 120;

void setup() {
  servo.attach(SERVO_PIN);
  servo.write(REST_ANGLE);
  delay(1000);
}

void loop() {
  pressButton();
  delay(1200); 
}

void pressButton() {
  // press
  servo.write(PRESS_ANGLE);
  delay(100);

  // release
  servo.write(REST_ANGLE);
  delay(100);
}