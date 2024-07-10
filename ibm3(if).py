username=input("enter your username: ")
if username=="abel":
    print("welcome ",username)
    password=input("enter password: ")
    if password=="password123":
        print("welcome Abel")
        choice=input("do you wish to continue(y/n)")
        if choice=="y":
            print("nothing more in this site bye bye")
            exit()
        else:
            print("byebye")
            exit()
    else:
        print("invalid password")
    
else:
    print("invalid login")
