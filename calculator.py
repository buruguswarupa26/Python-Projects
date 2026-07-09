num1 = float(input("Enter your first number:"))
operator = input("Enter operator(+,-,*,/):")
num2 = float(input("Enter your second number:"))
if operator == "+":
    result = num1 + num2
    print("Result:",result)
elif operator == "-":
    result = num1 - num2
    print("Result:",result)
elif operator == "*":
    result = num1 * num2
    print("Result:",result) 
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print("Result:",result) 
    else:
        print("Error: Divided by zero is not allowed")
else:
    print("invalid operator")                      