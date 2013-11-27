#include <Bridge.h>
int pirPin = 7;
int minSecsBetweenEmails = 60; // 1 min
long lastSend = -minSecsBetweenEmails * 1000l;

void setup()
{
 pinMode(pirPin, INPUT);
 Bridge.begin();
 Bridge.put("D7","0");
}

void loop()
{
 long now = millis(); //get system time
 if (digitalRead(pirPin) == HIGH) //check D7 state
 {
   if (now > (lastSend + minSecsBetweenEmails * 1000l)) //Only put once a minute
     {
       Bridge.put("D7", "1");
       Bridge.put("A0",String(analogRead(A1)));
       lastSend = now;
     }

 }
 else { Bridge.put("D7","0");
      }
 delay(500);

}
