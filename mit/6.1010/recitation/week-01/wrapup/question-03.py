# Given an implementation of get_pixel()... how to refactor it to reduce repetition and simplify?

def get_pixel1(image, row, col, boundary_behavior):
    if boundary_behavior == 'zero':
        if row < 0 and col < 0:
            return 0
        elif row < 0 and col <= image['width'] - 1:
            return 0
        elif row < 0 and col > image['width'] - 1:
            return 0
        elif row <= image['height'] - 1 and col < 0:
            return 0
        elif row <= image['height'] - 1 and col <= image['width'] - 1:
            return image['pixels'][row * image['width'] + col]
        elif row <= image['height'] - 1 and col > image['width'] - 1:
            return 0
        elif row > image['height'] - 1 and col < 0:
            return 0
        elif row > image['height'] - 1 and col <= image['width'] - 1:
            return 0
        elif row > image['height'] - 1 and col > image['width'] - 1:
            return 0

    elif boundary_behavior == 'extend':
        if row < 0 and col < 0:
            return image['pixels'][0 * image['width'] + 0]
        elif row < 0 and col <= image['width'] - 1:
            return image['pixels'][0 * image['width'] + col]
        elif row < 0 and col > image['width'] - 1:
            return image['pixels'][0 * image['width'] + (image['width']-1)]
        elif row <= image['height'] - 1 and col < 0:
            return image['pixels'][row * image['width'] + 0]
        elif row <= image['height'] - 1 and col <= image['width'] - 1:
            return image['pixels'][row * image['width'] + col]
        elif row <= image['height'] - 1 and col > image['width'] - 1:
            return image['pixels'][row * image['width'] + (image['width'] - 1)]
        elif row > image['height'] - 1 and col < 0:
            return image['pixels'][(image['height'] - 1) * image['width'] + 0]
        elif row > image['height'] - 1 and col <= image['width'] - 1:
            return image['pixels'][(image['height'] - 1) * image['width'] + col]
        elif row > image['height'] - 1 and col > image['width'] - 1:
            return image['pixels'][(image['height'] - 1) * image['width'] + (image['width'] - 1)]
        
    elif boundary_behavior == 'wrap':
        while row < 0:
            row += image['height']
        while row > 0:
            row -= image['height']
        while col < 0:
            col += image['width']
        while col > 0:
            col -= image['width']
        
        return image['pixels'][row * image['width'] + col]
    

# Refactor using helper functions and combining if/else statements

def boundary_behavior_zero(row, col, nrow, ncol, image):
    #> Easier to check first for any valid row/col combination
    if row <= nrow - 1 and row >= 0 and col <= ncol - 1 and col >= 0:
        return image['pixels'][row * ncol + col]
    
    #> Every other row/col combination should be invalid
    return 0


def boundary_behavior_extend(row, col, nrow, ncol, image):
    #> Indexing into the image is always: row_idx * ncol + col_idx
    
    #> Determine row index
    row_idx = min(max(row, 0), nrow - 1)
        
    #> Determine col index
    col_idx = min(max(col, 0), ncol - 1)
    
    return image['pixels'][row_idx * ncol + col_idx]


def boundary_behavior_wrap(row, col, nrow, ncol, image):
    #> Pre-existing implementation is actually not that bad, so just reuse it
    while row < 0:
        row += nrow
    while row > 0:
        row -= nrow
    
    while col < 0:
        col += ncol
    while col > 0:
        col -= ncol
    
    return image['pixels'][row * ncol + col]


def get_pixel2(image, row, col, boundary_behavior):
    nrow = image['height']
    ncol = image['width']
    
    if boundary_behavior == 'zero':
        boundary_behavior_zero(row, col, nrow, ncol, image)
    elif boundary_behavior == 'extend':
        boundary_behavior_extend(row, col, nrow, ncol, image)
    elif boundary_behavior == 'wrap':
        boundary_behavior_wrap(row, col, nrow, ncol, image)
    else:
        print('Invalid boundary behavior')
        return False