#include "SDS011.h"

float p10,p25;
int error;

SDS011 my_sds;

void setup() {
  my_sds.begin(0, 1);
  Serial.begin(9600);
  while (!Serial) {
    ;
  }
}

void loop() {
  error = my_sds.read(&p25,&p10);
  if (! error) {
    Serial.println("P2.5: "+String(p25));
    Serial.println("P10:  "+String(p10));
  }
  delay(100);
}

