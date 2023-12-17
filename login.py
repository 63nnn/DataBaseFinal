import time

adminacc = "0001"
adminpwd = "0001"



def login_staff():
    while True:
        acc = input("account: ")
        # acc = adminacc              # 要記得刪掉
        if acc == "":
            break   
        if (adminacc!=acc):
            print(f'"{acc}"account does not exist.')
            continue

        pwd=input("password: ")
        # pwd = adminpwd              # 要記得刪掉
        if pwd=="": 
            break  
        if (adminpwd != pwd):
            print("wrong password.")
        else:
            print()
            print("Login success.")
            print()
            time.sleep(0.5)
            return True
        

