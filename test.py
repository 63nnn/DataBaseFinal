import interface
import pymysql
import os
import json
# from decimal import Decimal


os.chdir("C:\\Serious\\Program\\Github\\DataBaseFinal")
with open("setting.json", 'r', encoding="utf8") as jfile:
    jj = json.load(jfile)

db = pymysql.connect(host=jj["host"], 
                port=jj["port"], 
                user=jj["user"], 
                password=jj["password"],
                database="flower_shop")

# 33-876-4443-2/玫瑰花/南海苗圃/50/束/6.00/二樓花房/2018-11-20

str1 = input("請依照格式並用斜線分開\n花草苗木編號/ 花草苗木名稱/ 供應商名稱/ 公司內現有數量/ 單位/ 單價/ 公司內存放位置/ 進貨日期(YYYY-MM-DD): \n").split("/")

# str1 = "33-876-0543-2/玫瑰花/南海苗圃/50/束/6.00/二樓花房/2018-11-20".split("/")

str1.insert(6, eval(str1[3])*eval(str1[5]) )
sqlcmd = ""
if len(str1) == 9:
    sqlcmd = f'''INSERT INTO `flowers` VALUES("{str1[0]}","{str1[1]}","{str1[2]}",{str1[3]},"{str1[4]}",{str1[5]},{str1[6]},"{str1[7]}","{str1[8]}");'''
else:
    print("wrong")

print(sqlcmd)
with db.cursor() as cur:
    try:
        cur.execute(sqlcmd)
        db.commit()
        input("Success. (Press Enter to continue)")
    except:
        db.rollback()
        print(os.error)
        input("Please try again. (Press Enter to continue)")
