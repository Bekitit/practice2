transaction = []
balance = 0

def add_income():
    global balance
    amount = float(input("Enter Amount:  "))
    description = input('Enter Description:  ')
    balance += amount
    transaction.append({"type":'income',"amount":amount,"description":description})
def add_expense():
    global balance
    amount = float(input("Enter Amount:  "))  
    description = input("Enter Description:  ")
    balance -= amount
    transaction.append({"type":"expense","amount":amount,'description':description})
def show_balance():
    global balance
    print('Your Current Balance is:  '+ str(balance))
def transaction_history():
    print('   Transaction History   ')
    for t in transaction:
        
        print(t["type"] + " " + str(t["amount"]) + " " + t["description"])         
def main():
    while True:
       print(' Personal Finance Tracker ')
       print("1: Add Income")
       print("2: Add EXpense")
       print("3: Show Balance")
       print("4: Transaction History")
       print("5: Exit")
       chose = int(input("   CHOSE 1-5   "))
       if chose == 1:
           add_income()
       elif chose == 2:
           add_expense()
       elif chose == 3:
           show_balance()
       elif chose == 4:
           transaction_history()
       elif chose == 5:
           print('   Goodbye  ')
           break
       else:
           print('Invalid Number Please Try Again  ')
main()                           