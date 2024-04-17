# Different kernel representations

#> 1. Image Dictionary Kernel: set up like an image, but indexing rows and cols may be difficult
kernel = {
    "height": 3,
    "width": 3,
    "pixels": [0, 0, 0, 0, 0, 0, 0, 1, 0]
}


#> 2. Flat-List Kernel: just a list, it must be assumed that the kernel has same height and width
kernel = [0, 0, 0, 0, 0, 0, 0, 1, 0]


#> 3. Nested-List Kernel: clearly shows rows and cols, but may need to flatten depending on image representation
kernel = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 1, 0]
]

#> 4. Image Coordinate Offets to Kernel Value Dictionary: probably the most flexible, yet also most complex, representation
#>      Keys are (row, col) tuples for corresponding kernel value
#>      Kernel is centered at (0, 0)
kernel = {
    (-1, -1): 0, (-1,  0): 0, (-1,  1): 0,
    ( 0, -1): 1, ( 0,  0): 0, ( 0,  1): 0,
    (1 , -1): 0, ( 1,  0): 0, ( 1,  1): 0,
}