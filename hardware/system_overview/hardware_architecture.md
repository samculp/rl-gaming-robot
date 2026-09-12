# Hardware Architecture

## Control Flow

RL agent → Python → USB → Arduino → MOSFET driver → Solenoid → Controller button

The RL agent selects an action. Python sends the corresponding command to the Arduino over USB. The Arduino drives the appropriate MOSFET, which activates the corresponding solenoid to physically press the controller button. The output from the controller is then fed back to the computer over USB, completing the loop.

## Power Path

Battery → BMS → in-line switch → XT60 → Fuse → PCB → Solenoids

The power supply was created using 9 18650 lithium ion cells harvested from an autonomous Samsung floor vacuum. The each cell is ~1.8 Ah, 4.2 V nominal. The battery pack is configured as 3S3P, making it a 12.6V 5.4 Ah battery. A BMS (battery management system) is connected to the pacl and serves the following purposes:

- Overcharge protection - prevents cells from being charged beyond their safe voltage
- Over-discharge protection - disconnects the pack if cell voltage falls too low
- Overcurrent/short-circuit protection - disconnects the pack when excessive current is detected
- Cell blancing - helps keep the three series cell groups at similar voltages during charging

The battery supplies power to the solenoids through the BMS, in-line switch, and PCB. A 7.5 A blade fuse is mounted on the PCB. The Arduino is powered separately through its USB connection.