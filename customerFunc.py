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
                password=jj["password"])

    # print("[1]:新增資料")
    # print("[2]:刪除資料")
    # print("[3]:修改資料")
    # print("[4]:查詢資料")
    # print("[5]:列印資料")
    # print("[q]:回到上一頁")

def mainFunc():
    interface.customer_func()
    choice = input("請輸入數字選擇功能:")
    if choice == "1":
        pass
    elif choice == "2":
        pass
    elif choice == "3":
        pass
    elif choice == "4":
        pass
    elif choice == "5":
        pass
    elif choice == "6":
        pass
    else:
        print("Please try again.")