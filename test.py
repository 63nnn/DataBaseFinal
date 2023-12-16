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
        # str1 = input("請依照格式並用斜線分開(有空格請留空)\n\n客戶姓名/ 身分證字號/統一編號/ 生日(YYYY-DD-MM) /電話/ Email/ 照片/ 會員折扣/ 地址\n").split("/")

        sqlcmd = '''SELECT * FROM `customer`;'''
        with db.cursor() as cur:
            try:
                cur.execute(sqlcmd)
                records = cur.fetchall()
                records = list(records)
                temp = []
                for i in records:
                    temp.append(list(i))
                print(temp)
                interface.customer_table(temp)

                input("Success. (Press Enter to continue)")
            except Exception as e:
                db.rollback()
                print(f"Encounter exception: {e}")
                input("Please try again. (Press Enter to continue)")        
except Exception as e:
        print(f"Encounter exception: {e}")
        input("Please try again. (Press Enter to continue)")   