// Serial test script

#include <Servo.h>

Servo myservo; 
int pos = 0;

const int buzzerPin = 11;
void alert(){
  tone(buzzerPin,1000);
  delay(200);
  noTone(buzzerPin);
  delay(200);
  tone(buzzerPin,1500);
  delay(200);
  noTone(buzzerPin);
  delay(200);
  tone(buzzerPin,1300);
  delay(200);
  noTone(buzzerPin);
  delay(200);
  tone(buzzerPin,1500);
  delay(200);
  noTone(buzzerPin);
  delay(200);
}
int setPoint = 55;
byte readString;

void setup()
{
  myservo.attach(9);
  myservo.write(5);
  Serial.begin(9600);  // initialize serial communications at 9600 bps

}

void servo(){
    myservo.write(90);              // tell servo to go to position in variable 'pos'
    delay(3000);
    myservo.write(5);
  }

void loop()
{
  
  while(!Serial.available()) {}
  // serial read section
  while (Serial.available())
  {
    if (Serial.available() >0)
    {
      readString= Serial.read();
    }
  }

    if(readString==97)
      {Serial.println("terima"); 
      servo();
       return;
      }
    if(readString==98)
      {Serial.println("gagal"); 
      alert();
       return;
      }

  
}
