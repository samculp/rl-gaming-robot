# RL Gaming Robot Hardware

This directory contains the hardware development files for the RL Gaming Robot project. It includes experimental prototypes, hardware tests, and CAD files.

## Directory Structure

```text
hardware/
├── experiments/
│   ├── actuator_pulse/
│   └── cad_files/
└── production/
```

## Experiments

The `experiments` directory contains prototypes, tests, and early-stage hardware development.

### actuator_pulse

Contains experiments and code related to controlling and testing the actuators used to physically interact with the gaming controller.

These experiments are used to test actuator timing, pulse duration, and button actuation behavior before integrating the hardware into the complete robot.

### cad_files

Contains CAD models and designs created during the experimental hardware development process.

These files may include prototypes, mounting systems, actuator assemblies, controller holders, and other mechanical components.

## Production

The `production` directory contains hardware designs, code, and documentation intended for the final integrated version of the RL Gaming Robot.

Files in this directory should represent tested and validated designs rather than experimental prototypes.

## Development Philosophy

Hardware development is organized into two stages:

1. **Experiments** — Prototype and test individual components and concepts.
2. **Production** — Integrate validated components into the final robot design.

Experimental designs should be tested and validated before being moved or adapted for use in the production hardware.
