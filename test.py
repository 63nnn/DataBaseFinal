import interface
from interface import clen
import pymysql
import os
import json
import datetime
import time
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
    # print("[1]:查詢某客戶對供應商之金額, ", end="")
    # print("[3]:查詢某客戶之購買總金額, ", end="")
    # print("[5]:排序各客戶購買總金額, ")
    # print("[2]:查詢各客戶對供應商之金額, ", end="")
    # print("[4]:查詢各客戶之購買總金額, ", end="")
    # print("[6]:查詢尚未出貨訂單, ")
# 
purchase = ["花草苗木名稱","客戶身分證字號/統一編號","花草苗木編號","供應商名稱","購買數量","售價","總金額","折扣後金額","訂購日期","預計交貨日期","實際交貨日期"]


def read():
    interface.purchase_read_func()
    choice = input("請輸入數字選擇功能:")
    if choice == "1":
        os.system("cls")
        c1, c2 = input("請依照格式並用斜線分開(有空格請留空)\n\n 客戶身分證字號/統一編號/ 供應商名稱: \n")
        ctmToSupp(c1, c2)
    elif choice == "2":
        os.system("cls")
    elif choice == "3":
        os.system("cls")
    elif choice == "4":
        os.system("cls")
        c1, c2 = input("請依照格式並用斜線分開(有空格請留空)\n\n 客戶身分證字號/統一編號/ 供應商名稱: \n")
        ctmToSupp(c1, c2)
    elif choice == "5":
        os.system("cls")
    elif choice == "6":
        os.system("cls")
    elif choice == "q":
        return
    else:
        print("Please try again.")
        time.sleep(1.5)
    
    pass


### 要更變表格


def ctmToSupp(ctm=None, supp=None):
    try:
        str1 = [ctm, supp]
        flag = 0
        sqlcmd = ""
        if (str1[0] != None) and (str1[1] != None):
            sqlcmd = f'''SELECT * FROM `purchase` WHERE `cnumber` = "{str1[0]}" AND `sname` = "{str1[1]}";'''
            flag = 1
        elif (str1[0] != None):
            sqlcmd = f'''SELECT * FROM `purchase` WHERE `cnumber` = "{str1[0]}";'''
        elif (str1[1] != None):
            sqlcmd = f'''SELECT * FROM `purchase` WHERE `sname` = "{str1[1]}";'''
            flag = 1
        elif (str1[0] == None) and (str1[1] == None):
            sqlcmd = f'''SELECT * FROM `purchase`;'''

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



def totalSort():
    pass

def notYet():
    pass

read()