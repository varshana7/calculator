def calculator():
    print("CALCULATOR")

    try:
        num1=float(input("enter num 1: "))
        num2=float(input("enter num 2: "))
        op=input("enter operator(+,-,%,/,*): ")
        if (op == "+"):
            sum=num1+num2
            print(sum)
        elif(op == "-"):
            sub=num1-num2
            print(sub)
        elif(op == "%"):
            mod=num1%num2
            print(mod)
        elif(op == "/"):
            div=num1/num2
            print(div)
        elif(op =="*"):
            mul=num1*num2
            print(mul)
        else:
            print("invalid operator")
    except ValueError:
        print("Enter a valid number")
calculator()
print("Thank you for using calculator")