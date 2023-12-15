import os

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
    os.system("cls")
    table_head(145)
    print("<<花草苗木資料表>>")
    print("[1]:新增資料")
    print("[2]:查詢資料")
    print("[3]:列印資料")
    print("[q]:回到上一頁")

def customer_func():
    table_head(145)
    print("[1]:")
    print("[2]:")
    print("[3]:")
    print("[4]:")
    print("[5]:")
    print("[q]:回到上一頁")

def stable_customer_func():
    table_head(145)
    print("[1]:")
    print("[2]:")
    print("[3]:")
    print("[4]:")
    print("[5]:")
    print("[q]:回到上一頁")


def supplier_func():
    table_head(145)
    print("[1]:")
    print("[2]:")
    print("[3]:")
    print("[q]:回到上一頁")

def purchase_func():
    table_head(145)
    print("[1]:")
    print("[2]:")
    print("[q]:回到上一頁")


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


def table(width):
    table_head(width)
    for i in range(30):
        table_blank(width)
    table_head(width)

t1 = ["09-876-0543-2","玫瑰花","南海苗圃",50,"束",6.00,300.00,"二樓花房","2018-11-20"]
t2 = ["胡謅鄒","B123456789","2000-11-13","04-2345-6666","321@gmail.com" ,30,"photo",0.82,"台中市台灣大道四段一七二七號"]
t3 = ["南海苗圃","C312345678","04-2359-0121","221@gmail.com","王海東","台中市台灣大道14號"]
t4 = ["水仙花","B187654321","08-878-0540-2","北海苗園", 30, 15.00, 450.00, 369.00,"2018-10-31","2018-11-02","2018-11-02"]

def clen(str1, length): # 每多幾個中文字就少幾個補齊字元
    str1 = str(str1)
    return length - len(str1.encode("big5")) + len(str1)

## 花表
def flowers_format(list1):
    print(f"|{list1[0]:<{clen(list1[0], 15)}}|{list1[1]:<{clen(list1[1], 15)}}|{list1[2]:<{clen(list1[2], 15)}}|{list1[3]:<{clen(list1[3], 15)}}|{list1[4]:<{clen(list1[4], 5)}}|{list1[5]:<{clen(list1[5], 5)}}|{list1[6]:<{clen(list1[6], 10)}}|{list1[7]:<{clen(list1[7], 15)}}|{list1[8]:<{clen(list1[8], 10)}}")
    flen = len(f"|{list1[0]:<{clen(list1[0], 15)}}|{list1[1]:<{clen(list1[1], 15)}}|{list1[2]:<{clen(list1[2], 15)}}|{list1[3]:<{clen(list1[3], 15)}}|{list1[4]:<{clen(list1[4], 5)}}|{list1[5]:<{clen(list1[5], 5)}}|{list1[6]:<{clen(list1[6], 10)}}|{list1[7]:<{clen(list1[7], 15)}}|{list1[8]:<{clen(list1[8], 10)}}")
    return flen
def flowers_table():
    flowers_format(flowers)
    flowers_format(t1)
    for i in range(3):
        print("|")

## 顧客表
def customer_format(list1):
    print(f"|{list1[0]:<{clen(list1[0], 8)}}|{list1[1]:<{clen(list1[1], 20)}}|{list1[2]:<{clen(list1[2], 11)}}|{list1[3]:<{clen(list1[3], 13)}}|{list1[4]:<{clen(list1[4], 20)}}|{list1[5]:<{clen(list1[5], 5)}}|{list1[6]:<{clen(list1[6], 5)}}|{list1[7]:<{clen(list1[7], 9)}}|{list1[8]:<{clen(list1[8], 30)}}")
def customer_table():
    customer_format(customer)
    customer_format(t2)
    for i in range(3):
        print("|")

## 供應商表
def supplier_format(list1):
    print(f"|{list1[0]:<{clen(list1[0], 13)}}|{list1[1]:<{clen(list1[1], 15)}}|{list1[2]:<{clen(list1[2], 13)}}|{list1[3]:<{clen(list1[3], 20)}}|{list1[4]:<{clen(list1[4], 11)}}|{list1[5]:<{clen(list1[5], 30)}}")
def supplier_table():
    supplier_format(supplier)
    supplier_format(t3)
    for i in range(3):
        print("|")

## 購買表
def purchase_format(list1):
    print(f"|{list1[0]:<{clen(list1[0], 13)}}|{list1[1]:<{clen(list1[1], 24)}}|{list1[2]:<{clen(list1[2], 14)}}|{list1[3]:<{clen(list1[3], 11)}}|{list1[4]:<{clen(list1[4], 9)}}|{list1[5]:<{clen(list1[5], 6)}}|{list1[6]:<{clen(list1[6], 8)}}|{list1[7]:<{clen(list1[7], 11)}}|{list1[8]:<{clen(list1[8], 12)}}|{list1[9]:<{clen(list1[9], 12)}}|{list1[10]:<{clen(list1[10], 12)}}")
def purchase_table():
    purchase_format(purchase)
    purchase_format(t4)
    for i in range(3):
        print("|")

## tests
# flowers_table()
# customer_table()
# customer_table()
# purchase_table()

# 正則表達式

if __name__ == "__main__":
    pass