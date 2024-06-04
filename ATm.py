import time
print(" WELCOME TO ISLAMIC BANKING")
print(" Please enter your card")
time.sleep(5)
password=1234
pin=int(input("enter your ATM pin "))
balance=5000
if pin==password:
    while True:
        
        print("""
            PRESS 
            1 for balance
            2 for withdrawl balance
            3 for deposit balace
            4 for exit
            """)

        try:
            option=int(input("please enter your choice "))
        except:
            print("please enter valid option ")
        if option==1:
            print(f"your current balance is {balance}")
            print("================================================")
        if option==2:
            withdraw_amount=int(input("pease enter your withdraw amount "))
            balance=balance-withdraw_amount
            print(f"{withdraw_amount} is debited from your account ")
            print(f"your current balance is {balance}")
            print("================================================")
        if option==3:
            deposite_amount=int(input("pease enter your deposite amount "))
            balance=balance+ deposite_amount
            print(f"{deposite_amount} is deposite to your account")
            print(f"your updated balance is {balance}")
            print("================================================")
        if option==4:
            break

else:
    print("wrong pin try again")
