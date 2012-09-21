int doorbell = 2;
int prevValue = 0;

void setup()
{
 Serial.begin(9600); 
 Serial.println("hellooooo!");
}

void loop()
{
  int bellValue = digitalRead(doorbell);
  
  if(bellValue && bellValue != prevValue){
    Serial.println("dingdong");
  }
  prevValue = bellValue;
  delay(10);
}
