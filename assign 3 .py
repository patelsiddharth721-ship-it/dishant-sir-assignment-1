import numpy as np

# Task 1: Instagram likes on 7 posts and properties
insta_likes = np.array([120, 450, 89, 1024, 340, 750, 520])
print("--- Task 1: Instagram Likes Properties ---")
print(f"Array: {insta_likes}")
print(f"ndim: {insta_likes.ndim}")
print(f"shape: {insta_likes.shape}")
print(f"size: {insta_likes.size}")
print(f"dtype: {insta_likes.dtype}")
print(f"itemsize: {insta_likes.itemsize} bytes")
print(f"nbytes: {insta_likes.nbytes} bytes")
print("-" * 40)

# Task 2: 2D step counts for 5 days (5 rows, 2 cols: morning, evening)
step_counts = np.array(
    [[4000, 3500], [4500, 4000], [5000, 4500], [3800, 3200], [4200, 3900]]
)
print("--- Task 2: Reshaping Step Counts ---")
print("Original 2D shape:", step_counts.shape)

# Convert to 1D
step_1d = step_counts.reshape(-1)
print("Reshaped to 1D shape:", step_1d.shape)

# Convert back to 5x2 2D array
step_2d_back = step_1d.reshape(5, 2)
print("Reshaped back to 2D shape:", step_2d_back.shape)
print("-" * 40)

# Task 3: Zomato 12 food prices with ravel, flatten, and resize
zomato_prices = np.array(
    [150, 200, 250, 300, 120, 180, 220, 350, 400, 130, 160, 210]
)
print("--- Task 3: Zomato Food Prices Reshaping ---")

# Reshaping into a 3x4 grid first to demonstrate ravel() and flatten() differences
prices_grid = zomato_prices.reshape(3, 4)

# ravel() returns a view (shares memory with the original array when possible)
ravled_prices = prices_grid.ravel()

# flatten() always allocates new memory and returns a copy
flattened_prices = prices_grid.flatten()

print("Ravelled prices:", ravled_prices)
print("Flattened prices:", flattened_prices)

# resize() modifies the array in-place and can change its total size
prices_grid.resize(2, 6)
print("Resized array (2x6):\n", prices_grid)
print("-" * 40)

# Task 4: Spotify playlist grid (3x3) using T and np.transpose()
spotify_grid = np.array([[12, 5, 8], [7, 15, 6], [10, 9, 14]])
print("--- Task 4: Spotify Playlist Grid Transpose ---")
print("Original Grid:\n", spotify_grid)
print("Using .T:\n", spotify_grid.T)
print("Using np.transpose():\n", np.transpose(spotify_grid))
print("-" * 40)

# Task 5: Flipkart ratings (15 items) -> 3x5 -> flatten
flipkart_ratings = np.array(
    [4.5, 4.0, 3.5, 5.0, 4.2, 3.8, 4.6, 4.1, 3.9, 4.7, 4.3, 4.4, 3.7, 4.9, 4.8]
)
print("--- Task 5: Flipkart Ratings Reshape & Flatten ---")
ratings_3x5 = flipkart_ratings.reshape(3, 5)
print("3x5 Array:\n", ratings_3x5)

ratings_flat = ratings_3x5.flatten()
print("Flattened back to 1D:", ratings_flat)

# Real-world usage difference between flatten() and ravel():
# - Use ravel() when you need memory efficiency and performance (it returns a view),
#   meaning changes to the flattened array will affect the original array.
# - Use flatten() when you need a safe, independent copy of the data, ensuring that
#   modifying the resulting 1D array does not mutate your original multi-dimensional dataset.