floor = int(input("Which floor would you like to go to? (1 to 10): "))
access_level = input("Do you have VIP access? (yes/no): ").lower()

if 1 <= floor <= 3:
    print(f"Access granted. Going to floor {floor}.")
elif 4 <= floor <= 7:
    if access_level == "yes":
        print(f"Access granted to VIP floor {floor}.")
    else:
        print("Access denied. VIP floors require special access.")
elif 8 <= floor <= 10:
    print(f"Warning: Floors {floor} to 10 are under maintenance.")
else:
    print("Invalid floor. Please choose between 1 and 10.")
