# Rewrite code examples to make them more pythonic

movies = ["Alien", "Barbie", "Clue", "Frozen", "Inception"]
ratings = [8.5, 7.3, 7.2, 7.4, 8.8, 3.3, 1.5]

#> Example A:
def exampleA():
    for i in [0, 1, 2, 3, 4, 5]:
        print(i ** 2)

def exampleA_():
    for i in range(6):
        print(i ** 2)

exampleA()
print()
exampleA_()

print()
print()
print()

#> Example B:
def exampleB():
    i = 0
    while i < len(movies):
        print(movies[i])
        i += 1

def exampleB_():
    for movie in movies:
        print(movie)

exampleB()
print()
exampleB_()

print()
print()
print()

#> Example C:
def exampleC():
    for i in range(len(movies) - 1, -1, -1):
        print(movies[i])

def exampleC_():
    for movie in reversed(movies):
        print(movie)

exampleC()
print()
exampleC_()

print()
print()
print()

#> Example D:
def exampleD():
    for i in range(len(movies)):
        print(i, movies[i])

def exampleD_():
    for i, movie in enumerate(movies):
        print(i, movie)

exampleD()
print()
exampleD_()

print()
print()
print()

#> Example E:
def exampleE():
    n = min(len(movies), len(ratings))
    for i in range(n):
        print(movies[i], ratings[i])

def exampleE_():
    for movie, rating in zip(movies, ratings):
        print(movie, rating)

exampleE()
print()
exampleE_()