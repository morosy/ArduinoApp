import requests


def read_token(path):
    with open(path, 'r') as f:
        return f.read().strip()


# トークンの読み込み
API_TOKEN = read_token("IDs/token.txt")

HEADERS = {
    'Authorization': API_TOKEN,
    'Content-Type': 'application/json; charset=utf8'
}

# 学習済みリモコンのID
CEILING_LIGHT_DEVICE_ID = read_token("IDs/ceiling_light_device_id.txt")  # シーリングライト

# ONコマンド（通常は赤外線リモコンで「電源」ボタンに相当）
payload = {
    "command": "turnOn",
    "parameter": "default",
    "commandType": "command"
}

url = f"https://api.switch-bot.com/v1.0/devices/{CEILING_LIGHT_DEVICE_ID}/commands"
response = requests.post(url, headers=HEADERS, json=payload)

print(f"Status: {response.status_code}")
print(f"Response: {response.text}")
