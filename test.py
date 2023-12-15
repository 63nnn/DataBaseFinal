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
                password=jj["password"],
                database="flower_shop")

with db.cursor() as cur:
    try:
        print("in")
        # cur.execute("SHOW DATABASES;")
        cur.execute("SELECT * FROM `flowers`;")
        records = cur.fetchall()
        records = list(records[0:2])
        for i in records:
            # print(list(i))
            list1 = list(i)
            # interface.flowers_table(list1)
            
             
        print()
        input("Success. (Press Enter to continue)")
    except:
        print(os.error)
        input("Please try again. (Press Enter to continue)")