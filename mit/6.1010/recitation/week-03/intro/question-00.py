# Creates a large order list and a large set
# Times how long it takes to find the 1,000 largest numbers in both

import time

big_num = 10_000_000
big_num_list = list(range(big_num))
big_num_set = set(big_num_list)

small_num = 1_000
small_num_list = list(range(big_num - small_num, big_num))

# First Run (using a set)
start = time.time()
count = 0
print("Counting 1000 largest numbers in a set...")

for i in small_num_list:
    count += i in big_num_set

end = time.time()
print("Count using set:", count, "\ntime:", end - start, "seconds.")

print()

start = time.time()
count = 0
print("Counting last 1000 numbers in a list...")

for i in small_num_list:
    count += i in big_num_list

end = time.time()

print("Count using list:", count, "\ntime:", end - start, "seconds.")