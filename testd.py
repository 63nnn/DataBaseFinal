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
        str1 = input("請依照格式並用斜線分開(不得留空)\n\n客戶身分證字號/統一編號/ 花草苗木編號:\n").split("/")
        sqlcmd = ""
        if (str1[0] != "") and (str1[1] != ""):
            sqlcmd = f'''SELECT * FROM `purchase` WHERE `cnumber` = "{str1[0]}" AND `fnumber` = "{str1[1]}";'''
        else:
            raise
        with db.cursor() as cur:
            try:
                cur.execute(sqlcmd)
                records = cur.fetchall()
                records = list(records)
                temp = []
                for i in records:
                    temp.append(list(i))

                sqlcmd = f'''UPDATE `purchase` SET `real_delivery` = "{str(datetime.date.today())}" WHERE `cnumber` = "{str1[0]}" AND `fnumber` = "{str1[1]}";'''
                cur.execute(sqlcmd)
                db.commit()
                interface.purchase_table(temp)

                input("Success. (Press Enter to continue)")
            except Exception as e:
                db.rollback()
                print(f"Encounter exception: {e}")
                input("Please try again. (Press Enter to continue)")        
except Exception as e:
        print(f"Encounter exception: {e}")
        input("Please try again. (Press Enter to continue)")
