# Inventory Management System
def add_record():
    with open("coffee_inventory.txt", "a") as file:
        while True:
            description = input("Enter coffee description (or type 'exit' to quit): ")
            if description.lower() == "exit":
                break
            try:
                quantity = int(input("Enter quantity: "))
                file.write(f"{description},{quantity}\n")
                print("Record added.")
            except ValueError:
                print("Invalid quantity. Please enter a number.")

#add_record()
