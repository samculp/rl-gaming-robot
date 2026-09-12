# Power Budget

## Battery Pack

The battery pack consists of nine 18650 lithium-ion cells configured as 3S3P. Each cell has an approximate capacity of 1.8 Ah and a nominal voltage of 3.6-3.7 (4.2 V fully charged).

- Configuration: 3S3P
- Cells: 9 × 18650
- Nominal voltage: 10.8-11.1 V
- Maximum voltage: 12.6 V
- Capacity: 5.4 Ah
- Approximate energy: 58-60 Wh

## Power Path

Battery → BMS → In-line switch → XT60 → 7.5 A fuse → PCB → Solenoids

The BMS provides:
- Overcharge protection
- Over-discharge protection
- Overcurrent and short-circuit protection
- Cell balancing

The Arduino is powered separately through USB.

## Solenoid Load

Each solenoid is rated for 12 V and draws a maximum of 1.6 A.

| Load | Voltage | Max Current | Quantity | Total Max Current |
|---|---:|---:|---:|---:|
| Solenoid | 12 V | 1.6 A | 4 | 6.4 A |

The maximum combined solenoid current is approximately 6.4 A when all four solenoids are activated simultaneously.

## Protection

- Fuse: 7.5 A blade fuse
- Maximum solenoid load: 6.4 A
- Fuse margin: 1.1 A