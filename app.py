def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def main():
    print("Menu-Driven Calculator:")
    print("1. Addition")
    print("2. Subtraction")
    choice = input("Select choice: ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if choice == '1':
        print(f"Result: {add(num1, num2)}")
    elif choice == '2':
        print(f"Result: {subtract(num1, num2)}")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
