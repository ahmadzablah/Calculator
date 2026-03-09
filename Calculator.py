operator = input("Enter an Operator (+ - * /):")
num1 = float(input("Enter 1st Number:"))
num2 = float(input("Enter 2nd Number:"))

if operator == "+":
    result = num1 + num2
    print(round(result))
    
elif operator == "-":
    result = num1 - num2
    print(round(result))
    
elif operator == "*":
    result = num1 * num2
    print(round(result))
     
elif operator == "/":
    result = num1 / num2
    print(round(result))
    if num1 / num2 == 0:
        print("Error: Cannot Devide By Zero")
    
else:
    print(f"{operator} is not valid")
    
while True:
    operator = input("Enter an Operator (+ - * /):")
    num1 = float(input("Enter 1st Number:"))
    num2 = float(input("Enter 2nd Number:"))
