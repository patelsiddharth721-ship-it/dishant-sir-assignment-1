import numpy as np

# Task 1: Instagram likes & comments -> engagement per post and average
likes = np.array([120, 450, 89, 1024, 340, 750, 520])
comments = np.array([12, 45, 8, 102, 34, 75, 52])
engagement_per_post = likes + comments
avg_total_engagement = engagement_per_post.mean()
print("--- Task 1: Instagram Engagement ---")
print(f"Engagement per post: {engagement_per_post}")
print(f"Average total engagement: {avg_total_engagement}")
print("-" * 40)

# Task 2: Zomato food prices & discounts -> final price using element-wise subtraction
zomato_prices = np.array([250, 400, 150, 300, 500])
zomato_discounts = np.array([50, 80, 20, 60, 100])
final_prices = zomato_prices - zomato_discounts
print("--- Task 2: Zomato Final Prices ---")
print(f"Final prices after discount: {final_prices}")
print("-" * 40)

# Task 3: IPL team scores for 5 matches -> boolean array for scores > 180
ipl_scores = np.array([165, 192, 178, 205, 180])
high_scores_mask = ipl_scores > 180
print("--- Task 3: IPL High Scores (>180) ---")
print(f"Scores: {ipl_scores}")
print(f"Matches > 180: {high_scores_mask}")
print("-" * 40)

# Task 4: Paytm & PhonePe transactions (6 transactions) -> np.logical_or()
paytm_paid = np.array([1, 0, 1, 0, 0, 1])
phonepe_paid = np.array([0, 1, 1, 0, 1, 0])
either_app_paid = np.logical_or(paytm_paid, phonepe_paid)
print("--- Task 4: Payment Gateway Logical OR ---")
print(f"Paid via either Paytm or PhonePe: {either_app_paid}")
print("-" * 40)

# Task 5: Weekly steps, broadcasting bonus (+500), and aggregate total sum
weekly_steps = np.array([6000, 7500, 8200, 5400, 9100, 6800, 7000])
bonus_steps = weekly_steps + 500  # Broadcasting (+500 to every element)
total_steps_week = bonus_steps.sum()  # Aggregate operation
print("--- Task 5: Step Counter with Broadcasting & Aggregation ---")
print(f"Original steps: {weekly_steps}")
print(f"Steps with 500 bonus: {bonus_steps}")
print(f"Total steps for the week: {total_steps_week}")