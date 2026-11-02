import numpy as np

print("=" * 60)
print("SESSION 6 - Indexing & Slicing (All Tasks)")
print("=" * 60 + "\n")

# ==========================================
# TASK 1: Basic Indexing (First & Last Price)
# ==========================================
print("--- TASK 1: Basic Indexing ---")
prices = np.array([199, 299, 399, 499, 599])

first_price = prices[0]
last_price = prices[-1]

print(f"Prices Array: {prices}")
print(f"First Price:  {first_price}")
print(f"Last Price:   {last_price}")
print("\n" + "=" * 60 + "\n")

# ==========================================
# TASK 2: 2D Array Slicing (Cricket Scores)
# ==========================================
print("--- TASK 2: 2D Array Slicing ---")
cricket_scores = np.array([
    [45, 80, 12, 65, 102],  # Player 1
    [30, 42, 55, 18, 90],   # Player 2
    [100, 75, 40, 85, 60]   # Player 3
])

matches_2_to_4 = cricket_scores[:, 1:4]

print("Full Cricket Scores (Players x Matches):\n", cricket_scores)
print("\nScores for Matches 2 to 4 (Columns 1 to 3):\n", matches_2_to_4)
print("\n" + "=" * 60 + "\n")

# ==========================================
# TASK 3: Negative Indexing (Last 3 Ratings)
# ==========================================
print("--- TASK 3: Negative Indexing ---")
ratings = np.array([4.5, 3.8, 4.2, 2.9, 5.0, 3.5])

last_three = ratings[-3:]

print(f"Ratings Array:      {ratings}")
print(f"Last Three Ratings: {last_three}")
print("\n" + "=" * 60 + "\n")

# ==========================================
# TASK 4: Step Slicing (Every 3rd Number)
# ==========================================
print("--- TASK 4: Step Slicing ---")
natural_numbers = np.arange(1, 21)

step_sliced = natural_numbers[1::3]

print(f"Natural Numbers:             {natural_numbers}")
print(f"Every 3rd starting from 2nd: {step_sliced}")
print("\n" + "=" * 60 + "\n")

# ==========================================
# TASK 5: Boolean Indexing (Flipkart Prices > 500)
# ==========================================
print("--- TASK 5: Boolean Indexing ---")
flipkart_prices = np.array([349, 899, 450, 1299, 500, 650, 299])

expensive_prices = flipkart_prices[flipkart_prices > 500]

print(f"All Flipkart Prices:     {flipkart_prices}")
print(f"Prices Greater than 500: {expensive_prices}")
print("\n" + "=" * 60 + "\n")

# ==========================================
# TASK 6: np.where() (IPL Scores Above 200)
# ==========================================
print("--- TASK 6: np.where() ---")
ipl_scores = np.array([210, 180, 195, 220, 205, 175])

high_score_indices = np.where(ipl_scores > 200)

print(f"IPL Team Scores:         {ipl_scores}")
print(f"Indices of Scores > 200: {high_score_indices[0]}")
print(f"Actual Scores > 200:     {ipl_scores[high_score_indices]}")
print("=" * 60)