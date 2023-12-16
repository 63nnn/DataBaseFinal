import interface
import pymysql
import os
import json
import time
from interface import clen


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
    # print("[4]:修改資料")
    # print("[5]:查詢供應商數量")
    # print("[6]:查詢相同負責人")
    # print("[q]:回到上一頁")

def mainFunc():
    while True:
        os.system("cls")
        with db.cursor() as cur:
            try:
                cur.execute("SELECT * FROM `supplier`;")
                records = cur.fetchall()
                records = list(records)
                if len(records) > 6:
                    records = records[0:6]
                temp = []
                for i in records:
                    temp.append(list(i))
                interface.supplier_table(temp)
            except Exception as e:
                print(f"Encounter exception: {e}")
                input("Please try again. (Press Enter to continue)")
        interface.supplier_func()
        choice = input("請輸入數字選擇功能:")
        if choice == "1":
            os.system("cls")
            create()
        elif choice == "2":
            os.system("cls")
            read()
        elif choice == "3":
            os.system("cls")
            readAll()
        elif choice == "4":
            os.system("cls")
            update()
        elif choice == "5":
            os.system("cls")
            amountOfSupplier()
        elif choice == "6":
            os.system("cls")
            sameInCharge()
        elif choice == "q":
            return
        else:
            print("Please try again.")
            time.sleep(1.5)

def create():
    try:
        str1 = input("請依照格式並用斜線分開(有空格請留空)\n\n供應商名稱/供應商統一編號/ 電話/ Email/ 負責人姓名/ 地址: \n").split("/")
        sqlcmd = ""
        if len(str1) == 6:
            sqlcmd = f'''INSERT INTO `supplier` VALUES("{str1[0]}","{str1[1]}","{str1[2]}","{str1[3]}","{str1[4]}","{str1[5]}");'''
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
            print(f"Encounter exception: {e}")
            input("Please try again. (Press Enter to continue)")

def read():
    try:
        str1 = input("請依照格式並用斜線分開(有空格請留空)\n\n供應商名稱/ 供應商統一編號:\n").split("/")
        sqlcmd = ""
        if (str1[0] != "") and (str1[1] != ""):
            sqlcmd = f'''SELECT * FROM `supplier` WHERE `sname` = "{str1[0]}" AND `snumber` = "{str1[1]}";'''
        elif (str1[0] != ""):
            sqlcmd = f'''SELECT * FROM `supplier` WHERE `sname` = "{str1[0]}";'''
        elif (str1[1] != ""):
            sqlcmd = f'''SELECT * FROM `supplier` WHERE `snumber` = "{str1[1]}";'''
        with db.cursor() as cur:
            try:
                cur.execute(sqlcmd)
                records = cur.fetchall()
                records = list(records)
                temp = []
                for i in records:
                    temp.append(list(i))
                interface.supplier_table(temp)

                input("Success. (Press Enter to continue)")
            except Exception as e:
                db.rollback()
                print(f"Encounter exception: {e}")
                input("Please try again. (Press Enter to continue)")        
    except Exception as e:
            print(f"Encounter exception: {e}")
            input("Please try again. (Press Enter to continue)")

def readAll():
    try:
        sqlcmd = '''SELECT * FROM `supplier`;'''

        with db.cursor() as cur:
            try:
                cur.execute(sqlcmd)
                records = cur.fetchall()
                records = list(records)
                temp = []
                for i in records:
                    temp.append(list(i))
                interface.supplier_table(temp)

                input("Success. (Press Enter to continue)")
            except Exception as e:
                db.rollback()
                print(f"Encounter exception: {e}")
                input("Please try again. (Press Enter to continue)")        
    except Exception as e:
        print(f"Encounter exception: {e}")
        input("Please try again. (Press Enter to continue)")

