data = {
    123456:{'name': 'Tharun', 'pin': 1234, 'balance': 10000,'history': []},
    234567:{'name': 'Rohit', 'pin': 1234, 'balance': 20000,'history': []},
    345678:{'name': 'Ramesh', 'pin': 1234, 'balance': 30000,'history': []}
}

def logic():
    global acc_num
    acc_num = int(input("Enter your account number: "))
    pin = int(input("Enter your pin: "))
    if acc_num in data and data[acc_num]['pin'] == pin:
        print("Login successful")
        return True
    else:
        print("Invalid account number or pin")


def menu():
    print(f"Welcome to the ATM, {data[acc_num]['name']}")
    print("[C] Check Balance")
    print("[D] Deposit")
    print("[W] Withdraw")
    print("[H] Transaction History")
    print("[Q] Quit")

def checkbalance():
    print(f"Hello, {data[acc_num]['name']}")
    print("Current balance:", data[acc_num]['balance'],end="\n\n")

def deposit():
    amount = int(input("Enter amount to deposit:"))
    data[acc_num]['balance']+=amount
    data[acc_num]['history'].append(f'{amount} is deposited')
    print(f'{amount} is deposited successfully')
    checkbalance()

def withdraw():
    amount = int(input("Enter amount to withdraw:"))
    if data[acc_num]['balance']>=amount:
        data[acc_num]['balance']-=amount
        data[acc_num]['history'].append(f'{amount} is withdrawn')
        print(f'{amount} is withdrawn successfully')
        checkbalance()
    else:
        print("Insufficient balance")

def transactionhistory():
    if data[acc_num]['history']:
        print("----------Transaction history:----------")
        for i in data[acc_num]['history']:
            print(i)
        print("----------end of transaction history----------")
    else:
        print("No transaction history ")



