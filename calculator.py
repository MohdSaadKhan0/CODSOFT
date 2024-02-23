def addition(x, y):
    return x + y

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero."

def calculator():
    while True:
        print("Options:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Input choice (1, 2, 3, 4, 5): ")

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
                continue

            if choice == '1':
                print(f"Result: {addition(num1, num2)}")
            elif choice == '2':
                print(f"Result: {subtraction(num1, num2)}")
            elif choice == '3':
                print(f"Result: {multiplication(num1, num2)}")
            elif choice == '4':
                print(f"Result: {division(num1, num2)}")

        elif choice == '5':
            print("Exiting Calculator")
            break
        else:
            print("Invalid input. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    calculator()
