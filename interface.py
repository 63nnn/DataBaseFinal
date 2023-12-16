import os
import time
# from decimal import Decimal
# from datetime import date

def login_menu():
    table_head(145)
    print("[1]:登入系統")
    print("[q]:關機")
    
def main_menu():
    table_head(145)
    print("[1]:花草苗木資料表")
    print("[2]:客戶資料表")
    print("[3]:靜止客戶資料表")
    print("[4]:供應商資料表")
    print("[5]:客戶購買資料表")
    print("[q]:登出系統")

def flowers_func():
    table_head(145)
    print("<<花草苗木資料表>>")
    print("[1]:新增資料")
    print("[2]:查詢資料")
    print("[3]:列印資料")
    print("[4]:查詢花草苗木總數量與小計")
    print("[5]:查詢所有購入之總經額")
    print("[q]:回到上一頁")

def customer_func():
    table_head(145)
    print("<<客戶資料表>>")
    print("[1]:新增資料")
    print("[2]:刪除資料")
    print("[3]:修改資料")
    print("[4]:查詢資料")
    print("[5]:列印資料")
    print("[6]:統計客戶人數")
    print("[7]:客戶平均年齡")
    print("[q]:回到上一頁")

def stable_customer_func():
    table_head(145)
    print("<<靜止客戶資料表>>")
    print("[1]:新增資料")
    print("[2]:修改資料")
    print("[3]:查詢資料")
    print("[4]:移轉資料")
    print("[5]:列印資料")
    print("[6]:統計客戶人數")
    print("[7]:客戶平均年齡")
    print("[q]:回到上一頁")

def supplier_func():
    table_head(145)
    print("<<供應商資料表>>")
    print("[1]:新增資料")
    print("[2]:查詢資料")
    print("[3]:列印資料")
    print("[4]:修改資料")
    print("[5]:查詢供應商數量")
    print("[6]:查詢相同負責人")
    print("[q]:回到上一頁")

def purchase_func():
    table_head(145)
    print("<<客戶購買資料表>>")
    print("[1]:新增資料")
    print("[2]:查詢資料")
    print("[3]:修改資料")
    print("[4]:交貨完成登記")
    print("[q]:回到上一頁")

def errAnimate():
    print("Please try again.", end="")
    for i in range(6):
        print(".", end="")
        time.sleep(0.3)
    print()



def table_head(width): #表格上下底
    print("+", end="")
    for i in range(width):
        print("-", end="")
    print("+")
def table_blank(width): #表格空白
    print("|", end="")
    for i in range(width):
        print(" ", end="")
    print("|")


flowers = ["花草苗木編號","花草苗木名稱","供應商名稱","公司內現有數量","單位","單價","小計","公司內存放位置","進貨日期"]
customer = ["客戶姓名","身分證字號/統一編號","生日","電話","Email","年齡","照片","會員折扣","地址"]
supplier = ["供應商名稱","供應商統一編號","電話","Email","負責人姓名","地址"]
purchase = ["花草苗木名稱","客戶身分證字號/統一編號","花草苗木編號","供應商名稱","購買數量","售價","總金額","折扣後金額","訂購日期","預計交貨日期","實際交貨日期"]

t1 = [["09-876-0543-2","玫瑰花","南海苗圃",50,"束",6.00,300.00,"二樓花房","2018-11-20"]]
t2 = [["胡謅鄒","B123456789","2000-11-13","04-2345-6666","321@gmail.com" ,30,"photo",0.82,"台中市台灣大道四段一七二七號"]]
t3 = [["南海苗圃","C312345678","04-2359-0121","221@gmail.com","王海東","台中市台灣大道14號"]]
t4 = [["水仙花","B187654321","08-878-0540-2","北海苗園", 30, 15.00, 450.00, 369.00,"2018-10-31","2018-11-02","2018-11-02"]]

def clen(str1, length): # 每多幾個中文字就少幾個補齊字元
    str1 = str(str1)
    return length - len(str1.encode("big5")) + len(str1)

