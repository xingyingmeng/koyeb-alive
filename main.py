import requests

# Koyeb 变量
app_url = "https://xxxx.koyeb.app/"    #填写koyeb的app域名或argo的域名
app_name = 'nezha'      # 填写应用名称
api_key = ''     # 填写api key
base_url = 'https://app.koyeb.com/v1/apps' 

# Telegram 变量，不填则默认不用
tgbot_token = ''    # 填写Telegram bot token
tgchat_id = ''    # 填写Telegram chat id

# 发送tg消息
def send_telegram_message(tgbot_token, tgchat_id, send_message):
    if tgbot_token and tgchat_id and send_message:
        response = requests.post(
            f'https://api.telegram.org/bot{tgbot_token}/sendMessage',
            json={"chat_id": tgchat_id, "text": send_message}
        )
        return response.status_code == 200

# 检查app的域名状态是否正常
def check_app_status(app_url, app_headers):
    try:
        response = requests.get(app_url, headers=app_headers)
        return response.status_code == 200
    except requests.RequestException as e:
        return False

# 恢复app
def resume_app(api_key, app_name):
    api_headers = {'Authorization': f'Bearer {api_key}'}
    response = requests.get(base_url, headers=api_headers)
    if response.status_code == 200:
        apps = response.json().get('apps', [])
        for app in apps:
            if app['name'] == app_name:
                app_id = app['id']
                app_status = app['status']
                # 如果 App 状态不是 HEALTHY，则尝试恢复
                if app_status != 'HEALTHY':
                    resume_url = f'{base_url}/{app_id}/resume'
                    resume_response = requests.post(resume_url, headers=api_headers)
                    if resume_response.status_code == 200:
                        send_message = "Koyeb app is successfully resumed !"
                        send_telegram_message(tgbot_token, tgchat_id, send_message)
                        return True
                    else:
                        print(f"Failed to resume app: {resume_response.status_code}")
                else:
                    send_message = "Koyeb app is healthy,no need to do anything."
                    # 状态正常，默认注释不发送消息，需要使用去掉注释即可
                   # send_telegram_message(tgbot_token, tgchat_id, send_message)
                return False
        else:
            print(f"App named {app_name} not found.")
            return False
    else:
        print(f"Failed to fetch apps: {response.status_code}")
        return False

def main():
    app_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    # 检查应用状态,也可用于大多数访问保活
    if not check_app_status(app_url, app_headers):
        print("Koyeb app 状态异常,正在恢复")
        resume_app(api_key, app_name)
    else:
        print("Koyeb app 状态正常,无需操作")

if __name__ == "__main__":
    main()