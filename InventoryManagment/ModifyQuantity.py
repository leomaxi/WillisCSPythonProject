# Inventory Management System
import os

def modify_quantity():
    target_description = input("Enter description of the coffee you want to update: ")
    updated = False

    try:
        with open("coffee_inventory.txt", "r") as original, open("temp_inventory.txt", "w") as temp:
            for line in original:
                description, quantity = line.strip().split(",")
                if description.lower() == target_description.lower():
                    try:
                        new_quantity = int(input(f"Enter new quantity for '{description}': "))
                        temp.write(f"{description},{new_quantity}\n")
                        updated = True
                        print("Record updated.")
                    except ValueError:
                        print("Invalid input. Skipping update.")
                        temp.write(line)
                else:
                    temp.write(line)
        # Replace the original file with the updated one
        os.remove("coffee_inventory.txt")
        os.rename("temp_inventory.txt", "coffee_inventory.txt")

        if not updated:
            print("No matching record found.")

    except FileNotFoundError:
        print("Inventory file not found.")

#modify_quantity()