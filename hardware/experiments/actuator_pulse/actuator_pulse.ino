// testing one unit of the robot
// continuously pulses to trigger the solenoid
// pin 2 is connected to the gate of the MOSFET

const int solenoidPin = 2;

void setup() {
  Serial.begin(115200);
  Serial.println("Enter 1 to pulse:");
  pinMode(solenoidPin, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    
    if (command == '1') {
      pulse();
    }
  }
}

void pulse() {
  digitalWrite(solenoidPin, HIGH);
  delay(3000);
  digitalWrite(solenoidPin, LOW);
}