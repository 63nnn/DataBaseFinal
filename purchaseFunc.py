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
    # print("[2]:查詢資料")
    # print("[3]:列印資料")
    # print("[4]:交貨完成登記")

    # print("[1]:查詢某客戶對供應商之金額, ", end="")
    # print("[3]:查詢某客戶之購買總金額, ", end="")
    # print("[5]:排序各客戶購買總金額, ")
    # print("[2]:查詢各客戶對供應商之金額, ", end="")
    # print("[4]:查詢各客戶之購買總金額, ", end="")
    # print("[6]:查詢尚未出貨訂單, ")

def mainFunc():
    while True:
        os.system("cls")
        with db.cursor() as cur:
            try:
                cur.execute("SELECT * FROM `purchase`;")
                records = cur.fetchall()
                records = list(records)
                if len(records) > 6:
                    records = records[0:6]
                temp = []
                for i in records:
                    temp.append(list(i))
                interface.purchase_table(temp)
            except Exception as e:
                print(f"Encounter exception: {e}")
                input("Please try again. (Press Enter to continue)")
        interface.purchase_func()
        choice = input("請輸入數字選擇功能:")
        if choice == "1":
            os.system("cls")
            create()
        elif choice == "2":
            os.system("cls")
            interface.purchase_read_func()
        elif choice == "3":
            os.system("cls")
            readAll()
        elif choice == "4":
            os.system("cls")
        elif choice == "q":
            return
        else:
            print("Please try again.")
            time.sleep(1.5)

def create():
    pass

def readAll():
    pass

def delivered():
    pass

def ctmToSupp():
    pass

def totalSort():
    pass

def notYet():
    pass