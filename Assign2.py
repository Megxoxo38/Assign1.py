def add(num1, num2):
    return num1 + num2
def sub(num1, num2):
    return num1-num2
def mul(num1, num2):
    return num1 * num2
def div(num1, num2):
    if num2 == 0:
        print("error division by zero")
        return 
    else:
        return num1 / num2
def cal(add, sub, mul, div):
    num1 = float(input("enter the first number"))
    num2 = float(input("enter the second number"))
    ops = (input("enter any of the operations (+,-,*,/)"))
    if ops == "+":
        result = add(num1, num2)
    elif ops == '-':
        result = sub(num1, num2)
    elif ops == '*':
        result = mul(num1, num2)
    elif ops == '/':
        result = div(num1, num2)
    else:
        print("INVALID OPERATOR")
        return
    print(f"{num1} {ops} {num2} = {result}")
cal(add, sub, mul, div)


