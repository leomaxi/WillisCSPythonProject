import sys

# Check if an argument was passed
if len(sys.argv) > 1:
    name = sys.argv[1]
    print(f"Hello, {name}!")
else:
    print("Please provide your name as an argument.")