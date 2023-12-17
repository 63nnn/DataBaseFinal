import os
import login
import interface
import flowersFunc
import customerFunc
import stableCustomerFunc
import supplierFunc
import purchaseFunc

#test


def main():
    while True:
        while True: #login
            os.system("cls")
            interface.login_menu()
            login_choice = input("act:").strip()
            # login_choice = "1"          # 要記得刪掉
            if login_choice == "1":
                if login.login_staff():
                    break
            elif login_choice == "q":    
                return
            else:
                print("Please try again.")
        while True:
            os.system("cls")
            interface.main_menu()
            manip = input("輸入數字選擇要查看的功能:").strip()
            
            if manip == "1":
                flowersFunc.mainFunc()
            elif manip == "2":
                customerFunc.mainFunc()
            elif manip == "3":
                stableCustomerFunc.mainFunc()
            elif manip == "4":
                supplierFunc.mainFunc()
            elif manip == "5":
                purchaseFunc.mainFunc()
            elif manip == "q":
                break
            else:
                print("Please try again.")
            



if __name__ == "__main__":
    main()
    end = input("press Enter to exit.......")