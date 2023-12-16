import interface
import pymysql
import os
import json


os.chdir("C:\\Serious\\Program\\Github\\DataBaseFinal")
with open("setting.json", 'r', encoding="utf8") as jfile:
    jj = json.load(jfile)

db = pymysql.connect(host=jj["host"], 
             port=jj["port"], 
             user=jj["user"], 
             password=jj["password"],
             database="flower_shop")

    # print("[1]:新增資料")
    # print("[2]:查詢資料")
    # print("[3]:列印資料")
    # print("[q]:回到上一頁")

import time

def mainFunc():
    while True:
        os.system("cls")
        with db.cursor() as cur:
            try:
                cur.execute("SELECT * FROM `flowers`;")
                records = cur.fetchall()
                records = list(records)
                if len(records) > 6:
                    records = records[0:6]
                temp = []
                for i in records:
                    temp.append(list(i))
                interface.flowers_table(temp)
            except Exception as e:
                print(f"Encounter exception: {e}")
                input("Please try again. (Press Enter to continue)")
        interface.flowers_func()
        choice = input("請輸入數字選擇功能:")
        if choice == "1":
            os.system("cls")
            create()
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "q":
            return
        else:
            print("Please try again.")
            time.sleep(1.5)

# 39-896-0543-2/測試花/南海苗圃/50/束/6.00/二樓花房/2018-11-20
# 39-896-2243-2//南海苗圃/50/束/6.00/二樓花房/2018-11-20
# 49-896-0543-2/測試花/南海苗圃/50/束/6.00/二樓花房/2018-11-20
# 50-896-0543-2/測試花/南海苗圃/50/束/6.00/二樓花房/2018-11-20
# 00-896-0543-2/測試花/南海苗圃/50/束/6.00/二樓花房/2018-11-20

def create():
    try:
        str1 = input("請依照格式並用斜線分開\n\n花草苗木編號/ 花草苗木名稱/ 供應商名稱/ 公司內現有數量/ 單位/ 單價/ 公司內存放位置/ 進貨日期(YYYY-MM-DD): \n").split("/")
        str1.insert(6, eval(str1[3])*eval(str1[5]) )
        sqlcmd = ""
        if len(str1) == 9:
            sqlcmd = f'''INSERT INTO `flowers` VALUES("{str1[0]}","{str1[1]}","{str1[2]}",{str1[3]},"{str1[4]}",{str1[5]},{str1[6]},"{str1[7]}","{str1[8]}");'''
        with db.cursor() as cur:
            try:
                cur.execute(sqlcmd)
                db.commit()
                input("Success. (Press Enter to continue)")
            except Exception as e:
                db.rollback()
                print(f"Encounter exception: {e}")
                input("Please try again. (Press Enter to continue)")        
    except Exception as e:
        db.rollback()
        print(f"Encounter exception: {e}")
        input("Please try again. (Press Enter to continue)")   

def read():
    pass

