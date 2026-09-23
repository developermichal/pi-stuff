# PC Cooling Controller / Hardware Experiments

This repository contains hardware experiments for a PC cooling controller.

The project has two separate tracks:

1. Arduino Nano Proof of Concept
2. Target RP2040 + Raspberry Pi 3A+ project

Do not mix pin mappings between these two project tracks.

## Documentation

- [OLED 128x64 6-pin - Arduino Nano](docs/oled_128x64_6pin_arduino.md)
- [OLED 128x64 6-pin - Raspberry Pi 3A+](docs/oled_128x64_6pin_pi3.md)
- [Arduino Nano Cooling Controller PoC](docs/nano_poc_pinout.md)

## Code

Arduino:

```text
arduino_src/oled_6_pin_test/oled_6_pin_test.ino
```

Raspberry Pi:

```text
src/6_pin_128_64_oled/oled_first_try.py
```

## Status Legend

```text
[CONFIRMED]
Physically checked and working.

[CONFIRMED IN SOURCE]
Confirmed by current source code.

[TESTED]
Physically tested; the result may be positive or negative.

[PLANNED]
Project assumption, not yet verified in hardware.

[UNDER INVESTIGATION]
Problem has been observed and is still being diagnosed.

[DEPRECATED]
Old setting that should not be used.
```

