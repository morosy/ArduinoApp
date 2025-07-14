const int trigPin = 9;
const int echoPin = 10;

void setup() {
    Serial.begin(9600);
    pinMode(trigPin, OUTPUT);
    pinMode(echoPin, INPUT);
}

void loop() {
    long duration;
    float distance;

    // トリガーパルスを送信（10マイクロ秒のHIGH）
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);

    // Echoピンで受信時間を測定
    duration = pulseIn(echoPin, HIGH);

    // 音速は約 340m/s（＝0.034 cm/μs） → 往復なので2で割る
    distance = duration * 0.034 / 2;

    // 距離を表示（単位：cm）
    Serial.print("距離: ");
    Serial.print(distance);
    Serial.println(" cm");

    delay(2000);  // 測定間隔（500ms）
}
