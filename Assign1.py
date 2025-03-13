def calculator():
    num1=float(input("enter the first number: "))
    num2=float(input("enter the second number: "))
    operator=(input("enter an operator(+ - / *): "))
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/' :
        if num2 != 0:
         result = num1 / num2
        else:
            print("Error division by zero")
        #return
    else:
        print ("INVALID OPERATOR")
        return
    print(f"{num1}  {operator}  {num2} =  {result}")


calculator()
