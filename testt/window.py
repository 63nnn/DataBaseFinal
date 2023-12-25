import keyboard as ky



def show(f):
    def hotkey_pressed():
        print("Space was pressed!")

    # register the hotkey using the keyboard library
    ky.add_hotkey('space', hotkey_pressed)

    # wait for keyboard events
    ky.wait()
    
    list1 = f()
    index = [""]*len(list1)
    print(list1)
    print(index)
    return input()
        
    

def login_menu():
    list1 = ["[1]:登入系統", "[q]:關機"]
    return list1

def main_menu(prt = False):
    list1 = ["[1]:花草苗木資料表", "[2]:客戶資料表","[3]:靜止客戶資料表","[4]:供應商資料表","[5]:客戶購買資料表","[q]:登出系統"]
    if prt == True:
        for i in list1:
            print(i)
    return list1



print(show(main_menu))
