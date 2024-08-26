# Ordered timesteps of a game called "Free Food Bonanza"

#> A. Find duplicate game boards
#>   1 & 3
#>   Others are also duplicates if we exclude the F tile


#> B. Boards that are reachable from other boards
#>   1 -> 2, 1 -> 3, 1 -> 4
#>   2 -> 1, 2 -> 3
#>   3 -> 1, 3 -> 2, 3 -> 4
#>   4 -> 1, 4 -> 3, 4 -> 5
#>   5 -> 4, 5 -> 6
#>   6 -> 5, 6 -> 7
#>   7 -> 6, 7 -> 8
#>   8 -> 7, 8 -> 9
#>   9 -> 8, 9 -> 10


#> C. What timestep is the game supposed to end?
#>   Timestamp 6 when the F tile is collected


#> D. What is the minimum number of moves if starting on timestep 1?
#>   1 -> 4 -> 5 -> 6 (3 moves)