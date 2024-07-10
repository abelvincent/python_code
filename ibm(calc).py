def add():
    print("sum is: ",x + y)
def subtract():
    print("difference is: ",x-y)
def mult():
    print("the product is: ",x*y)
def div():
    print("the quotient is: ",x/y)
while True:
    try:
        x=int(input("enter the first input: "))
        y=int(input("enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        continue
    while True:
        choice=input("enter your choice(+,*,/,-) or 'q' to quit: ")
        if choice in ["+", "-", "*", "/", "q"]:
            break
        else:
            print("Invalid choice. Please enter a valid operation (+, -, *, /) or 'q' to quit.")

    if choice=="+":
        add()
    elif choice=="-":
        subtract()
    elif choice=="*":
        mult()
    elif choice=="/":
        div()
    elif choice.lower()=='q':
        print("thank you for using calculator")
        break
