

# Info
# Password = Manish
# User_id = manishabc@xyz.com
# passcode = 1234

import sys  #importing for using exit function 

# Deciding the Password for Entering Banking System
Password = "Manish"

# Asking the user for Password 
x = input("Password: ")

i = 0
while(True):  
    
    if(x == Password):
        print("..................")
        print("Correct Passsword")
        print("Opening..")
        print(".................. \n")
        print("     #########  ")
        print("    #  >   <  # ")
        print("   #           #       Welcome To ABC Bank !!")
        print("    #   ---   # ")
        print("     #########  \n\n")
        
        break     # Getting out of infinite loop if password is correct  
    if(i == 2):
        print("You Entered Wrong Password 3 times")
        print("Account Locked for 24 hours")
        sys.exit()     # Getting out of code if password is wrong 3 times
    else:
        print(".........................")
        print("Wrong Password \n")
        print("Attempt Remaining ", 2 - i)
        print(".........................")
        x = input("Password: ")
        i = i + 1
        
print("*****Enter your Login credentials*****")

# Deciding the user login credentials
User_id = "manishabc@xyz.com" 
Passcode = "1234"

# Asking the user to enter to login credentials
u_id = input("User_id: ")
pcode = input("Passcode: ")  

while(True):
    if(u_id == User_id and pcode == Passcode):
        print("Welcome Manish Kumar")
        break
    else:
        if(u_id != User_id):
            print("User_id Entered Wrong")
        if(pcode != Passcode):
            print("Passcode Entered Wrong")
        print("\n")
        u_id = input("User_id: ")
        pcode = input("Passcode: ") 

# Entering into bank details
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

print("How can we Help you !! ")
print("1.  CHECK BALANCE")
print("2.  LOAN DETAILS")
print("3.  WITHDRAW MONEY")
print("4.  TRANSFER MONEY")
print("5.  WANT TO ASK A QUERY")
print("6.  TO SEE THE INDEX")
print("7.  EXIT FROM SYSTEM\n")

print("Enter the number of task you want to move forward into")


# Making the inside of each task 

balance = 1500000   # Initial balance 

while(True):
    
    task = input("Task: ")    # Getting the type of task input
    if(task == '1'):     # Checking Balance
        print("Your current balance is Rs ", balance)
        
    elif(task == '2'):   # Loan Details
        print("Type of Loan you desire")
        print("A.  Home Loan")
        print("B.  Education Loan")
        print("C.  Personal work Loan")
        print("D.  To Exit")
        
        # Declaring rate of interest of different loan types
        rate_a = 5
        rate_b = 3
        rate_c = 6
        
        while(True):
            loan = input("loan type : ")
            loan = loan.upper()
            if(loan == 'A'):    # Home loan
                print("Rate of Interest on Home Loan is currently:{0}% per year".format(rate_a))
                while(True):
                    try:
                        amount = int(input("Enter the Amount you want loan ,Rs: "))
                    except ValueError:
                        print("Enter the value in digits")
                    else:
                        break
                    
                while(True):
                    try:
                        time = int(input("Enter the number of years you want loan for: "))
                    except ValueError:
                        print("Enter the value in digits")
                    else:
                        break
                    
                s_i = amount * rate_a * time /100
                print("Simple Interest on your desired condition Rs ", s_i)
                t_amt = amount + s_i
                print("The Total  Amount to be paid is Rs: ", t_amt)
                
            elif(loan == 'B'):     # Education loan
                print("Rate of Interest on Education Loan is currently:{0}% per year".format(rate_b))
                while(True):
                    try:
                        amount = int(input("Enter the Amount you want loan ,Rs: "))
                    except ValueError:
                        print("Enter the value in digits")
                    else:
                        break
                    
                while(True):
                    try:
                        time = int(input("Enter the number of years you want loan for: "))
                    except ValueError:
                        print("Enter the value in digits")
                    else:
                        break
                    
                s_i = amount * rate_b * time /100
                print("Simple Interest on your desired condition Rs ", s_i)
                t_amt = amount + s_i
                print("The Total  Amount to be paid is Rs: ", t_amt)
                
            elif(loan == 'C'):      # Personal work loan
                print("Rate of Interest on Personal work Loan is currently:{0}% per year".format(rate_c))
                while(True):
                    try:
                        amount = int(input("Enter the Amount you want loan ,Rs: "))
                    except ValueError:
                        print("Enter the value in digits")
                    else:
                        break
                    
                while(True):
                    try:
                        time = int(input("Enter the number of years you want loan for: "))
                    except ValueError:
                        print("Enter the value in digits")
                    else:
                        break
                    
                s_i = amount * rate_c * time /100
                print("Simple Interest on your desired condition Rs ", s_i)
                t_amt = amount + s_i
                print("The Total  Amount to be paid is Rs: ", t_amt)
                
            elif(loan == 'D'):    # Exit from loan Details
                break
            
            else:
                print("Please enter from given choices only")
                
    elif(task == '3'):    # Withdraw money
        
            while(True):
                try:
                    w_money = int(input("Enter the amount you want to withdraw Rs: "))
                except ValueError:
                    print("Enter the value in digits")
                else:
                    break
            if(w_money <= balance):
                balance = balance - w_money 
                print("Cash Rs{0} withdrawn from your account total balance left Rs{1}".format(w_money, balance))
            else:
                print("Sorry cant perform the task ,your balance might be low")
                print("Type 1 to check your balance")
                
    elif(task == '4'):      # Transfering money

            p_id = input("Enter the person's id: ")
            while(True):
                try:
                    t_money = int(input("Enter the amount you want to transfer Rs: "))
                except ValueError:
                    print("Enter the value in digits")
                else:
                    break
            if(t_money <= balance):
                balance = balance - t_money
                print("Cash Rs{0} trsnsfered to {1} account".format(t_money, p_id))
                print("Total balance left {0}".format(balance))
            else:
                print("Sorry cant perform the task ,your balance might be low")
                print("Type 1 to check your balance")
        
    elif(task == '5'):      # Asking Query
        ques = input("Enter your Query : ")
        print("Our executive will answer your query within 24 hrs.")
        
    elif(task == '6'):      # Checking index
        print("1.  CHECK BALANCE")
        print("2.  NEED LOAN")
        print("3.  WITHDRAW MONEY")
        print("4.  TRANSFER MONEY")
        print("5.  WANT TO ASK A QUERY")
        print("6.  TO SEE THE INDEX")
        print("7.  EXIT FROM SYSTEM\n")
        
    elif(task == '7'):       # Exiting from Banking System
        print("*****THANKS FOR VISITING OUR ABC BANK *****")
        print(".................. \n")
        print("     #########  ")
        print("    #  >   <  # ")
        print("   #           #       BYE !!")
        print("    #   ---   # ")
        print("     #########  \n\n")
        break
    else:
        print("Please enter from given choices only")