def update():
    try:
        str1 = input("請依照格式並用斜線分開(有空格請留空)\n\n供應商名稱/ 供應商統一編號:\n").split("/")
        sqlcmd = ""
        if (str1[0] != "") and (str1[1] != ""):
            sqlcmd = f'''SELECT * FROM `supplier` WHERE `sname` = "{str1[0]}" AND `snumber` = "{str1[1]}";'''
        elif (str1[0] != ""):
            sqlcmd = f'''SELECT * FROM `supplier` WHERE `sname` = "{str1[0]}";'''
        elif (str1[1] != ""):
            sqlcmd = f'''SELECT * FROM `supplier` WHERE `snumber` = "{str1[1]}";'''
        result = []
        with db.cursor() as cur:
            try:
                cur.execute(sqlcmd)
                records = cur.fetchall()
                records = list(records)
                temp = []
                for i in records:                   #蒐集
                    temp.append(list(i))
                result = []
                for i in temp:                      #查找
                    if i[0] == str1[0] or i[1] == str1[1]:
                        result.append(i)
            except Exception as e:
                db.rollback()
                print(f"Encounter exception: {e}")
                input("Please try again. (Press Enter to continue)")       
            try:
                if result != []:
                    interface.supplier_table(result)
                    result = result[0]
                    print(result)
                    choice= input("修改第一筆哪個欄位的資料?\n")
                    supplier = ["供應商名稱","供應商統一編號","電話","Email","負責人姓名","地址"]
                    suppliersql = ["sname","snumber","phone","Email","in_charge","address"]
                    for i in range(len(supplier)):
                        if choice == supplier[i]:
                            temp = input("更改為: ")
                            sqlcmd = f'''UPDATE `supplier` SET `{suppliersql[i]}` = "{temp}" WHERE `{suppliersql[1]}` = "{result[1]}";'''
                            with db.cursor() as cur:
                                try:
                                    cur.execute(sqlcmd)
                                    db.commit()
                                    input("Success. (Press Enter to continue)")
                                    break
                                except Exception as e:
                                    db.rollback()
                                    print(f"Encounter exception: {e}")
                                    input("Please try again. (Press Enter to continue)")
                    else:
                        input("Please try again. (Press Enter to continue)")
                else:
                    print("not found")
                    input("Please try again. (Press Enter to continue)")
            except Exception as e:
                print(f"Encounter exception: {e}")
                input("Please try again. (Press Enter to continue)")
    except Exception as e:
        print(f"Encounter exception: {e}")
        input("Please try again. (Press Enter to continue)")

def amountOfSupplier():
    try:
        sqlcmd = "SELECT * FROM `supplier`;"
        with db.cursor() as cur:
            try:
                cur.execute(sqlcmd)
                records = cur.fetchall()
                records = list(records)
                temp = []
                for i in records:
                    temp.append(list(i))
                amount = len(temp)
                print(f"供應商數量: {amount}")
                input("Success. (Press Enter to continue)")        
            except Exception as e:
                print(f"Encounter exception: {e}")
                input("Please try again. (Press Enter to continue)")
    except Exception as e:
                print(f"Encounter exception: {e}")
                input("Please try again. (Press Enter to continue)")

def sameInCharge():
    try:
        sqlcmd = "SELECT * FROM `supplier`;"
        with db.cursor() as cur:
            try:
                cur.execute(sqlcmd)
                records = cur.fetchall()
                records = list(records)
                temp = []
                for i in records:
                    temp.append(list(i))
                
                choice = input("[1]:用Email查詢, [2]:用負責人名查詢, [3]:查詢有重複項目: ")
                if choice == "1":
                    srh = input("輸入Email: ")
                    srhlist = []
                    for i in temp:
                        if i[3] == srh:
                            srhlist.append(i)
                    interface.supplier_table(srhlist)
                    input("Success. (Press Enter to continue)")
                elif choice == "2":
                    srh = input("輸入負責人姓名: ")
                    srhlist = []
                    for i in temp:
                        if i[4] == srh:
                            srhlist.append(i)
                    interface.supplier_table(srhlist)
                    input("Success. (Press Enter to continue)")
                elif choice == "3":
                    # Email.count
                    listEmail = []
                    for i in temp:
                        if i[3] != "":
                            listEmail.append(i[3])
                    setEmail = set(listEmail)
                    dictEmail = {}
                    for i in setEmail:
                        dictEmail[i] = listEmail.count(i)
                    print("<<Email>>")
                    title = ["Email", "供應商數量"]
                    print(f"{title[0]:<{clen(title[0], 20)}}|{title[1]:>{clen(title[1], 12)}}")
                    for i, j in dictEmail.items():
                        print(f"{i:<{clen(i, 20)}}|{j:>{clen(j, 12)}}")
                    print()
                    #InCharge.count
                    listInCharge = []
                    for i in temp:
                        if i[4] != "":
                            listInCharge.append(i[4])
                    setInCharge = set(listInCharge)
                    dictInCharge = {}
                    for i in setInCharge:
                        dictInCharge[i] = listInCharge.count(i)
                    print("<<負責人>>")
                    title = ["姓名", "供應商數量"]
                    print(f"{title[0]:<{clen(title[0], 10)}}|{title[1]:>{clen(title[1], 12)}}")
                    for i, j in dictInCharge.items():
                        print(f"{i:<{clen(i, 10)}}|{j:>{clen(j, 12)}}")
                    input("Success. (Press Enter to continue)")
                else:
                    print("Please try again.")
                    time.sleep(1.5)
            except Exception as e:
                print(f"Encounter exception: {e}")
                input("Please try again. (Press Enter to continue)")
    except Exception as e:
            print(f"Encounter exception: {e}")
            input("Please try again. (Press Enter to continue)")

