# Rewrite each function to use only one line of code

movies = ["Alien", "Barbie", "Clue", "Frozen", "Inception"]
ratings = [7.3, 8.5, 7.2, 7.4, 8.5, 3.3, 1.5]

#> Function 1
def total_squares(n):
    result = 0
    for i in range(n):
        s = i ** 2
        result += s
    
    return result

def total_squares_oneline(n):
    return sum([i ** 2 for i in range(n)])

print(total_squares(4))
print(total_squares_oneline(4))

print()

#> Function 2
def average(numbers):
    total = 0
    count = 0
    for x in numbers:
        total += x
        count += 1
    
    return total / count

def average_oneline(numbers):
    return (sum(numbers) / len(numbers))

print(average([1, 2, 3]))
print(average_oneline([1, 2, 3]))

print()

#> Function 3
def get_sample(samples, t):
    if t < 0:
        return samples[0]
    elif t >= len(samples):
        return samples[-1]
    else:
        return samples[t]

def get_samples_oneline(samples, t):
    return samples[max(min(t, len(samples) - 1), 0)]

print(get_sample([1, 2, 3, 4, 5], 3))
print(get_samples_oneline([1, 2, 3, 4, 5], 3))

print()

#> Function 4
def best_movie(movies, ratings):
    best_rating = ratings[0]
    for rating in ratings:
        if rating > best_rating:
            best_rating = rating
    
    best_movie = movies[0]
    for i in range(len(movies)):
        if ratings[i] == best_rating:
            best_movie = movies[i]
    
    return best_movie

def best_movie_oneline(movies, ratings):
    return movies[[i for i, x in enumerate(ratings) if x == max(ratings)][-1]]

print(best_movie(movies, ratings))
print(best_movie_oneline(movies, ratings))

print()

#> Function 5
def nonnegative(numbers):
    """
    Given a list of numbers, return True if and only
    if all the numbers are nonnegative
    """
    sofar = True
    for x in numbers:
        if x < 0:
            sofar = False
    return sofar

def nonnegative_oneline(numbers):
    return len([1 for number in numbers if number >= 0]) == len(numbers)

print(nonnegative([1, 2, 3, 4, 5]))
print(nonnegative_oneline([1, 2, 3, 4, 5]))
print(nonnegative([-1, 2, 3, 4, 5]))
print(nonnegative_oneline([-1, 2, 3, 4, 5]))

print()

#> Function 6
def nondecreasing(numbers):
    """
    Given a list of numbers, return True if and only
    if the numbers are in nondecreasing order
    """
    sofar = True
    for i in range(len(numbers) - 1):
        if numbers[i + 1] <= numbers[i]:
            sofar = False
    return sofar

def nondecreasing_oneline(numbers):
    return numbers == sorted(numbers)

print(nondecreasing([1, 2, 3, 4, 5]))
print(nondecreasing_oneline([1, 2, 3, 4, 5]))
print(nondecreasing([5, 4, 3, 2, 1]))
print(nondecreasing_oneline([5, 4, 3, 2, 1]))

print()

#> Function 7
def above_threshold(numbers, thresh_val):
    """
    Given a list of numbers, return True if and
    only if at least one of the
    numbers is >= thresh_val
    """
    sofar = False
    for num in numbers:
        if num >= thresh_val:
            sofar = True
    return sofar

def above_threshold_oneline(numbers, thresh_val):
    return len([1 for number in numbers if number >= thresh_val]) > 0

print(above_threshold([1, 2, 3, 4, 5], 4))
print(above_threshold_oneline([1, 2, 3, 4, 5], 4))
print(above_threshold([1, 2, 3, 4, 5], 6))
print(above_threshold_oneline([1, 2, 3, 4, 5], 6))