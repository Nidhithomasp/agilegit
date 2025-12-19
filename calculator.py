def calculator():
    while True:
        print("\n--- Simple Calculator Menu ---")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Exit")
        
        choice = input("Select an option (1/2/3): ")

        if choice == '3':
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
        else:
            print("Invalid input! Please choose 1, 2, or 3.")

# Run the calculator
calculator()