int pin0 = 0;


void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
}

void loop() {
  // put your main code here, to run repeatedly:

  int a0_val = analogRead(pin0);
  Serial.println(a0_val);
  
}
