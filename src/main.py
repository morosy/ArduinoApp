import serial
import requests
import time

# シリアルポート設定
SERIAL_PORT = '/dev/cu.usbmodem11101'
BAUD_RATE = 9600

# トークン・デバイスID読み込み
def read_token(path):
    with open(path, 'r') as f:
        return f.read().strip()

API_TOKEN = read_token("IDs/token.txt")
CEILING_LIGHT_DEVICE_ID = read_token("IDs/ceiling_light_device_id.txt")

HEADERS = {
    'Authorization': API_TOKEN,
    'Content-Type': 'application/json; charset=utf8'
}

# SwitchBotコマンド送信関数
def send_switchbot_turn_on():
    url = f"https://api.switch-bot.com/v1.0/devices/{CEILING_LIGHT_DEVICE_ID}/commands"
    payload = {
        "command": "turnOn",
        "parameter": "default",
        "commandType": "command"
    }
    response = requests.post(url, headers=HEADERS, json=payload)
    print(f"[SwitchBot] turnOn sent. Status: {response.status_code}")

# 距離を監視し、100cm未満でAPI呼び出し
def monitor_distance_and_trigger():
    with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=2) as ser:
        already_triggered = False  # 多重実行防止
        while True:
            line = ser.readline().decode().strip()
            if line.startswith("DIST:"):
                try:
                    distance = float(line.replace("DIST:", ""))
                    print(f"[Arduino] 距離: {distance} cm")

                    if distance < 100 and not already_triggered:
                        print("[Action] 100cm未満 turnOn を実行")
                        send_switchbot_turn_on()
                        already_triggered = True

                    elif distance >= 100:
                        already_triggered = False  # 再び近づくまでリセット

                except ValueError:
                    continue

if __name__ == "__main__":
    monitor_distance_and_trigger()
