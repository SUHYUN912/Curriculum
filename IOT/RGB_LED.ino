//This example code is in the Public Domain (or CC0 licensed, at your option.)
//By Evandro Copercini - 2018
//
//This example creates a bridge between Serial and Classical Bluetooth (SPP)
//and also demonstrate that SerialBT have the same functionalities of a normal Serial

#include "BluetoothSerial.h"

#if !defined(CONFIG_BT_ENABLED) || !defined(CONFIG_BLUEDROID_ENABLED)
#error Bluetooth is not enabled! Please run `make menuconfig` to and enable it
#endif

BluetoothSerial SerialBT;

void setup() {
  Serial.begin(115200);
  SerialBT.begin("ESP32_06"); //Bluetooth device name
  Serial.println("The device started, now you can pair it with bluetooth!");

  pinMode(12, OUTPUT);
  pinMode(13, OUTPUT);
  pinMode(14, OUTPUT);

  digitalWrite(12, LOW);
  digitalWrite(13, LOW);
  digitalWrite(14, LOW);
}

void loop() {
  if (SerialBT.available()) {
    char data = SerialBT.read();

    if(data=='1')
  {
    digitalWrite(12, HIGH);
    digitalWrite(13, LOW);
    digitalWrite(14, LOW);
    Serial.println("STOP");
  }
  else if(data=='2')
  {
    digitalWrite(14, HIGH);
    digitalWrite(12, LOW);
    digitalWrite(13, LOW);
    Serial.println("WAIT");
  }
  else if(data=='3')
  {
    digitalWrite(13, HIGH);
    digitalWrite(12, LOW);
    digitalWrite(14, LOW);
    Serial.println("PASS");
  }
  }
  delay(20);
}
