# koyeb-alive
koyeb在搭建完探针以后长时间不登陆会强制暂停，没法舒服吃灰 (~~白嫖~~  <br>
脚本可以检查koyeb app状态是否正常，如果不正常则尝试恢复并在成功后发送tg消息到指定用户

## koyeb api key申请
1. 右上角点击account setting <br>
![图1](https://raw.githubusercontent.com/zhuifan1/koyeb-alive/main/pic/1.png)

2. 选择第三个 <br>
![图2](https://raw.githubusercontent.com/zhuifan1/koyeb-alive/main/pic/2.png)

3. 得到key <br>
![图3](https://raw.githubusercontent.com/zhuifan1/koyeb-alive/main/pic/3.png)

## 相关变量
  | 变量名        | 是否必须  | 备注 |
  | ------------ | ------   | ---- |
  | app_url             | 是 | koyeb的app的域名或argo域名 |
  | app_name             | 是 | koyeb的app名 |
  | api_key         | 是 | koyeb的api key |
  | tgbot_token           | 否 | tg bot token |
  | tgchat_id              | 否 | tg id |

## 如何使用
仅需下载main.py并填好变量，确保有python环境，安装requests库
```bash
apt install python3 python3-pip
pip3 install requests
```
设置cron定期执行
```
crontab -e
```
不需要url保活, 每天执行一次
```
0 18 * * * /usr/bin/python3 ~/main.py
```
需要url保活, 每两分钟执行一次
```
*/2 * * * * /usr/bin/python3 ~/main.py
```
