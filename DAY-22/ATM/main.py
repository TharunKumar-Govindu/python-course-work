import logic as lg

if lg.logic():
    while True:
        lg.menu()
        choice = input("Enter your choice: ")
        if choice == 'C':
            lg.checkbalance()
        elif choice == 'D':
            lg.deposit()
        elif choice == 'W':
            lg.withdraw()
        elif choice == 'H':
            lg.transactionhistory()
        elif choice == 'Q':
            print("Thank you for using the ATM")
            break
        else:
            print("Invalid choice")