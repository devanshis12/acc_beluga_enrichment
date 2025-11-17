#include <SD.h>
const int chipSelect = 10;
const int sensorPins[5] = {2, 3, 4, 5, 6};
int sensorStates[5];

void setup() {
  Serial.begin(9600);                                         // initialize serial monitor
  for (int i = 0; i < 5; i++) pinMode(sensorPins[i], INPUT);  // set all input pins
  if (!SD.begin(chipSelect)) {                                // initialize SD card
    Serial.println("SD Card initialization failed!");
    while (1); // Stop if SD fails
  }
  Serial.println("SD Card initialized.");
}

void loop() { 
  for (int i = 0; i < 5; i++) {                   // for each sensor
    sensorStates[i] = digitalRead(sensorPins[i]); // read input from sensor
  }
  
  File dataFile = SD.open("vibdata.csv", FILE_WRITE); // open SD card file to write to
  if (dataFile) {
    dataFile.print(sensorStates[0]);       // write the first sensor state
    for (int i = 1; i < 5; i++) {
      dataFile.print(",");                 // seperate each input by a comma
      dataFile.print(sensorStates[i]);     // get next sensor state
    }
    dataFile.println();                
    dataFile.close();
  } else {
    Serial.println("Could not open file."); // throw error if SD file doesn't open
  }
  delay(1000); // get reading every second
}
