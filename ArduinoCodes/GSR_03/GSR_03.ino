const int signalPin = A0; // GSR signal connected to A0
const int referencePin = A1; // Reference signal connected to A1

void setup() {
  Serial.begin(115200);
}

void loop() {
  // Read the voltage across the GSR electrode (voltage divider)
  int signalValue = analogRead(signalPin);
  
  // Read the voltage across the reference electrode (voltage divider)
  int referenceValue = analogRead(referencePin);

  // Calculate the difference between the GSR signal and the reference signal
  int differentialValue = signalValue - referenceValue;

  // Output the differential value
  Serial.println(differentialValue);

  delay(1); // delay in between reads for stability
}

