print("Welcome to the Calculator")
print("1. addition")
print("2. subtraction")
print("3. multiplication")
print("4. division")
choice = input("enter choice 1/2/3/4: ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if choice == "1":
    print("result:",num1 + num2)
elif choice == "2":
    print("result:", num1 - num2)
elif choice == "3":
    print("result:", num1 * num2)
elif choice == "4":
    if num2 != 0:
        print("result:", num1 / num2)
    else:
        print("cannot be divisible by zero")
else:
    print("Invalid input")