#menu driven calculator
def add(a,b):
    return a+b 

def substract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def devide(a,b):
    if b==0:
        print("Error can not devide by zero")
    else:
        print("Result:",a/b)

while True:
    print("\n python calculator")
    print("1.addition")
    print("2.substraction")
    print("3.multipliation")
    print("4.Division")
    print("5.exit")
    
    choice = input("Enter your choice(1-5)")
    if choice == "5":
        print("Thank you") 
        break
    if choice not in ["1","2","3","4"]:
        print("invalid choice .please select a number from 1 to 5 ")
        continue
    
    try:
         n1=float(input("enter the no"))
         n2=float(input("enter the second number"))
    except ValueError:
        print("invalid input")
        continue
    if choice =="1":
        res=add(n1,n2)
        print("Result:",res)
    elif choice =="2":
        res=substract(n1,n2)
        print("Result:",res)
    elif choice =="3":
        res=multiply(n1,n2)
        print("Result:",res)
    elif choice =="4":
        res=devide(n1,n2)
        print("Result:",res)