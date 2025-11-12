operand1 = int(input("Enter first number: "))
operand2 = int(input("Enter first number: "))
operator = input("Enter operator: ")

if operator == '+':
    print(operand1+operand2)
if operator == '-':
    print(operand1-operand2)
if operator == '/':
    print(operand1/operand2)
if operator == '*':
    print(operand1*operand2)
else:
    print("Invalid operator")