import re
import interface
import pymysql
import os
import json
import datetime
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

try:
        str1 = input("請依照格式並用斜線分開(有空格請留空)\n\n客戶姓名/ 身分證字號/統一編號:\n").split("/")
        sqlcmd = ""
        if (str1[0] != "") and (str1[1] != ""):
            sqlcmd = f'''SELECT * FROM `stable_customer` WHERE `cname` = "{str1[0]}" AND `cnumber` = "{str1[1]}";'''
        elif (str1[0] != ""):
            sqlcmd = f'''SELECT * FROM `stable_customer` WHERE `cname` = "{str1[0]}";'''
        elif (str1[1] != ""):
            sqlcmd = f'''SELECT * FROM `stable_customer` WHERE `cnumber` = "{str1[1]}";'''

        result = []
        with db.cursor() as cur:
            try:
                cur.execute(sqlcmd)
                records = cur.fetchall()
                records = list(records)
                temp = []
                for i in records:
                    temp.append(list(i))
                result = []
                for i in temp:
                    if i[0] == str1[0] or i[1] == str1[1]:
                        result.append(i)
            except Exception as e:
                db.rollback()
                print(f"Encounter exception: {e}")
                input("Please try again. (Press Enter to continue)")       
            try:
                if result != []:
                    interface.customer_table(result)
                    result = result[0]
                    choice= input("確定轉移第一筆資料嗎? (Y / N): ")
                    if choice.lower() == "y":
                        sqlcmd = f'''INSERT INTO `customer` VALUES("{result[0]}","{result[1]}","{result[2]}","{result[3]}","{result[4]}",{eval(result[5])},"{result[6]}","{result[7]}","{result[8]}");'''
                        with db.cursor() as cur:
                            try:
                                cur.execute(sqlcmd)
                                db.commit()
                                sqlcmd = f'''DELETE FROM `stable_customer` WHERE `cname` = "{str1[0]}" OR `cnumber` = "{str1[1]}";'''
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
                else:
                    print("not found")
                    input("Please try again. (Press Enter to continue)")
            except Exception as e:
                print(f"Encounter exception: {e}")
                input("Please try again. (Press Enter to continue)")
except Exception as e:
        print(f"Encounter exception: {e}")
        input("Please try again. (Press Enter to continue)")