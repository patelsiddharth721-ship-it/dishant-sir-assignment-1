import sys
import time
import numpy as np


def list_vs_array_memory():
  # Task 1 & 2: Create list and numpy array with numbers from 1 to 1000
  py_list = list(range(1, 1001))
  np_array = np.arange(1, 1001)

  # Measure memory usage in bytes
  list_memory = sys.getsizeof(py_list) + sum(
      sys.getsizeof(i) for i in py_list
  )  # total memory including pointers and elements in list
  list_memory_basic = sys.getsizeof(
      py_list
  )  # container size (though elements are references)
  array_memory = np_array.nbytes

  print("--- Task 2: Memory Usage ---")
  print(f"Python List container size: {sys.getsizeof(py_list)} bytes")
  print(
      "NumPy Array (nbytes - raw data):"
      f" {np_array.nbytes} bytes (total allocated: {np_array.nbytes})"
  )
  print("-" * 30)


# Task 3: Compare addition speed for 10,000 integers
def compare_addition_speed():
  size = 10000
  py_list = list(range(1, size + 1))
  np_array = np.arange(1, size + 1)

  # Time Python List addition using list comprehension
  start_time = time.perf_counter()
  list_result = [x + 5 for x in py_list]
  end_time = time.perf_counter()
  list_duration = end_time - start_time

  # Time NumPy Array addition using vectorization
  start_time = time.perf_counter()
  array_result = np_array + 5
  end_time = time.perf_counter()
  array_duration = end_time - start_time

  print("--- Task 3: Addition Speed Comparison (10,000 integers) ---")
  print(f"Python List time: {list_duration:.6f} seconds")
  print(f"NumPy Array time: {array_duration:.6f} seconds")
  print("-" * 30)


# Task 4: Zomato-style example (Vectorized operations vs For-loops)
def zomato_rating_example():
  # Example restaurant ratings on Zomato
  ratings_list = [4.2, 3.8, 4.5, 3.9, 4.7]
  ratings_array = np.array([4.2, 3.8, 4.5, 3.9, 4.7])

  print("--- Task 4: Zomato-style Example ---")
  print(f"Original Ratings: {ratings_array}")

  # 1. Using a For-Loop (Python list approach)
  doubled_list = []
  for rating in ratings_list:
    doubled_list.append(rating * 2)
  print(f"Using For-Loop (List): {doubled_list}")

  # 2. Using Vectorization (NumPy approach - replacing for-loops)
  doubled_array = ratings_array * 2
  print(f"Using Vectorization (NumPy): {doubled_array}")
  print("-" * 30)


if __name__ == "__main__":
  list_vs_array_memory()
  compare_addition_speed()
  zomato_rating_example()