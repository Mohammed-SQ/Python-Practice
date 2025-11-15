print("\nOptions:")

print("1. Divide two numbers")

print("2. Find remainder (modulus)")

print("3. Calculate power")

print("4. Quit")

choice = input("Enter your choice (1-4): ").strip()

if choice == '1':

    try:

        num1 = float(input("Enter first number: "))

        num2 = float(input("Enter second number: "))

        if num2 != 0:

            result = num1 / num2

            print(f"{num1} divided by {num2} is {result}")

        else:

            print("Cannot divide by zero.")

    except ValueError:

        print("Invalid numbers. Please enter valid numbers.")

elif choice == '2':

    try:

        num1 = int(input("Enter first number: "))

        num2 = int(input("Enter second number: "))

        if num2 != 0:

            result = num1 % num2

            print(f"Remainder of {num1} divided by {num2} is {result}")

        else:

            print("Cannot divide by zero.")

    except ValueError:

        print("Invalid numbers. Please enter integers.")

elif choice == '3':

    try:

        base = float(input("Enter base number: "))

        exponent = float(input("Enter exponent: "))

        result = base ** exponent

        print(f"{base} to the power of {exponent} is {result}")

    except ValueError:

        print("Invalid numbers. Please enter valid numbers.")

elif choice == '4':

    print("Goodbye!")
    
else:

    print("Invalid choice. Please select 1-4.")