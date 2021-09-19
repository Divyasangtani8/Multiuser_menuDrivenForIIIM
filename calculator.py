def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2

def multi(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2

def display():

    print(''' operations available  :
                1 - Add
                2 - Subtract
                3 - Multiply
                4 - Divide
                5 - Exit''')

    choice = int(input("select operation by entering the assigned s.no"))

    n1 = int(input("enter 1st no. : "))
    n2 = int(input("enter 2nd no. : "))

    if choice == 1:
        print("addition is = ", add(n1, n2))
        display()

    elif choice == 2:
        print("subtraction is = ", sub(n1, n2))
        display()
    elif choice == 3:
        print("multiplicaton is = ", multi(n1, n2))
        display()
    elif choice == 4:
        print("division is = ", div(n1, n2))
        display()
    elif choice == 5:
        print("Thank you for using our service...")

    else:
        print("enter the input again")
        display()
    
display()

    
