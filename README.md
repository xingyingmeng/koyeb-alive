# koyeb-alive
主要用于koyeb搭建哪吒探针的保活，也可以保活koyeb的其他项目

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
