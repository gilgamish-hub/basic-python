# Task 1: Calculate Factorial Using a Function

def factorial(n):
    """Function to calculate factorial of a number using recursion"""
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# Example call
num = 5
result = factorial(num)
print(f"The factorial of {num} is: {result}")
