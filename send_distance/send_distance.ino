const int trigPin = 9;
const int echoPin = 10;

void setup() {
    Serial.begin(9600);
    pinMode(trigPin, OUTPUT);
    pinMode(echoPin, INPUT);
}

void loop() {
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);

    long duration = pulseIn(echoPin, HIGH, 30000);
    float distance = duration * 0.034 / 2;

    if (distance > 2 && distance < 400) {
        Serial.print("DIST:");
        Serial.println(distance);  // 「DIST:xx.xx」形式
    }

    delay(1000);  // 1秒おきに送信
}
