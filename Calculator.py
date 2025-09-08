from functions import*

while True:
    print("What do you want to do?")
    print("1 Addition")
    print("2 Subtration")
    print("3 Multipliation")
    print("4 Division")
    print("Enter Q to Exit")

    choice = input("Enter your choice : ")
    if choice == 'Q' or choice == 'q':
        break

    num1 = int(input("Enter the Number 1 : "))
    num2 = int (input("Enter the Number 2 : "))

    if choice == '1' :
        addition(num1, num2)
    elif choice == '2' :
        subtraction(num1, num2)
    elif choice == '3' :
        multiplication(num1, num2)
    elif choice == '4' :
        division(num1, num2) 
    else:
        print("Invalid Choice")   
    
    print('\n') #used to add a space between when executing.
    # we use a loop to execute the program endlessly. (frank ocean endless $$)               