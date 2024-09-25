#sample calculater program 
#create class name as a calculater:

def calculater():
    print("sample calculater:")
    while True:
        num1=float(input("Enter first number:"))
        operater=input("Enter a operater(+,-,*,/)")
        num2=float(input("Enter second number:"))
        if operater=="+":
            print(num1+num2)
        elif operater=="-":
            print(num1-num2)
        elif operater=="*":
            print(num1*num2)
        elif operater=="/":
            if num2 !=0:
                print(num1/num2)
            else:
                print("error: Division by zero")
        else:
            print("invalid operater")
calculater()                             