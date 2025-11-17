int vib_pin=7;
int led_pin=13;

void setup() {
 pinMode(vib_pin,INPUT);
 pinMode(led_pin,OUTPUT);
 Serial.begin(9600);
}


void loop() {
 int val;
 val=digitalRead(vib_pin);
 if(val==1)
 {
   digitalWrite(led_pin,HIGH);
   Serial.println(val);
   delay(1000);
   digitalWrite(led_pin,LOW);
   delay(1000);
  }
  else
  digitalWrite(led_pin,LOW);
  Serial.println(val);
}
