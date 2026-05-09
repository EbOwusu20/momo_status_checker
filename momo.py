

code = input("Enter code: ")

if code != "*170#":
    print("Wrong Code")

else:
    print("\n1) Transfer Money")
    print("2) MomoPay")
    print("3) Airtime")
    print("4) Allow Cashout")
    print("5) Financial")
    print("#) Next")

    option = input("Enter option: ")

    if option == "#":

        print("\n6) My Wallet")
        print("7) Just4U")
        print("8) MoMo App")

        wallet = input("Enter option: ")

        if wallet == "6":

            print("\n1) Check Balance")
            print("2) Allow Cash Out")
            print("3) My Approvals")
            print("4) Report Fraud")
            print("5) Statements")

            balance_option = input("Enter option: ")

            if balance_option == "1":

                pin = input("\nEnter MoMo PIN: ")

                if pin == "2345":

                    print("\nCurrent Balance: GHS 10000.00")
                    print("Available Balance: GHS 10000.00")

                else:
                    print("Wrong PIN")

            else:
                print("Invalid Option")

        else:
            print("Invalid Option")

    else:
        print("Invalid Option")