import interface
import pymysql
import os
import json
import time


os.chdir("C:\\Serious\\Program\\Github\\DataBaseFinal")
with open("setting.json", 'r', encoding="utf8") as jfile:
    jj = json.load(jfile)

db = pymysql.connect(host=jj["host"], 
                port=jj["port"], 
                user=jj["user"], 
                password=jj["password"],
                database="flower_shop")

    # print("[1]:新增資料")
    # print("[2]:刪除資料")
    # print("[3]:修改資料")
    # print("[4]:查詢資料")
    # print("[5]:列印資料")
    # print("[6]:統計客戶人數")
    # print("[7]:客戶平均年齡")


def mainFunc():
    while True:
        os.system("cls")
        with db.cursor() as cur:
            try:
                cur.execute("SELECT * FROM `customer`;")
                records = cur.fetchall()
                records = list(records)
                if len(records) > 6:
                    records = records[0:6]
                temp = []
                for i in records:
                    temp.append(list(i))
                interface.customer_table(temp)
            except Exception as e:
                print(f"Encounter exception: {e}")
                input("Please try again. (Press Enter to continue)")
        interface.customer_func()
        choice = input("請輸入數字選擇功能:")
        if choice == "1":
            os.system("cls")
            create()
        elif choice == "2":
            os.system("cls")
            pass
        elif choice == "3":
            os.system("cls")
            pass
        elif choice == "4":
            os.system("cls")
            pass
        elif choice == "5":
            os.system("cls")
            pass
        elif choice == "ˊ":
            os.system("cls")
            pass
        elif choice == "7":
            os.system("cls")
            pass
        elif choice == "q":
            return
        else:
            print("Please try again.")
            time.sleep(1.5)


def create():
    try:
        str1 = input("請依照格式並用斜線分開(有空格請留空)\n\n客戶姓名/ 身分證字號/統一編號/ 生日(YYYY-DD-MM) /電話/ Email/ 年齡/ 照片/ 會員折扣/ 地址\n").split("/")

            
    except Exception as e:
        print(f"Encounter exception: {e}")
        input("Please try again. (Press Enter to continue)")   
