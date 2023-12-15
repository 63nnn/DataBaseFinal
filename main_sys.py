import login
import interface 


def main():
    while True: #login
        interface.login_menu()
        login_choice = input("act:")
        if login_choice == "1":
            if login.login_staff():
                break
        elif login_choice == "2":
            return
        else:
            print("Please try again.")
    while True:
        interface.main_menu()
        manip = input("act:")



if __name__ == "__main__":
    main()
    end = input("press Enter to exit.......")