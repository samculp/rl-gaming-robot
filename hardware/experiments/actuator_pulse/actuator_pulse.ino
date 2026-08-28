// testing one unit of the robot
// continuously pulses to trigger the solenoid
// pin 2 is connected to the gate of the MOSFET

const int solenoidPin = 2;

void setup() {
  Serial.begin(9600);
  pinMode(solenoidPin, OUTPUT);
}

void loop() {
  pulse();
  delay(1000);
}

void pulse() {
  digitalWrite(solenoidPin, HIGH);
  delay(100);
  digitalWrite(solenoidPin, LOW);
}