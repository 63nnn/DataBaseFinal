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


# str1 = input("請依照格式並用斜線分開\n花草苗木編號/ 花草苗木名稱/ 供應商名稱/ 公司內現有數量/ 單位/ 單價/ 公司內存放位置/ 進貨日期(YYYY-MM-DD): \n").split("/")
str1 = "09-876-0543-2/玫瑰花/南海苗圃/50/束/6.00/300.00/二樓花房/2018-11-20".split("/")
print(str1)
sqlcmd = ""
with db.cursor() as cur:
    try:
        cur.execute(sqlcmd)
        records = cur.fetchall()
        print(type(records), "records")
        for i in records:
            print(i)
        
        print()
        # input("Success. (Press Enter to continue)")
    except:
        print(os.error)
        input("Please try again. (Press Enter to continue)")

# from decimal import Decimal

# i = [Decimal("6.00")]
# print(type(i[0]))