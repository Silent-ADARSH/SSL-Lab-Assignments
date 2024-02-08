print("Welcome to PNB\n\nInsert your card")
password=2004

choice=0
Amount=0
MONEY=0
for i in range(3):
    pin=int(input("Enter your 4 digit pin"))
    if pin==password:
        print("pin confirmed!")
        print("What DO YOU WANT TO do?")
        print("1 == balance")
        print("2 == deposit")
        print("3 == withdraw")
        print("4 == cancel")
        break

    else:
        print("PIN incorrect!!!! please retry.")

    if i==2:
        print("Transaction Cancelled,RETRY")
        exit()
    
choice = int(input("Kindly select your choice\n"))
if choice == 1: 
    print("your current balance is 10000 rupees")
    
elif choice == 2:
    print("enter the amount you want to deposit")
    Amount = int(input("amount->"))
    b= 10000+Amount
    print("thankyou for your transaction\nyour current balance is\n")
    print(b)
    
elif choice == 3:
    print("enter the amount you want to withdraw")
    MONEY = int(input("amount to withdraw->"))
    c=10000-MONEY
    print("thankyou for your transaction\nyour current balance is\n")
    print(c)
    
elif choice == 4:
    print(" TRANSACTION COMPLETED\n\nYOU CAN REMOVE YOUR CARD")