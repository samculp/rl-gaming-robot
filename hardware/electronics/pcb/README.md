# Solenoid Driver PCB

Custom PCB for interfacing the Arduino with the 12 V solenoid actuators.

## Functions

- Switches solenoids using IRLZ44N MOSFETs
- Provides flyback protection using 1N4004 diodes
- Provides gate resistors for MOSFET control
- Provides LED power indication
- Distributes fused 12 V power to the solenoids
- Provides screw-terminal connections for power, control, and solenoids

## Files

- `solenoid_driver.kicad_sch` — Schematic
- `solenoid_driver.kicad_pcb` — PCB layout
- `solenoid_driver.kicad_pro` — KiCad project