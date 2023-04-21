#include <SPI.h>
#include <MFRC522.h>
 
#define SS_PIN 53
#define RST_PIN 5
MFRC522 mfrc522(SS_PIN, RST_PIN);
 
void setup() 
{
  Serial.begin(9600);
  SPI.begin();
  mfrc522.PCD_Init();
}

void loop(){
  if (!mfrc522.PICC_IsNewCardPresent()) {
    return;
  }
  if (!mfrc522.PICC_ReadCardSerial()) {
    return;
  }
  
  byte uidBytes[3];
  for (byte i = 0; i < mfrc522.uid.size; i++) {
    uidBytes[i] = mfrc522.uid.uidByte[i];
  }
  

  for (byte i = 0; i < mfrc522.uid.size; i++) {
    Serial.print(uidBytes[i] < 0x4 ? "0" : "");
    Serial.print(uidBytes[i], HEX);
    Serial.print(" ");
  }
  
  delay(2000);
}
