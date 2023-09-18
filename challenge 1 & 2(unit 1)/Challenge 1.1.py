import math
num = int(input("Enter a number: "))
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    factorial = math.factorial(num)
    print(f"The factorial of {num} is {factorial}")