int vib_pin=7;
int chipSelect=10;

void setup() {
  pinMode(vib_pin,INPUT);
  Serial.begin(9600);
  if (!SD.begin(chipSelect)) {
    Serial.println("SD card initialization failed");
    while (1);
  }
  Serial.println("SD card initialized");
}

void loop() {
  int val;
  val=digitalRead(vib_pin);
  File dataFile = SD.open("vibdata.csv", FILE_WRITE);
  if (datafile) {
    datafile.print(val);
    datafile.println();
    datafile.close();
  } else {
    Serial.println("Could not open file");
  }
  delay(2000);
}
