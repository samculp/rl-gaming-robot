# Solenoid Driver PCB

Custom PCB for interfacing the Arduino with four 12 V solenoid actuators.

## Components

| Component                      | Quantity | Purpose                                                                                                 |
| ------------------------------ | -------: | ------------------------------------------------------------------------------------------------------- |
| IRLZ44N N-channel MOSFET       |        4 | Electrically switches each solenoid on and off using the Arduino control signal.                        |
| 1N4004 diode                   |        4 | Provides flyback protection by suppressing the voltage spike generated when a solenoid is switched off. |
| 220 Ω gate resistor            |        4 | Limits current into each MOSFET gate and provides controlled gate drive.                                |
| 10 kΩ pull-down resistor       |        4 | Pulls the gate of each MOSFET down to GND when it is not being driven HIGH by the Arduino.              |
| Green LED                      |        1 | Indicates that the PCB is receiving power.                                                              |
| 1 kΩ resistor                  |        1 | Limits current through the power indicator LED.                                                         |
| 2-position screw terminal      |        1 | Provides the 12 V power input connection.                                                               |
| 2-position screw terminal      |        4 | Provides connections for the four solenoids and power/ground distribution.                              |
| 5-position screw terminal      |        1 | Provides the control signal and ground connections between the Arduino and PCB.                         |
| 7.5 A blade fuse               |        1 | Protects the PCB and solenoid power circuit from excessive current.                                     |
| Fuse holder                    |        1 | Holds the 7.5 A blade fuse in the solenoid power path.                                                  |
| M2 mounting holes              |        4 | Secure the PCB to the mechanical assembly.                                                              |

## Files

* `solenoid_driver.kicad_sch` — Electrical schematic.
* `solenoid_driver.kicad_pcb` — PCB layout.
* `solenoid_driver.kicad_pro` — KiCad project file.
