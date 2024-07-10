def add():
    print("sum is: ",x + y)
def subtract():
    print("difference is: ",x-y)
def mult():
    print("the product is: ",x*y)
def div():
    print("the quotient is: ",x/y)
x=int(input("enter the first input: "))
y=int(input("enter the second number: "))
choice=input("enter your choice(+,*,/,-)")
if choice=="+":
    add()
elif choice=="-":
    subtract()
elif choice=="*":
    mult()
elif choice=="/":
    div()
