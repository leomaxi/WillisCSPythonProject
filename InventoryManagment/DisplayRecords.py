# Inventory Management System
# Run from here - InventoryManagment/DisplayRecords.py
# All features are linked together to make it a complete app
import os
from pathlib import Path
from AddRecords import add_record
from ModifyQuantity import modify_quantity

# Enable users to add coffee inventory records to a file.

def display_records():
    try:
        # Check if the file exists, if not create it
        file_path = Path("coffee_inventory.txt")
        if not file_path.exists():
            file_path.touch()

        # Open the file in read mode
        with open("coffee_inventory.txt", "r") as file:
            # Read the contents of the file and display them
            print("\n Coffee Inventory Records ---")
            for line in file:
                # Split each line into description and quantity
                description, quantity = line.strip().split(",")
                # Print the description and quantity
                print(f"Description: {description}, Quantity: {quantity}")
            print("-----------------------------")

        #Ask user for input to add records or modify quantity
        userChoice = input("Enter 1 to add records, or 2 to Modify quantity?: ")
        if int(userChoice) == 1:
            add_record()
        elif int(userChoice) == 2:
            modify_quantity()
        else:
            print("Invalid choice. Please enter 1 or 2.");

    except FileNotFoundError:
        print("Couldn't Create / Read No inventory file.")

display_records()
