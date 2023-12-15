

adminacc = "0001"
adminpwd = "0001"



def login_staff():
    while True:
        acc = input("account: ")
        if acc == "":
            break   
        if (adminacc!=acc):
            print(f'"{acc}"account does not exist.')
            continue

        pwd=input("password: ")
        if pwd=="": 
            break  
        if (adminpwd != pwd):
            print("wrong password.")
        else:
            print()
            print("Login success.")
            print()
            return True
        

