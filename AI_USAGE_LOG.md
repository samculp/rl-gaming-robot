# AI Usage & Verification Log

**Project Name:** RL Gaming Robot  
**Project Area:** Hardware / Controller Input Experiment  

---

## Overview & AI Usage Statement

TODO

---

## Entry 1: Prototype 1 - SNES USB Controller Input Mapping Experiment

* **Date:** August 31, 2026  
* **Tool Used:** ChatGPT  
* **Associated Git Issue:** Test SNES USB controller input mapping  
* **Associated Feature Branch:** `controller-input-test`  

### Exact Prompt Submitted:

> "quick python script for testing input on this snes usb controller i just got from walmart"

### AI Output Summary & Code Generated

AI generated a Python script using the `pygame` library to:

* Detect connected USB controllers.
* Display the controller name.
* Display the number of buttons, axes, and hats detected.
* Print button press events.
* Print button release events.
* Print joystick axis movement values.
* Print D-pad or hat movement values when applicable.

The generated experiment allowed the physical SNES USB controller to be tested interactively.

### Human Testing, Verification & Results

The controller was manually tested using the generated Python experiment. The following input mappings were observed and recorded:

#### Button Mapping

| SNES Button | Input Mapping |
|---|---:|
| X | Button 0 |
| A | Button 1 |
| B | Button 2 |
| Y | Button 3 |
| Select | Button 8 |
| Start | Button 9 |

#### D-Pad Mapping

The controller D-pad was detected as two joystick axes rather than individual buttons or a joystick hat.

| Direction | Axis | Value When Pressed |
|---|---:|---:|
| Left | Axis 0 | -1 |
| Right | Axis 0 | 1 |
| Up | Axis 1 | -1 |
| Down | Axis 1 | 1 |
| Released | Axis 0 / Axis 1 | Approximately -0.01 |

### Human Review & Modifications Identified

Testing identified that the D-pad does not return exactly `0` when released. Instead, the controller reports a value of approximately `-0.01`.

Based on this result, future controller input handling should implement a dead zone rather than checking for an exact axis value of zero.

Example dead zone approach:

```python
DEADZONE = 0.5

if axis_0 < -DEADZONE:
    print("LEFT")
elif axis_0 > DEADZONE:
    print("RIGHT")

if axis_1 < -DEADZONE:
    print("UP")
elif axis_1 > DEADZONE:
    print("DOWN")