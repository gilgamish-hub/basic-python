# Task 2: Using the Math Module for Calculations

import math

# Taking input from the user
number = float(input("Enter a number: "))

if number <= 0:
    print("Please enter a positive number for valid results.")
else:
    sqrt_val = math.sqrt(number)
    log_val = math.log(number)
    sin_val = math.sin(number)

    print(f"\n--- Results ---")
    print(f"Square root of {number}: {sqrt_val}")
    print(f"Natural logarithm of {number}: {log_val}")
    print(f"Sine of {number} (in radians): {sin_val}")
