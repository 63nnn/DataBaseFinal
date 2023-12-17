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
        
        sqlcmd = "SELECT * FROM `purchase`;"
        

        with db.cursor() as cur:
            try:
                cur.execute(sqlcmd)
                records = cur.fetchall()
                records = list(records)
                temp = []
                
                for i in records:                   #蒐集
                    temp.append(list(i))
                print(type(temp[6][10]))
                interface.purchase_table(temp)

                # temp =  sorted(temp, key=lambda x:eval(x[4]), reverse=False)
                # print()
                interface.purchase_table(temp)

                input("Success. (Press Enter to continue)")
            except Exception as e:
                db.rollback()
                print(f"Encounter exception: {e}")
                input("Please try again. (Press Enter to continue)")
except Exception as e:
        print(f"Encounter exception: {e}")
        input("Please try again. (Press Enter to continue)")