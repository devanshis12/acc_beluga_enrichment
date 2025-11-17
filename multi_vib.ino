const int sensorPins[5] = {2, 3, 4, 5, 6}; // Sensors connected to these pins
int sensorStates[5]; // Array to store state of each sensor

void setup() {
  Serial.begin(9600);
  for (int i = 0; i < 5; i++) {
    pinMode(sensorPins[i], INPUT);
  }
}

void loop() {
  for (int i = 0; i < 5; i++) {
    sensorStates[i] = digitalRead(sensorPins[i]);
    Serial.print("Sensor ");
    Serial.print(i + 1);
    Serial.print(": ");
    Serial.println(sensorStates[i]);
  }
  delay(2000); // Short delay between readings
}
