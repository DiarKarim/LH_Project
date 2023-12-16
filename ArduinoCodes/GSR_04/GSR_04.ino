const int signalPin = A0; // GSR signal connected to A0
const int referencePin = A1; // Reference signal connected to A1
const int numReadings = 10; // number of readings to average

int signalReadings[numReadings]; // array to store signal readings
int referenceReadings[numReadings]; // array to store reference readings
int readIndex = 0; // current index in the reading arrays
int totalSignal = 0; // running total of the signal readings
int totalReference = 0; // running total of the reference readings

void setup() {
  Serial.begin(115200);
  // initialize all the readings to 0:
  for (int thisReading = 0; thisReading < numReadings; thisReading++) {
    signalReadings[thisReading] = 0;
    referenceReadings[thisReading] = 0;
  }
}

void loop() {
  // subtract the last reading:
  totalSignal -= signalReadings[readIndex];
  totalReference -= referenceReadings[readIndex];
  
  // read from the sensor:
  signalReadings[readIndex] = analogRead(signalPin);
  referenceReadings[readIndex] = analogRead(referencePin);
  
  // add the reading to the total:
  totalSignal += signalReadings[readIndex];
  totalReference += referenceReadings[readIndex];
  
  // advance to the next position in the array:
  readIndex = (readIndex + 1) % numReadings;
  
  // calculate the average:
  int averageSignal = totalSignal / numReadings;
  int averageReference = totalReference / numReadings;
  
  // calculate the differential value:
  int differentialValue = averageSignal - averageReference;
  
  // send it to the computer (as ASCII digits):
  Serial.println(differentialValue);
  
  delay(10); // delay in between reads for stability
}

