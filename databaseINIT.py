import pymysql
import os
import json


os.chdir("C:\\Serious\\Program\\Github\\DataBaseFinal")
with open("setting.json", 'r', encoding="utf8") as jfile:
    jj = json.load(jfile)

db = pymysql.connect(host=jj["host"], 
                 port=jj["port"], 
                 user=jj["user"], 
                 password=jj["password"])

sqlcmd = "SHOW DATABASES;" # all init cmd

with db.cursor() as cur: # if 'flower_shop' exist then delet it to init
    try:
        cur.execute("SHOW DATABASES;")
        records = cur.fetchall()
        for i in records:
            if i[0] == 'flower_shop':
                cur.execute("DROP DATABASE `flower_shop`;")
                print("DROP DATABASE `flower_shop` success.")
                break
        print("NO database `flower_shop`.")
    except:
        print(os.error)
    


