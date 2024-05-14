const unsigned long timeout = 1000;

unsigned long lastReceivedA = 0;
unsigned long lastReceivedB = 0;
unsigned long lastReceivedC = 0;

void setup() {
  Serial.begin(9600);
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
}

void loop() {
  unsigned long currentMillis = millis();

  if (Serial.available() > 0) {
    char data = Serial.read();
    
    if (data == 'A') {
      digitalWrite(8, HIGH);
      lastReceivedA = currentMillis;
    } else if (data == 'a') {
      digitalWrite(8, LOW);
      lastReceivedA = currentMillis;
    }
    
    if (data == 'B') {
      digitalWrite(9, HIGH);
      lastReceivedB = currentMillis;
    } else if (data == 'b') {
      digitalWrite(9, LOW);
      lastReceivedB = currentMillis;
    }
    
    if (data == 'C') {
      digitalWrite(10, HIGH);
      lastReceivedC = currentMillis;
    } else if (data == 'c') {
      digitalWrite(10, LOW);
      lastReceivedC = currentMillis;
    }
  }

  if (currentMillis - lastReceivedA >= timeout) {
    digitalWrite(8, LOW);
  }
  
  if (currentMillis - lastReceivedB >= timeout) {
    digitalWrite(9, LOW);
  }

  if (currentMillis - lastReceivedC >= timeout) {
    digitalWrite(10, LOW);
  }
}