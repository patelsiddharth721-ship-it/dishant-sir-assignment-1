import numpy as np

print("=" * 60)
print("SESSION 8 - Useful Utility Functions - 1 (All Tasks)")
print("=" * 60 + "\n")

# ==========================================
# TASK 1: Unique IPL Team Names (np.unique())
# ==========================================
print("--- TASK 1: Unique IPL Team Names ---")
ipl_teams = np.array(['MI', 'CSK', 'RCB', 'MI', 'DC', 'CSK', 'RCB', 'KKR', 'GT', 'MI'])

unique_teams = np.unique(ipl_teams)

print(f"All IPL Teams:        {ipl_teams}")
print(f"Sorted Unique Teams:  {unique_teams}")
print("\n" + "=" * 60 + "\n")

# ==========================================
# TASK 2: Missing Zomato Ratings (np.isnan())
# ==========================================
print("--- TASK 2: Missing Zomato Ratings ---")
zomato_ratings = np.array([4.2, np.nan, 3.8, 4.5, np.nan, 5.0, 3.2, np.nan])

missing_mask = np.isnan(zomato_ratings)
missing_count = np.sum(missing_mask)

print(f"Zomato Ratings:       {zomato_ratings}")
print(f"Number of Missing (NaN) Ratings: {missing_count}")
print("\n" + "=" * 60 + "\n")

# ==========================================
# TASK 3: Flipkart Price Clipping (np.clip())
# ==========================================
print("--- TASK 3: Flipkart Price Clipping ---")
flipkart_prices = np.array([45, 150, 850, 1200, 320, 95])

clipped_prices = np.clip(flipkart_prices, 100, 1000)

print(f"Original Prices: {flipkart_prices}")
print(f"Clipped Prices (Between 100 and 1000): {clipped_prices}")
print("\n" + "=" * 60 + "\n")

# ==========================================
# TASK 4: YouTube Views Handling (NaN and Inf)
# ==========================================
print("--- TASK 4: Handling NaN and Inf in YouTube Views ---")
yt_views = np.array([1200, np.nan, 45000, np.inf, 3200, -np.inf, np.nan, 98000])

# Find max finite value to replace inf
finite_mask = np.isfinite(yt_views)
max_finite = np.max(yt_views[finite_mask])

# Create copies/modifications
cleaned_views = yt_views.copy()

# Replace NaN with 0
cleaned_views[np.isnan(cleaned_views)] = 0

# Replace positive/negative inf with max finite value
cleaned_views[cleaned_views == np.inf] = max_finite
cleaned_views[cleaned_views == -np.inf] = max_finite

print(f"Original Views (with NaN/Inf): {yt_views}")
print(f"Max Finite Value:              {max_finite}")
print(f"Cleaned Views Array:           {cleaned_views}")
print("\n" + "=" * 60 + "\n")

# ==========================================
# TASK 5: Finding Even Number Indices (np.where())
# ==========================================
print("--- TASK 5: Finding Even Number Indices ---")
numbers = np.array([12, 17, 24, 33, 40, 55, 62])

# Find indices of even numbers using np.where()
even_indices = np.where(numbers % 2 == 0)

print(f"Numbers Array:       {numbers}")
print(f"Indices of Evens:    {even_indices[0]}")
print(f"Actual Even Numbers: {numbers[even_indices]}")
print("=" * 60)