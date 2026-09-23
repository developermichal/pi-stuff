# OLED 128x64 6-pin - Raspberry Pi 3A+

## FAKTY

Testowany sprzęt:

```text
Raspberry Pi 3 Model A+
OLED SH1106 128x64 6-pin
SPI
```

### [CONFIRMED IN SOURCE]

Aktualny kod:

```text
src/6_pin_128_64_oled/oled_first_try.py
```

zawiera:

```python
serial = spi(
    port=0,
    device=0,
    gpio_DC=24,
    gpio_RST=25
)

device = sh1106(serial)
```

Konfiguracja:

```text
port=0      -> SPI0
device=0    -> /dev/spidev0.0
gpio_DC=24  -> BCM24 -> physical pin 18
gpio_RST=25 -> BCM25 -> physical pin 22
```

Używane połączenie testowe:

```text
OLED VCC -> physical pin 17 -> 3.3 V
OLED GND -> physical pin 20 -> GND

OLED SDA -> physical pin 19 -> BCM10 -> SPI0 MOSI
OLED SCL -> physical pin 23 -> BCM11 -> SPI0 SCLK

OLED DC  -> physical pin 18 -> BCM24
OLED RES -> physical pin 22 -> BCM25
```

### [TESTED]

```text
/dev/spidev0.0
/dev/spidev0.1
```

istnieją.

Python uruchamia się bez tracebacka.

OLED pozostaje czarny.

### [TESTED] RESET

```text
OLED VCC względem GND:
około 3.0 V

BCM25 / physical pin 22 bez OLED:
3.3 V po ustawieniu HIGH

RES -> GND na całkowicie odłączonym OLED:
około 21 MOhm

OLED podłączony wyłącznie do VCC i GND:
RES względem GND około 0.59 V
```

Wcześniejsze `5.9 V` było błędne.

### [UNDER INVESTIGATION]

Problem dotyczy linii:

```text
RES / RESET
```

Konkretna przyczyna nie jest zapisana jako fakt, dopóki nie zostanie potwierdzona.

## ZAŁOŻENIA PROJEKTOWE

Brak dodatkowych założeń projektowych w tym dokumencie.

