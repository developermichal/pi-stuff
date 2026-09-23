# OLED 128x64 6-pin - Arduino Nano

## FAKTY

Posiadany moduł:

```text
OLED 128x64
6 pin
SH1106
4-wire SPI
brak osobnego CS
```

Piny:

```text
GND
VCC
SCL
SDA
RES
DC
```

W używanym trybie:

```text
SCL = SPI CLK
SDA = SPI MOSI / DATA
```

### [CONFIRMED]

Fizycznie działające połączenie:

```text
OLED SCL -> Arduino Nano D13
OLED SDA -> Arduino Nano D11
OLED DC  -> Arduino Nano D7
OLED RES -> Arduino Nano D8
OLED GND -> GND
```

Potwierdzona poprawka:

```text
DC  = D7
RES = D8
```

### [DEPRECATED]

Wcześniejsze odwrotne mapowanie DC/RES jest błędne i nie powinno być używane:

```text
OLED DC  -> Arduino Nano D8
OLED RES -> Arduino Nano D7
```

### [CONFIRMED IN SOURCE]

Aktualny plik:

```text
arduino_src/oled_6_pin_test/oled_6_pin_test.ino
```

zawiera:

```cpp
U8G2_SH1106_128X64_NONAME_F_4W_SW_SPI u8g2(
  U8G2_R0,
  13,              // CLK / SCL
  11,              // DATA / SDA
  U8X8_PIN_NONE,   // CS
  7,               // DC
  8                // RESET
);
```

Znaczenie:

```text
13 = CLK
11 = DATA / MOSI
CS = NONE
7  = DC
8  = RESET
```

### [TESTED]

Podczas działającego testu napięcie mierzone na VCC tego konkretnego OLED-a wynosiło około:

```text
3.0-3.1 V
```

Nie jest to nominalna specyfikacja wszystkich modułów SH1106.

## ZAŁOŻENIA PROJEKTOWE

Brak dodatkowych założeń projektowych w tym dokumencie.

