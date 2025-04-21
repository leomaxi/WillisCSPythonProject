def calculator():
    print("Hi, Welcome to tLeonard's consol calculator\n")

    while True:
        try:
            choice = askForInput()
            if choice == 5:
                print("Thanks for using Leonard's calculator. Goodbye!")
                break

            a = float(input("Enter the First Value: "))
            b = float(input("Enter the Second Value: "))

            if choice == 1:
                print(f"The result is: {a + b}")
            elif choice == 2:
                print(f"The result is: {a - b}")
            elif choice == 3:
                print(f"The result is: {a * b}")
            elif choice == 4:
                if b == 0:
                    print("Cannot divide it by zero")
                else:
                    print(f"The result is: {a / b}")
            else:
                print("Invalid choice. Please select between 1 and 5.")

        except ValueError:
            print("Invalid input. Please enter numeric values. Lets start again.")
            calculator()
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            calculator()
        print()
        print() # Blank lines as a style

def askForInput():
    print("Please choose the operations which you want to perform")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit Calculator")
    choice = int(input("Enter the choice which you want to perform: "))
    return choice

if __name__ == "__main__":
    calculator()
