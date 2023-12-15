import os
import login
import interface
import flowersFunc
import customerFunc
import stableCustomerFunc
import supplierFunc
import purchaseFunc


def main():
    while True: #login
        interface.login_menu()
        # login_choice = input("act:")
        login_choice = "1"          # 要記得刪掉
        if login_choice == "1":
            if login.login_staff():
                break
        elif login_choice == "2":    
            return
        else:
            print("Please try again.")
    while True:
        interface.main_menu()
        manip = input("輸入數字選擇要查看的功能:")
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
        elif manip == "6":
            print("Not yet")
            pass
        else:
            print("Please try again.")



if __name__ == "__main__":
    main()
    end = input("press Enter to exit.......")