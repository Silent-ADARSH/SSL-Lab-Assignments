#to print cube of a number using input and also using command line
import sys 
x = int(sys.argv[1])
print("From command line the cube is: ",x**3)
print("Enter the num: ")
a = int(input("From the user: "))
print("The cube of number is ",a**3)