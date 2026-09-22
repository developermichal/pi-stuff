#include <U8g2lib.h>

U8G2_SH1106_128X64_NONAME_F_4W_SW_SPI u8g2(
  U8G2_R0,
  13,              // CLK / SCL
  11,              // DATA / SDA
  U8X8_PIN_NONE,   // CS
  7,               // DC
  8                // RESET
);

void setup() {
  Serial.begin(115200);

  u8g2.begin();

  u8g2.clearBuffer();
  u8g2.setFont(u8g2_font_7x14B_tf);
  u8g2.drawStr(15, 25, "OLED DZIALA");
  u8g2.drawStr(25, 48, "SH1106");
  u8g2.sendBuffer();

  Serial.println("OLED FRAME SENT");
}

void loop() {
}