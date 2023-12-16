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
supplier = ["供應商名稱","供應商統一編號","電話","Email","負責人姓名","地址"]



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
                elif choice == "2":
                    srh = input("輸入負責人姓名: ")
                    srhlist = []
                    for i in temp:
                        if i[4] == srh:
                            srhlist.append(i)
                    interface.supplier_table(srhlist)
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
                else:
                    print("Please try again.")
                    time.sleep(1.5)


            except Exception as e:
                print(f"Encounter exception: {e}")
                input("Please try again. (Press Enter to continue)")
except Exception as e:
            print(f"Encounter exception: {e}")
            input("Please try again. (Press Enter to continue)")

