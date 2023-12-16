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
    # str1 = input("請依照格式並用斜線分開(有空格請留空)\n\n客戶姓名/ 身分證字號/統一編號/ 生日(YYYY-DD-MM) /電話/ Email/ 照片/ 會員折扣/ 地址\n").split("/")
    str1 = '''李四/B154876236/1999-1-12/04-4854-2154/021@gmail.com/photo/0.82/台中市台灣大道四段兩百五十號'''.split("/")
    thisYear = datetime.datetime.now().year
    cbirth = (str1[2].split("-"))[0]
    str1.insert(5, (thisYear - eval(cbirth)))
    sqlcmd = ""
    if len(str1) == 9:
        sqlcmd = f'''INSERT INTO `customer` VALUES("{str1[0]}","{str1[1]}","{str1[2]}","{str1[3]}","{str1[4]}","{str1[5]}",{str1[6]},"{str1[7]}","{str1[8]}");'''
    with db.cursor() as cur:
        try:
            cur.execute(sqlcmd)
            db.commit()
            # input("Success. (Press Enter to continue)")
        except Exception as e:
            db.rollback()
            print(f"Encounter exception: {e}")
            input("Please try again. (Press Enter to continue)")        
except Exception as e:
        print(f"Encounter exception: {e}")
        input("Please try again. (Press Enter to continue)")

