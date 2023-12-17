import interface
import pymysql
import os
import json
import time
import datetime


os.chdir("C:\\Serious\\Program\\Github\\DataBaseFinal")
with open("setting.json", 'r', encoding="utf8") as jfile:
    jj = json.load(jfile)

    # print("[1]:新增資料")
    # print("[2]:刪除資料")
    # print("[3]:修改資料")
    # print("[4]:查詢資料")
    # print("[5]:列印資料")
    # print("[6]:統計客戶人數")
    # print("[7]:客戶平均年齡")

def mainFunc():
    while True:
        db = pymysql.connect(host=jj["host"], 
                port=jj["port"], 
                user=jj["user"], 
                password=jj["password"],
                database="flower_shop")
        os.system("cls")
        with db.cursor() as cur:
            try:
                cur.execute("SELECT * FROM `customer`;")
                records = cur.fetchall()
                records = list(records)
                if len(records) > 6:
                    records = records[0:6]
                temp = []
                for i in records:
                    temp.append(list(i))
                interface.customer_table(temp)
            except Exception as e:
                print(f"Encounter exception: {e}")
                input("Please try again. (Press Enter to continue)")
        interface.customer_func()
        choice = input("請輸入數字選擇功能:").strip()
        if choice == "1":
            os.system("cls")
            create(db)
        elif choice == "2":
            os.system("cls")
            delete(db)
        elif choice == "3":
            os.system("cls")
            update(db)
        elif choice == "4":
            os.system("cls")
            read(db)
        elif choice == "5":
            os.system("cls")
            readAll(db)
        elif choice == "6":
            os.system("cls")
            amountOfCustomer(db)
        elif choice == "7":
            os.system("cls")
            averageCustomersAge(db)
        elif choice == "q":
            return
        else:
            print("Please try again.")
            time.sleep(1.5)
        db.close()


def create(db):
    try:
        str1 = input("請依照格式並用斜線分開(有空格請留空)\n\n客戶姓名/ 身分證字號或統一編號/ 生日(YYYY-DD-MM) /電話/ Email/ 照片/ 會員折扣/ 地址\n").split("/")
        for i in range(len(str1)):
            str1[i] = str1[i].strip()
        thisYear = datetime.datetime.now().year
        cbirth = (str1[2].split("-"))[0]
        str1.insert(5, (thisYear - eval(cbirth)))
        sqlcmd = ""
        if len(str1) == 9:
            sqlcmd = f'''INSERT INTO `customer` VALUES("{str1[0]}","{str1[1]}","{str1[2]}","{str1[3]}","{str1[4]}","{str1[5]}",NULL,"{str1[7]}","{str1[8]}");'''
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

def delete(db):
    try:
        str1 = input("請依照格式並用斜線分開(有空格請留空)\n\n客戶姓名/ 身分證字號或統一編號:\n").split("/")
        for i in range(len(str1)):
            str1[i] = str1[i].strip()
        sqlcmd = ""
        if (str1[0] != "") and (str1[1] != ""):
            sqlcmd = f'''SELECT * FROM `customer` WHERE `cname` = "{str1[0]}" AND `cnumber` = "{str1[1]}";'''
        elif (str1[0] != ""):
            sqlcmd = f'''SELECT * FROM `customer` WHERE `cname` = "{str1[0]}";'''
        elif (str1[1] != ""):
            sqlcmd = f'''SELECT * FROM `customer` WHERE `cnumber` = "{str1[1]}";'''

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
                    choice= input("確定刪除第一筆資料嗎? (Y / N): ")
                    if choice.lower() == "y":
                        sqlcmd = f'''INSERT INTO `stable_customer` VALUES("{result[0]}","{result[1]}","{result[2]}","{result[3]}","{result[4]}",{eval(result[5])},NULL,"{result[7]}","{result[8]}");'''
                        with db.cursor() as cur:
                            try:
                                cur.execute(sqlcmd)
                                db.commit()
                                sqlcmd = f'''DELETE FROM `customer` WHERE `cname` = "{str1[0]}" OR `cnumber` = "{str1[1]}";'''
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

