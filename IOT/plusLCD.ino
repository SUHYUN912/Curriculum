#include "BluetoothSerial.h"
#include <Wire.h> 
#include <LiquidCrystal_I2C.h>
BluetoothSerial SerialBT;
LiquidCrystal_I2C lcd(0x27,16,2); 

void setup() {
  Serial.begin(115200);
  SerialBT.begin("ESP32:66"); 
  lcd.init();         // initialize the lcd 
  lcd.backlight();
  lcd.print("Hello, world!");
}
void loop(){
if(SerialBT.available()>0){
  char data = SerialBT.read();  
  Serial.write(data);
  Serial.println();
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print("result is ");
  lcd.print(data);
  }
}
