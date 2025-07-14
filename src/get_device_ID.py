import requests

def read_token(path):
    with open(path, 'r') as f:
        return f.read().strip()

API_TOKEN = read_token("IDs/token.txt")
HEADERS = {
    'Authorization': API_TOKEN,
    'Content-Type': 'application/json; charset=utf8'
}

def list_devices():
    url = "https://api.switch-bot.com/v1.0/devices"
    response = requests.get(url, headers=HEADERS)
    data = response.json()

    if response.status_code == 200:
        print("【SwitchBot デバイス一覧】")
        for device in data["body"]["deviceList"]:
            print(f"- 名前: {device['deviceName']}")
            print(f"  ID: {device['deviceId']}")
            print(f"  種類: {device['deviceType']}")
            print("")
    else:
        print(f"エラー: {response.status_code} - {response.text}")

    for remote in data["body"]["infraredRemoteList"]:
        print(f"- 学習リモコン: {remote['deviceName']}")
        print(f"  ID: {remote['deviceId']}")
        print(f"  種類: {remote['remoteType']}")


if __name__ == "__main__":
    list_devices()
