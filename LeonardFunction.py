
def letterCaseCounter(text):
    # Initialize counters
    uppercase_count = 0
    lowercase_count = 0

    # loop through each character in the string
    for char in text:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1

    print("Total Uppercase Letters:", uppercase_count)
    print("Total Lowercase Letters:", lowercase_count)


# Get input from user
user_input = input("Enter a string or sentence: ")
# Call the function with user input
letterCaseCounter(user_input)
