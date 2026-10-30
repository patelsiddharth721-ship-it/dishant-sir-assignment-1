import numpy as np

# Task 1: Create a NumPy array called my_scores with 5 Zomato order ratings
my_scores = np.array([4, 5, 3, 4, 5])
print("Task 1 - my_scores:", my_scores)

# Task 2: Generate an array of all even numbers between 10 and 30 (inclusive)
even_numbers = np.arange(10, 31, 2)
print("Task 2 - Even numbers (10 to 30):", even_numbers)

# Task 3: Generate an array of 8 equally spaced values between 0 and 1
linspace_array = np.linspace(0, 1, 8)
print("Task 3 - 8 equally spaced values (0 to 1):", linspace_array)

# Task 4: Simulate Flipkart 'Add to Cart' counter (10 zeros, update 3rd and 7th items to 1)
cart_counter = np.zeros(10, dtype=int)
cart_counter[2] = 1  # 3rd item (index 2)
cart_counter[6] = 1  # 7th item (index 6)
print("Task 4 - Updated Cart Counter:", cart_counter)

# Task 5: Create 6 random OTP codes between 1000 and 9999 with seed 42
np.random.seed(42)
otp_codes = np.random.randint(1000, 10000, size=6)
print("Task 5 - Paytm OTP Codes:", otp_codes)