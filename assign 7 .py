import numpy as np

print("=" * 60)
print("SESSION 7 - Array Manipulation - 1 (All Tasks)")
print("=" * 60 + "\n")

# ==========================================
# TASK 1: Zomato & Swiggy Ratings (np.concatenate())
# ==========================================
print("--- TASK 1: Concatenating Ratings ---")
zomato_ratings = np.array([4.2, 4.5, 3.8, 4.0, 4.6])
swiggy_ratings = np.array([4.1, 3.9, 4.7, 4.3, 4.4])

combined_ratings = np.concatenate((zomato_ratings, swiggy_ratings))

print(f"Zomato Ratings:  {zomato_ratings}")
print(f"Swiggy Ratings:  {swiggy_ratings}")
print(f"Combined (10):   {combined_ratings}")
print("\n" + "=" * 60 + "\n")

# ==========================================
# TASK 2: Instagram Likes (np.vstack())
# ==========================================
print("--- TASK 2: Vertical Stacking (Instagram Likes) ---")
post1 = np.array([120, 150, 130, 200, 180, 220, 250])
post2 = np.array([90, 110, 105, 130, 140, 160, 175])
post3 = np.array([200, 210, 230, 250, 280, 300, 320])

stacked_posts = np.vstack((post1, post2, post3))

print("Post 1 Weekly Likes:", post1)
print("Post 2 Weekly Likes:", post2)
print("Post 3 Weekly Likes:", post3)
print("Stacked Array (Posts x Days):\n", stacked_posts)
print("\n" + "=" * 60 + "\n")

# ==========================================
# TASK 3: Flipkart Product IDs (np.array_split())
# ==========================================
print("--- TASK 3: Splitting Product IDs ---")
product_ids = np.arange(101, 113)

split_parts = np.array_split(product_ids, 5)

print(f"Original Product IDs: {product_ids}")
print("Divided into 5 parts:")
for i, part in enumerate(split_parts):
    print(f"  Part {i+1}: {part} (Shape: {part.shape})")
print("\n" + "=" * 60 + "\n")

# ==========================================
# TASK 4: WhatsApp Chat (np.insert() & np.delete())
# ==========================================
print("--- TASK 4: WhatsApp Group Chat Manipulation ---")
whatsapp_chats = np.array([
    [10, 15, 20, 25, 30, 35, 40],  # User 1
    [5,  8,  12, 15, 18, 22, 25],   # User 2
    [50, 45, 40, 35, 30, 25, 20]   # User 3
])

print("Original Chat Data (3 Users):\n", whatsapp_chats)

new_user = np.array([[12, 14, 16, 18, 20, 22, 24]])
whatsapp_with_new = np.insert(whatsapp_chats, whatsapp_chats.shape[0], new_user, axis=0)
print("\nAfter Adding New User (4 Users):\n", whatsapp_with_new)

total_messages_per_user = np.sum(whatsapp_with_new, axis=1)
min_user_index = np.argmin(total_messages_per_user)

whatsapp_cleaned = np.delete(whatsapp_with_new, min_user_index, axis=0)
print(f"\nTotal messages per user: {total_messages_per_user}")
print(f"Removing user at index {min_user_index} (who sent the least messages).")
print("Final Chat Data after Deletion:\n", whatsapp_cleaned)
print("\n" + "=" * 60 + "\n")

# ==========================================
# TASK 5: YouTube Views (.view() vs .copy())
# ==========================================
print("--- TASK 5: View vs Copy (.view() and .copy()) ---")
yt_views = np.array([1000, 2500, 4000, 1500, 3000])

yt_view_obj = yt_views.view()
yt_copy_obj = yt_views.copy()

yt_view_obj[0] = 9999
yt_copy_obj[1] = 8888

print("Original Array after modifications:", yt_views)
print("View Array (modified 1st element):   ", yt_view_obj)
print("Copy Array (modified 2nd element):   ", yt_copy_obj)
print("=" * 60)