def update(db):
    try:
        str1 = input("請依照格式並用斜線分開(有空格請留空)\n\n客戶姓名/ 身分證字號或統一編號:\n").split("/")
        for i in range(len(str1)):
            str1[i] = str1[i].strip()
        sqlcmd = ""
        if (str1[0] != "") and (str1[1] != ""):
            sqlcmd = f'''SELECT * FROM `customer` WHERE `cname` = "{str1[0]}" AND `cnumber` = "{str1[1]}";'''
        elif (str1[0] != ""):
            sqlcmd = f'''SELECT * FROM `customer` WHERE `cname` = "{str1[0]}";'''
        elif (str1[1] != ""):
            sqlcmd = f'''SELECT * FROM `customer` WHERE `cnumber` = "{str1[1]}";'''

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
                    interface.customer_table(result)
                    result = result[0]
                    choice= input("修改第一筆哪個欄位的資料?\n")
                    customer = ["客戶姓名","身分證字號或統一編號","生日","電話","Email","年齡","照片","會員折扣","地址"]
                    customersql = ["cname","cnumber","birthday","phone","Email","age","photo","VIPdiscount","address"]

                    for i in range(len(customer)):
                        if choice == customer[i]:
                            temp = input("更改為: ")
                            sqlcmd = f'''UPDATE `customer` SET `{customersql[i]}` = "{temp}" WHERE `{customersql[1]}` = "{result[1]}";'''
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

def read(db):
    try:
        str1 = input("請依照格式並用斜線分開(有空格請留空)\n\n客戶姓名/ 身分證字號或統一編號:\n").split("/")
        for i in range(len(str1)):
            str1[i] = str1[i].strip()
        sqlcmd = ""
        if (str1[0] != "") and (str1[1] != ""):
            sqlcmd = f'''SELECT * FROM `customer` WHERE `cname` = "{str1[0]}" AND `cnumber` = "{str1[1]}";'''
        elif (str1[0] != ""):
            sqlcmd = f'''SELECT * FROM `customer` WHERE `cname` = "{str1[0]}";'''
        elif (str1[1] != ""):
            sqlcmd = f'''SELECT * FROM `customer` WHERE `cnumber` = "{str1[1]}";'''

        with db.cursor() as cur:
            try:
                cur.execute(sqlcmd)
                records = cur.fetchall()
                records = list(records)
                temp = []
                
                for i in records:                   #蒐集
                    temp.append(list(i))
                interface.customer_table(temp)

                input("Success. (Press Enter to continue)")
            except Exception as e:
                db.rollback()
                print(f"Encounter exception: {e}")
                input("Please try again. (Press Enter to continue)")
    except Exception as e:
        print(f"Encounter exception: {e}")
        input("Please try again. (Press Enter to continue)")

def readAll(db):
    try:
        sqlcmd = '''SELECT * FROM `customer`;'''

        with db.cursor() as cur:
            try:
                cur.execute(sqlcmd)
                records = cur.fetchall()
                records = list(records)
                temp = []
                for i in records:
                    temp.append(list(i))
                interface.customer_table(temp)

                input("Success. (Press Enter to continue)")
            except Exception as e:
                db.rollback()
                print(f"Encounter exception: {e}")
                input("Please try again. (Press Enter to continue)")        
    except Exception as e:
        print(f"Encounter exception: {e}")
        input("Please try again. (Press Enter to continue)")

def amountOfCustomer(db):
    try:
        sqlcmd = "SELECT * FROM `customer`;"
        with db.cursor() as cur:
            try:
                cur.execute(sqlcmd)
                records = cur.fetchall()
                records = list(records)
                temp = []
                for i in records:
                    temp.append(list(i))
                amount = len(temp)
                print(f"客戶數量: {amount}(人/公司)")
                input("Success. (Press Enter to continue)")        
            except Exception as e:
                print(f"Encounter exception: {e}")
                input("Please try again. (Press Enter to continue)")
    except Exception as e:
            print(f"Encounter exception: {e}")
            input("Please try again. (Press Enter to continue)")

def averageCustomersAge(db):
    try:
        customer = ["客戶姓名","身分證字號或統一編號","生日","電話","Email","年齡","照片","會員折扣","地址"]
        customersql = ["cname","cnumber","birthday","phone","Email","age","photo","VIPdiscount","address"]

        sqlcmd = "SELECT * FROM `customer`;"
        with db.cursor() as cur:
            try:
                cur.execute(sqlcmd)
                records = cur.fetchall()
                records = list(records)
                temp = []
                for i in records:
                    temp.append(list(i))
                alen = 0
                aacum = 0
                for i in temp:
                    aacum += eval(str(i[5]))
                    alen += 1
                print(f"客戶平均年齡: {round(aacum / alen)}")
                input("Success. (Press Enter to continue)")
            except Exception as e:
                print(f"Encounter exception: {e}")
                input("Please try again. (Press Enter to continue)")
    except Exception as e:
            print(f"Encounter exception: {e}")
            input("Please try again. (Press Enter to continue)")

if __name__ == "__main__":
    pass

