"""import numpy as np

print("=" * 60)
print("SESSION 5 - Mathematical & Statistical Functions (All Tasks)")
print("=" * 60 + "\n")

# ==========================================
# TASK 1: Instagram Likes (Add & Subtract)
# ==========================================
print("--- TASK 1: Instagram Likes ---")
my_likes = np.array([120, 145, 98, 210, 175, 300, 245])
friend_likes = np.array([95, 180, 110, 190, 220, 275, 210])

combined_likes = np.add(my_likes, friend_likes)
difference_likes = np.subtract(my_likes, friend_likes)

print("My Likes:      ", my_likes)
print("Friend's Likes:", friend_likes)
print("Combined Likes:", combined_likes)
print("Difference:    ", difference_likes)
print("\n" + "=" * 60 + "\n")

# ==========================================
# TASK 2: Zomato Order Discount & Bill
# ==========================================
print("--- TASK 2: Zomato Order Discount ---")
prices = np.array([250.0, 450.0, 120.0, 320.0, 599.0])

# Apply 10% discount (multiply by 0.9)
discounted_prices = np.multiply(prices, 0.9)
final_bill = np.sum(discounted_prices)

print("Original Prices:   ", prices)
print("Discounted Prices: ", discounted_prices)
print(f"Final Bill Amount: ₹{final_bill:.2f}")
print("\n" + "=" * 60 + "\n")

# ==========================================
# TASK 3: 30-Day Step Count Analysis
# ==========================================
print("--- TASK 3: Fitness Step Count Analysis ---")
np.random.seed(42)
steps = np.random.randint(4000, 14000, size=30)

mean_steps = np.mean(steps)
median_steps = np.median(steps)
std_steps = np.std(steps)
max_steps = np.max(steps)

print("Daily Steps (30 days):", steps)
print(f"Average Steps:   {mean_steps:.1f}")
print(f"Median Steps:    {median_steps:.1f}")
print(f"Standard Dev:    {std_steps:.1f}")
print(f"Max Daily Steps: {max_steps}")
print("\n" + "=" * 60 + "\n")

# ==========================================
# TASK 4: BookMyShow Movie Rating Rounding
# ==========================================
print("--- TASK 4: BookMyShow Rating Rounding ---")
np.random.seed(10)
ratings = np.random.uniform(1.0, 5.0, size=10)

rounded = np.round(ratings)
floored = np.floor(ratings)
ceiled = np.ceil(ratings)

for r, ro, f, c in zip(ratings, rounded, floored, ceiled):
    print(f"Original: {r:.2f} | Round: {ro:.0f} | Floor: {f:.0f} | Ceil: {c:.0f}")
print("\n" + "=" * 60 + "\n")

# ==========================================
# TASK 5: Spotify Skip Analysis
# ==========================================
print("--- TASK 5: Spotify Skip Analysis ---")
np.random.seed(7)
spotify_plays = np.random.choice([0, 1], size=20, p=[0.6, 0.4])

skip_percentage = (np.sum(spotify_plays) / len(spotify_plays)) * 100
p75 = np.percentile(spotify_plays, 75)

print("Last 20 Spotify Plays (1=Skipped, 0=Listened):")
print(spotify_plays)
print(f"Percentage of Songs Skipped: {skip_percentage:.1f}%")
print(f"75th Percentile of Skips: {p75}")
print("=" * 60)"""