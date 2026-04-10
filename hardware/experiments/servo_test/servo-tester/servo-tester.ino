#include <Servo.h>

Servo servo;

const int SERVO_PIN = 9;
const int REST_ANLGE = 90;
const int PRESS_ANGLE = 110;

void setup() {
  servo.attach(SERVO_PIN);
  servo.write(REST_ANGLE);
  delay(1000);
}

void loop() {
  // press
  servo.write(PRESS_ANLGLE);
  delay(100);

  // release
  servo.write(REST_ANGLE);
  delay(2000);
}
