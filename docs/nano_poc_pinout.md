# Arduino Nano Cooling Controller PoC

# Potwierdzone fakty

## OLED [CONFIRMED]

```text
OLED SCL -> Nano D13
OLED SDA -> Nano D11
OLED DC  -> Nano D7
OLED RES -> Nano D8
OLED GND -> GND
```

## OLED VCC [TESTED]

```text
Podczas działającego testu Arduino:
około 3.0-3.1 V
```

# Założenia projektowe PoC

Cała pozostała konfiguracja jest obecnie:

```text
[PLANNED]
```

## Nano [PLANNED]

```text
D0  -> Serial RX / wolny
D1  -> Serial TX / wolny

D2  -> BUTTON UP
D3  -> BUTTON DOWN
D4  -> BUTTON LEFT
D5  -> BUTTON RIGHT
D6  -> BUTTON OK

D7  -> OLED DC
D8  -> OLED RESET

D9  -> FAN1 PWM -> ULN2803A
D10 -> FAN2 PWM -> ULN2803A

D11 -> OLED MOSI / DATA
D12 -> FREE
D13 -> OLED CLK

A0 -> POT1 100k
A1 -> POT2 100k
A2 -> POT3 10k
A3 -> FREE

A4 -> ADS1115 SDA
A5 -> ADS1115 SCL
```

Wyraźnie:

```text
Nano A0/A1/A2 = potencjometry
ADS1115 A0/A1 = termistory
```

## COMMON GND [PLANNED]

Planowany wspólny punkt:

```text
Nano GND
ADS1115 GND
OLED GND
ULN2803A GND
12 V PSU GND
FAN1 GND
FAN2 GND
NTC GND
buttons GND
potentiometers GND
```

## ADS1115 [PLANNED]

```text
ADS VDD  -> Nano 5V
ADS GND  -> COMMON GND
ADS SDA  -> Nano A4
ADS SCL  -> Nano A5
ADS ADDR -> GND
```

Adres:

```text
0x48
```

Kanały:

```text
ADS A0 -> NTC1
ADS A1 -> NTC2
ADS A2 -> FREE
ADS A3 -> FREE
```

## NTC [PLANNED]

```text
NTC1: 10k B3950 1%
NTC2: 10k B3950 1%
```

Dzielniki:

```text
+5V
 |
10k fixed
 |
 +---- ADS input
 |
NTC
 |
GND
```

## Przyciski [PLANNED]

```text
UP    -> D2
DOWN  -> D3
LEFT  -> D4
RIGHT -> D5
OK    -> D6
```

Druga strona:

```text
COMMON GND
```

Plan:

```cpp
INPUT_PULLUP
```

## ULN2803A [PLANNED]

```text
Nano D9  -> ULN IN1
Nano D10 -> ULN IN2

ULN pin 9  -> COMMON GND
ULN pin 10 -> NC

ULN pin 18 -> FAN1 PWM
ULN pin 17 -> FAN2 PWM
```

## Wentylatory [PLANNED]

```text
FAN1:
pin 1 -> GND
pin 2 -> +12 V
pin 3 -> TACH / nieużywany
pin 4 -> ULN pin 18

FAN2:
pin 1 -> GND
pin 2 -> +12 V
pin 3 -> TACH / nieużywany
pin 4 -> ULN pin 17
```

## PWM [PLANNED]

```text
D9 + D10
Timer1
około 25 kHz
```

Status:

```text
[PLANNED]
```

## Potencjometry [PLANNED]

```text
POT1 100k -> A0
POT2 100k -> A1
POT3 10k  -> A2
```

Każdy:

```text
outer -> +5 V
wiper -> analog input
outer -> GND
```

