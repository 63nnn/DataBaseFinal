import re
import interface
import pymysql
import os
import json
import datetime
# from decimal import Decimal


os.chdir("C:\\Serious\\Program\\Github\\DataBaseFinal")
with open("setting.json", 'r', encoding="utf8") as jfile:
    jj = json.load(jfile)

db = pymysql.connect(host=jj["host"], 
                port=jj["port"], 
                user=jj["user"], 
                password=jj["password"],
                database="flower_shop")

# 

try:
        customer = ["客戶姓名","身分證字號/統一編號","生日","電話","Email","年齡","照片","會員折扣","地址"]
        customersql = ["cname","cnumber","birthday","phone","Email","age","photo","VIPdiscount","address"]

        sqlcmd = "SELECT * FROM `customer`;"
        with db.cursor() as cur:
            try:
                cur.execute(sqlcmd)
                records = cur.fetchall()
                records = list(records)
                temp = []
                for i in records:
                    temp.append(list(i))
                alen = 0
                aacum = 0
                for i in temp:
                    aacum += eval(str(i[5]))
                    alen += 1
                print(f"客戶頻均年齡: {aacum / alen}")
                input("Success. (Press Enter to continue)")
            except Exception as e:
                print(f"Encounter exception: {e}")
                input("Please try again. (Press Enter to continue)")
except Exception as e:
        print(f"Encounter exception: {e}")
        input("Please try again. (Press Enter to continue)")