mark1=int(input("enter mark1: "))
mark2=int(input("enter mark2: "))
mark3=int(input("enter mark3: "))
minimum=min(mark1,mark2,mark3)
avg=(mark1+mark2+mark3-minimum)/2
print("average of best 2 ",avg)
