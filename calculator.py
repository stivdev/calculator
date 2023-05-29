def add(a, b):
    return a + b

def subtract(a, b):
    return a - b


print("Select an operation:")
print("1. Add")
print("2. Subtract")

choice = input("Enter your choice (1-2): ")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if choice == '1':
    print("Result:", add(num1, num2))
elif choice == '2':
    print("Result:", subtract(num1, num2))
else:
    print("Invalid choice!")
