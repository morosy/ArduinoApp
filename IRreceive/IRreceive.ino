#include <IRremote.hpp>

const int RECV_PIN = 2;  // VS1838BのOUTピンを接続したデジタルピン

void setup() {
    Serial.begin(9600);
    IrReceiver.begin(RECV_PIN, ENABLE_LED_FEEDBACK);  // IR受信を開始
    Serial.println("IR Receiver Ready");
}

void loop() {
    if (IrReceiver.decode()) {
        Serial.print("Received IR code: 0x");
        Serial.println(IrReceiver.decodedIRData.decodedRawData, HEX);
        IrReceiver.resume();
    }
}
