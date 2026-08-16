a = float(input("Enter First No: "))
b = float(input("Enter Second No: "))

print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
choice = input("Enter Choice (1-4): ")

if choice == '1':
    print("Addition is:", a + b)
elif choice == '2':
    print("Subtraction is:", a - b)
elif choice == '3':
    print("Multiplication is:", a * b)
elif choice == '4':
    if b == 0:
        print("Cannot divide by zero!")
    else:
        print("Division is:", a / b)
else:
    print("Invalid choice!")