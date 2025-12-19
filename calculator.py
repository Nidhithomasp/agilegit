def calculator():
    while True:
        print("\n--- Simple Calculator Menu ---")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiplication(*)")
        print("4. Division (/)")
        print("5. Exit")
        
        choice = input("Select an option (1/2/3/4/5): ")

        if choice == '5':
            print("Goodbye!")
            break

        if choice in ('1', '2'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                result = num1 + num2
                print(f"Result: {num1} + {num2} = {result}")
            
            elif choice == '2':
                result = num1 - num2
                print(f"Result: {num1} - {num2} = {result}")
            elif choice == '3':
                result = num1*num2
                print(f"Result: {num1}*{num2}={result}")
            elif choice == '4':
                result = num1 / num2
                print(f"Result: {num1} / {num2} = {result}")
        else:
            print("Invalid input! Please choose 1, 2, 3,4,5.")

# Run the calculator
calculator()