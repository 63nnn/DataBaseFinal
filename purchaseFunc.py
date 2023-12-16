import interface
import pymysql
import os
import json
import time
import datetime

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
            ctmToSupp()
        elif choice == "3":
            os.system("cls")
            readAll()
        elif choice == "4":
            os.system("cls")
            delivered()
        elif choice == "q":
            return
        else:
            print("Please try again.")
            time.sleep(1.5)

def create():
    try:
        # str1 = input("請依照格式並用斜線分開(有空格請留空)\n\n 客戶身分證字號/統一編號/ 花草苗木編號/ 購買數量/ 售價/ 訂購日期/ 預計交貨日期: \n").split("/")
        str1 = '''O223456789/08-878-0540-2/20/6.00/2018-11-20/2018-11-21'''.split("/")
        attemp = ""
        # 加入花草苗木名稱, 供應商名稱, 總金額, 實際交貨日期NULL
        sqlcmd = f'''SELECT * FROM `flowers` WHERE `fnumber` = "{str1[1]}";'''
        with db.cursor() as cur:
            try:
                cur.execute(sqlcmd)
                records = cur.fetchall()
                records = list(records)
                temp = []
                for i in records:
                    temp.append(list(i))
                if temp == []:
                    raise 
                str1.insert(0, temp[0][1])  #名稱
                str1.insert(3, temp[0][2])  #供應商
                ttotal = eval(str1[4]) * eval(str1[5])
                str1.insert(6, ttotal)      #總金額
                str1.insert(9, None)       #NULL
            except Exception as e:
                db.rollback()
                print(f"Encounter exception: {e}")
                input("Please try again. (Press Enter to continue)")
        # 折扣後總經額
        sqlcmd = f'''SELECT * FROM `customer` WHERE `cnumber` = "{str1[1]}";'''
        with db.cursor() as cur:
            try:
                cur.execute(sqlcmd)
                records = cur.fetchall()
                records = list(records)
                temp = []
                for i in records:
                    temp.append(list(i))
                if temp == []:
                    raise
                ttotal = round(str1[6] * eval(str(temp[0][7])), 1)
                str1.insert(7, ttotal)
            except Exception as e:
                db.rollback()
                print(f"Encounter exception: {e}")
                input("Please try again. (Press Enter to continue)")
        
        if len(str1) == 11:
            sqlcmd = f'''INSERT INTO `purchase` VALUES("{str1[0]}","{str1[1]}","{str1[2]}","{str1[3]}",{str1[4]},{str1[5]},{str1[6]},{str1[7]},"{str1[8]}","{str1[9]}",NULL);'''
        with db.cursor() as cur:
            try:
                cur.execute(sqlcmd)
                db.commit()

                print()
                input("Success. (Press Enter to continue)")
            except Exception as e:
                db.rollback()
                print(f"Encounter exception: {e}")
                input("Please try again. (Press Enter to continue)")        
    except Exception as e:
        print(f"Encounter exception: {e}")
        input("Please try again. (Press Enter to continue)")

    pass

def readAll():
    try:
        sqlcmd = '''SELECT * FROM `purchase`;'''

        with db.cursor() as cur:
            try:
                cur.execute(sqlcmd)
                records = cur.fetchall()
                records = list(records)
                temp = []
                for i in records:
                    temp.append(list(i))
                interface.purchase_table(temp)

                input("Success. (Press Enter to continue)")
            except Exception as e:
                db.rollback()
                print(f"Encounter exception: {e}")
                input("Please try again. (Press Enter to continue)")        
    except Exception as e:
        print(f"Encounter exception: {e}")
        input("Please try again. (Press Enter to continue)")
    pass

def delivered():
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

def ctmToSupp():
    pass

def totalSort():
    pass

def notYet():
    pass