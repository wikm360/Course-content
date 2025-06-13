op = input("+یا -چه کار میخوای برات انجام") 
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
num1 = float(num1)
num2 = float(num2)
if op == '+':
    print(num1 + num2)
elif op == "*" :
    print(num1 * num2)
elif op == '-':
    print(num1 - num2)
elif op == "/" :
    print(num1 / num2)
else :
    print("eshtebah vared kardi")