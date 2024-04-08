# Several ways to represent sounds in Python


# 1. As a dictionary, with keys:
#   rate: int, the sampling rate, in samples per second
#   samples: a list of floats, the samples
sound = {"rate": 8000, "samples": [1, 2, 3]}

print(sound["rate"])
print(sound["samples"])
print()


# 2. As a list with elements:
#   First: the rate
#   Second: a sublist containing the samples
sound = [8000, [1, 2, 3]]

print(sound[0])
print(sound[1])
print()


# 3. As a list with elements:
#   First: the rate
#   Second: remaining elements are the samples
sound = [8000, 1, 2, 3]

print(sound[0])
print(sound[1: ])