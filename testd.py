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

x1, x2 = input("q").split("/")

def ccc(c1=None, c2=None):
    print(f'''"{c1}, "{c2}"''')
ccc()