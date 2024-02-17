# koyeb-alive
koyeb在搭建完探针以后长时间不登陆会自动暂停，没法舒服吃灰(~~白嫖~~ ,本脚本用于检查koyeb app状态是否正常，如果不正常则尝试恢复并在成功后发送tg消息到指定用户

## koyeb api key申请
1. 右上角点击account setting <br>
![图1](https://raw.githubusercontent.com/zhuifan1/koyeb-alive/main/pic/1.png)

2. 选择第三个 <br>
![图1](https://raw.githubusercontent.com/zhuifan1/koyeb-alive/main/pic/2.png)

3. 得到key <br>
![图1](https://raw.githubusercontent.com/zhuifan1/koyeb-alive/main/pic/3.png)

## 相关变量
  | 变量名        | 是否必须  | 备注 |
  | ------------ | ------   | ---- |
  | app_name             | 是 | koyeb的app名 |
  | api_key         | 是 | koyeb的api key |
  | tgbot_token           | 否 | tg bot token |
  | tgchat_id              | 否 | tg id |

## 如何使用
填好变量，确保有python环境，安装requests库
```bash
apt install python3 python3-pip
pip3 install requests
```
设置cron定期执行即可
```
crontab -e
```
每天晚上6点执行
```
0 18 * * * /usr/bin/python3 ~/koyeb.py
```
