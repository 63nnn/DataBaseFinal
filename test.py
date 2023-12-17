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


def read(db):
    interface.purchase_read_func()
    # choice = input("請輸入數字選擇功能:")
    
    choice = "2"

    if choice == "1": #客戶 廠商
        os.system("cls")
        str1 = input("請依照格式並用斜線分開(有空格請留空)\n\n客戶身分證字號或統一編號/ 供應商名稱: \n").split("/")
        for i in range(len(str1)):
            str1[i] = str1[i].strip()
        ctmToSupp(db, str1[0], str1[1])
    elif choice == "2": #廠商
        os.system("cls")
        str1 = input("請依照格式並用斜線分開(有空格請留空)\n\n客戶身分證字號或統一編號/ 供應商名稱: \n").split("/")
        for i in range(len(str1)):
            str1[i] = str1[i].strip()
        print("33")
        ctmToSupp(db, str1[0], str1[1])
    elif choice == "3": #客戶
        os.system("cls")
        str1 = input("請依照格式並用斜線分開(有空格請留空)\n\n客戶身分證字號或統一編號/ 供應商名稱: \n").split("/")
        for i in range(len(str1)):
            str1[i] = str1[i].strip()
        ctmToSupp(db, str1[0], str1[1])
    elif choice == "4": #全部
        os.system("cls")
        str1 = input("請依照格式並用斜線分開(有空格請留空)\n\n客戶身分證字號或統一編號/ 供應商名稱: \n").split("/")
        for i in range(len(str1)):
            str1[i] = str1[i].strip()
        ctmToSupp(db, str1[0], str1[1])
    elif choice == "q":
        return
    else:
        print("Please try again.")
        time.sleep(1.5)
    
def ctmToSupp(db, ctm=None, supp=None):
    try:
        str1 = [ctm, supp]
        flag = 0 #有廠商
        sqlcmd = ""
        if (str1[0] != "") and (str1[1] != ""):
            sqlcmd = f'''SELECT * FROM `purchase` WHERE `cnumber` = "{str1[0]}" AND `sname` = "{str1[1]}";'''
            flag = 1
        elif (str1[0] != ""):
            sqlcmd = f'''SELECT * FROM `purchase` WHERE `cnumber` = "{str1[0]}";'''
        elif (str1[1] != ""):
            sqlcmd = f'''SELECT * FROM `purchase` WHERE `sname` = "{str1[1]}";'''
            flag = 1
        elif (str1[0] == "") and (str1[1] == ""):
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
                os.system("cls")

                dy = [] # 已交貨 2D
                dn = [] # 未交貨 2D
                tts =[]  # 總輸出 2D
                tt = [0] # 子輸出 1D
                if (str1[0] != "") and (str1[1] != ""): # 客戶廠商 交貨分開
                    for i in temp:
                        if i[10] == "None":
                            dn.append(list(i))
                        else:
                            dy.append(list(i))
                    for i in dn:
                        tt = [0,"未交貨"]
                        tt.insert(0, i[1])
                        tt.insert(1, i[3])
                        tt.insert(2, i[0])
                        tt[3] += i[7]
                        tts.append(tt)
                    total = 0
                    for i in tts:
                        total += eval(str(i[3]))
                    tts.append(["","","","",""])
                    tts.append(["","","",total,""])
                    interface.pur1_table(tts)

                    tts = []
                    for i in dy:
                        tt = [0,"已交貨"]
                        tt.insert(0, i[1])
                        tt.insert(1, i[3])
                        tt.insert(2, i[0])
                        tt[3] += eval(i[7])
                        tts.append(tt)
                    total = 0
                    for i in tts:
                        total += eval(str(i[3]))
                    tts.append(["","","","",""])
                    tts.append(["","","",total,""])
                    interface.pur1_table(tts)

                elif (str1[0] != ""): # 客戶
                    for i in temp:
                        tt = [0,"全部"]
                        tt.insert(0, i[1])
                        tt.insert(1, i[3])
                        tt.insert(2, i[0])
                        tt[3] += eval(i[7])
                        tts.append(tt)

                    total = 0
                    for i in tts:
                        total += eval(str(i[3]))
                    tts.append(["","","","",""])
                    tts.append(["","","",total,""])
                    interface.pur1_table(tts)

                elif (str1[1] != ""): # 廠商
                    for i in temp:
                        tt = [0,"全部"]
                        tt.insert(0, i[1])
                        tt.insert(1, i[3])
                        tt.insert(2, i[0])
                        tt[3] += eval(i[7])
                        tts.append(tt)

                    total = 0
                    for i in tts:
                        total += eval(str(i[3]))
                    tts.append(["","","","",""])
                    tts.append(["","","",total,""])
                    interface.pur1_table(tts)

                elif (str1[0] == "") and (str1[1] == ""): # 全部
                    for i in temp:
                        tt = [0,"全部"]
                        tt.insert(0, i[1])
                        tt.insert(1, i[3])
                        tt.insert(2, i[0])
                        tt[3] += eval(i[7])
                        tts.append(tt)

                    total = 0
                    for i in tts:
                        total += eval(str(i[3]))
                    tts.append(["","","","",""])
                    tts.append(["","","",total,""])
                    interface.pur1_table(tts)

                input("Success. (Press Enter to continue)")
            except Exception as e:
                db.rollback()
                print(f"Encounter exception: {e}")
                input("Please try again. (Press Enter to continue)")
                return     
    except Exception as e:
        print(f"Encounter exception: {e}")
        input("Please try again. (Press Enter to continue)")

read(db)

