import numpy as np

print("=" * 60)
print("SESSION 9 - Mini NumPy Case Study (All Tasks)")
print("=" * 60 + "\n")

# ==========================================
# TASK 1: Create Prices Array & Check Dtype
# ==========================================
print("--- TASK 1: Create Prices Array ---")
prices = np.array([299, 499, 799, 0, 1599, -1, 899])

print(f"Prices Array: {prices}")
print(f"Data Type:    {prices.dtype}")
print("\n" + "=" * 60 + "\n")

# ==========================================
# TASK 2: Clean Data (Replace <= 0 with positive mean)
# ==========================================
print("--- TASK 2: Clean Invalid Prices ---")
positive_mask = prices > 0
positive_prices = prices[positive_mask]
mean_positive = np.mean(positive_prices)

cleaned_prices = prices.copy()
cleaned_prices[cleaned_prices <= 0] = mean_positive

print(f"Original Prices:   {prices}")
print(f"Positive Average:  {mean_positive:.2f}")
print(f"Cleaned Prices:    {cleaned_prices}")
print("\n" + "=" * 60 + "\n")

# ==========================================
# TASK 3: Calculate Total Bill per Item
# ==========================================
print("--- TASK 3: Item-wise Total Bills ---")
quantities = np.array([2, 1, 3, 4, 2, 1, 5])

total_bills = cleaned_prices * quantities

print(f"Quantities:    {quantities}")
print(f"Cleaned Prices:{cleaned_prices}")
print(f"Total Bills:   {total_bills}")
print("\n" + "=" * 60 + "\n")

# ==========================================
# TASK 4: Summary Report
# ==========================================
print("--- TASK 4: Summary Report ---")
min_price = np.min(cleaned_prices)
max_price = np.max(cleaned_prices)
mean_price = np.mean(cleaned_prices)
total_price = np.sum(cleaned_prices)
overall_total_bill = np.sum(total_bills)

print(f"Minimum Price:       {min_price:.2f}")
print(f"Maximum Price:       {max_price:.2f}")
print(f"Average Price:       {mean_price:.2f}")
print(f"Total Price Sum:     {total_price:.2f}")
print(f"Overall Total Bill:  {overall_total_bill:.2f}")
print("\n" + "=" * 60 + "\n")

# ==========================================
# TASK 5: Unique Price Values Count
# ==========================================
print("--- TASK 5: Unique Price Values Count ---")
unique_prices = np.unique(cleaned_prices)
unique_count = len(unique_prices)

print(f"Unique Price Values:     {unique_prices}")
print(f"Number of Unique Prices: {unique_count}")
print("=" * 60)