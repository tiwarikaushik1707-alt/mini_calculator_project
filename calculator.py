def calculate(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b == 0:
            return "Error: Cannot divide by zero."
        return a / b
    else:
        return "Invalid operator."

print("----- Simple Calculator -----")

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    op = input("Choose operation (+, -, *, /): ")

    result = calculate(num1, num2, op)
    print("Result:", result)

except ValueError:
    print("Input error: Please enter valid numbers.")
