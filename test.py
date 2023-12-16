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
# 
purchase = ["花草苗木名稱","客戶身分證字號/統一編號","花草苗木編號","供應商名稱","購買數量","售價","總金額","折扣後金額","訂購日期","預計交貨日期","實際交貨日期"]
 
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
                print("ss")
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
                print(temp)
                ttotal = str1[6] * temp[0][7]
                print(temp)
                str1.insert(7, ttotal)
                print("s2")
            except Exception as e:
                db.rollback()
                print(f"Encounter exception: {e}")
                input("Please try again. (Press Enter to continue)")
        

        print(str1)
        if len(str1) == 11:
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
        print(f"Encounter exception: {e}")
        input("Please try again. (Press Enter to continue)")
