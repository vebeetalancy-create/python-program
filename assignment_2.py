#1.Basic Calculator Using Control Structures
#user inputs
num1 = float(input("Enter the first number : - "))
num2 = float(input("Enter the second number : - "))
#user operations
operation = input("Choose operation (+, -, *, /, %, //, **): ")
# calculation using if-elif-else
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
elif operation == "%":
    result = num1 % num2
elif operation == "//":
    result = num1 // num2
elif operation == "**":
    result = num1 ** num2
else:
    result = "Invalid operation selected."
print("Result:", int(result))

#2. Numeric Pattern Generation Using Nested Loops
#user input
rows = int(input("Enter the number of rows: "))
# number pattern
for i in range(1, rows + 1):
    for j in range(i, 0, -1):
        print(j, end='')
    print()