from luma.core.interface.serial import spi
from luma.oled.device import sh1106
from luma.core.render import canvas


# -------------------------------------------------
# Konfiguracja SPI
#
# port=0   -> SPI0
# device=0 -> /dev/spidev0.0
#
# gpio_DC=24  -> BCM GPIO24 -> fizyczny pin 18
# gpio_RST=25 -> BCM GPIO25 -> fizyczny pin 22
# -------------------------------------------------

serial = spi(
    port=0,
    device=0,
    gpio_DC=24,
    gpio_RST=25
)


# Tworzymy obiekt reprezentujący ekran SH1106
device = sh1106(serial)


# canvas() tworzy bufor obrazu.
# Wszystko, co narysujemy wewnątrz tego bloku,
# zostanie wysłane do OLED-a.
with canvas(device) as draw:

    draw.text(
        (10, 10),
        "Hello Pi!",
        fill="white"
    )