from functools import reduce

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

multiply_all = lambda nums: reduce(lambda x, y: x * y, nums)

print("Result:", multiply_all(numbers))
#
# multiply = lambda x, y: x * y
#
# x = int(input("Enter x: "))
# y = int(input("Enter y: "))
#
# print("Result:", multiply(x, y))