## 花表 2D list
def flowers_format(list1):
    print(f"|{list1[0]:<{clen(list1[0], 15)}}|{list1[1]:<{clen(list1[1], 15)}}|{list1[2]:<{clen(list1[2], 15)}}|{list1[3]:<{clen(list1[3], 15)}}|{list1[4]:<{clen(list1[4], 5)}}|{list1[5]:<{clen(list1[5], 5)}}|{list1[6]:<{clen(list1[6], 10)}}|{list1[7]:<{clen(list1[7], 15)}}|{list1[8]:<{clen(list1[8], 30)}}")
    # flen = len(f"|{list1[0]:<{clen(list1[0], 15)}}|{list1[1]:<{clen(list1[1], 15)}}|{list1[2]:<{clen(list1[2], 15)}}|{list1[3]:<{clen(list1[3], 15)}}|{list1[4]:<{clen(list1[4], 5)}}|{list1[5]:<{clen(list1[5], 5)}}|{list1[6]:<{clen(list1[6], 10)}}|{list1[7]:<{clen(list1[7], 15)}}|{list1[8]:<{clen(list1[8], 10)}}")
    # return flen
    ## 回傳字串長度 沒有用到
def flowers_table(list1):
    flowers_format(flowers)
    for i in list1:
        for j in range(len(i)):
            i[j] = str(i[j])
        flowers_format(i)
    tlen = 0
    if 6 - len(list1) > 0:
        tlen = 6 - len(list1)
    for i in range(tlen):
        print("|")

## 顧客表 2D list
def customer_format(list1):
    print(f"|{list1[0]:<{clen(list1[0], 8)}}|{list1[1]:<{clen(list1[1], 20)}}|{list1[2]:<{clen(list1[2], 11)}}|{list1[3]:<{clen(list1[3], 13)}}|{list1[4]:<{clen(list1[4], 20)}}|{list1[5]:<{clen(list1[5], 5)}}|{list1[6]:<{clen(list1[6], 9)}}|{list1[7]:<{clen(list1[7], 9)}}|{list1[8]:<{clen(list1[8], 20)}}")
def customer_table(list1):
    customer_format(customer)
    for i in list1:
        for j in range(len(i)):
            i[j] = str(i[j])
        customer_format(i)
    tlen = 0
    if 6 - len(list1) > 0:
        tlen = 6 - len(list1)
    for i in range(tlen):
        print("|")

## 供應商表 2D list
def supplier_format(list1):
    print(f"|{list1[0]:<{clen(list1[0], 13)}}|{list1[1]:<{clen(list1[1], 15)}}|{list1[2]:<{clen(list1[2], 13)}}|{list1[3]:<{clen(list1[3], 20)}}|{list1[4]:<{clen(list1[4], 11)}}|{list1[5]:<{clen(list1[5], 30)}}")
def supplier_table(list1):
    supplier_format(supplier)
    for i in list1:
        for j in range(len(i)):
            i[j] = str(i[j])
        supplier_format(i)
    tlen = 0
    if 6 - len(list1) > 0:
        tlen = 6 - len(list1)
    for i in range(tlen):
        print("|")

## 購買表 2D list
def purchase_format(list1):
    print(f"|{list1[0]:<{clen(list1[0], 13)}}|{list1[1]:<{clen(list1[1], 24)}}|{list1[2]:<{clen(list1[2], 14)}}|{list1[3]:<{clen(list1[3], 11)}}|{list1[4]:<{clen(list1[4], 9)}}|{list1[5]:<{clen(list1[5], 6)}}|{list1[6]:<{clen(list1[6], 8)}}|{list1[7]:<{clen(list1[7], 11)}}|{list1[8]:<{clen(list1[8], 12)}}|{list1[9]:<{clen(list1[9], 12)}}|{list1[10]:<{clen(list1[10], 12)}}")
def purchase_table(list1):
    purchase_format(purchase)
    for i in list1:
        for j in range(len(i)):
            i[j] = str(i[j])
        purchase_format(i)
    tlen = 0
    if 6 - len(list1) > 0:
        tlen = 6 - len(list1)
    for i in range(tlen):
        print("|")


# 正則表達式

if __name__ == "__main__":
    supplier_table(t3)
    pass