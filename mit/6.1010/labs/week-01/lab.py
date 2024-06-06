#!/usr/bin/env python3

"""
6.101 Lab:
Image Processing
"""

import math
from PIL import Image

# Imported for type hinting only
from typing import TypedDict, Callable

# NO ADDITIONAL IMPORTS ALLOWED!

class GreyScaleImage(TypedDict):
    height: int
    width: int
    pixels: list[int]

class Kernel(TypedDict):
    height: int
    width: int
    pixels: list[int]

HEIGHT, WIDTH, PIXELS = "height", "width", "pixels"

def get_width(image: GreyScaleImage) -> int:
    """
    Gets width of an image

    Args:
        image (GreyScaleImage): an image

    Returns:
        int: the width of the image
    """
    return image[WIDTH]

def get_height(image: GreyScaleImage) -> int:
    """
    Gets height of an image

    Args:
        image (GreyScaleImage): an image

    Returns:
        int: the height of the image
    """
    return image[HEIGHT]

def get_pixels(image: GreyScaleImage) -> list[int]:
    """
    Gets the pixels of an image

    Args:
        image (GreyScaleImage): an image

    Returns:
        list[int]: a list of pixels as integers [0, 255]
    """
    return image[PIXELS]

def get_index(image: GreyScaleImage, row: int, col: int) -> int:
    """
    Gets the index of particular pixel and a row and column location.
    The pixels are stored as a 1D list that represents a 2D matrix.

    Args:
        image (GreyScaleImage): an image
        row (int): the row index of the pixel
        col (int): the column index of the pixel

    Returns:
        int: the index of the 1D list that matches the 2D row and column
    """
    return row * get_width(image) + col

def get_pixel(image: GreyScaleImage, row: int, col: int) -> int:
    """
    Gets the pixel at a particular row and column location.
    The pixels are stored as a 1D list that represents a 2D matrix.

    Args:
        image (GreyScaleImage): an image
        row (int): the row index of the pixel
        col (int): the column index of the pixel

    Returns:
        int: the desired pixel value
    """
    pix = get_pixels(image)
    
    return pix[get_index(image, row, col)]

def set_pixel(image: GreyScaleImage, row: int, col: int, color: int) -> None:
    """
    Sets the pixel at a particular row and column location to a value

    Args:
        image (GreyScaleImage): an image
        row (int): the row of index of the pixel
        col (int): the column index of the pixel
        color (int): the value (0-255) to which to set the pixel
    """
    pix = get_pixels(image)
    
    pix[get_index(image, row, col)] = color

def blank_image(image: GreyScaleImage) -> GreyScaleImage:
    """
    Create a new image of the same shape that has all pixels set to zero

    Args:
        image (GreyScaleImage): an image

    Returns:
        GreyScaleImage: an image with all pixel values set to zero
    """
    nrow, ncol = get_height(image), get_width(image)
    
    return {HEIGHT: nrow, WIDTH: ncol, PIXELS: [0] * nrow * ncol}

def apply_per_pixel(image: GreyScaleImage, func: Callable) -> GreyScaleImage:
    """
    Apply a function to each pixel in an image

    Args:
        image (GreyScaleImage): an image
        func (Callable): a function that takes in one integer and returns another integer

    Returns:
        GreyScaleImage: an image with updated pixels
    """
    result = blank_image(image)
    
    for col in range(get_width(image)):
        for row in range(get_height(image)):
            color = get_pixel(image, row, col)
            new_color = func(color)
            set_pixel(result, row, col, new_color)
    
    return result

def inverted(image: GreyScaleImage) -> GreyScaleImage:
    """
    Invert all pixels of an image

    Args:
        image (GreyScaleImage): an image

    Returns:
        GreyScaleImage: the same image, but inverted
    """
    return apply_per_pixel(image, lambda color: abs(255 - color))

# HELPER FUNCTIONS

def list_to_2d_array(lst: list[int], nrow: int, ncol: int) -> list[int]:
    """
    Convert a 1D list to a 2D array

    Args:
        lst (list[int]): the original 1D list of integers
        nrow (int): the number of rows for the 2D array to have
        ncol (int): the number of columns for the 2D array to have

    Returns:
        list[int]: a 2D array represented as a nested list of lists
    """
    assert len(lst) == nrow * ncol, 'Invalid `nrow` or `ncol` arguments.'
    
    return [lst[(row * ncol):(row * ncol + ncol)] for row in range(nrow)]

def list_from_2d_array(array: list[int]) -> list[int]:
    """
    Convert a 2D array to a 1D list

    Args:
        array (list[int]): the original 2D array represented as a nested list of lists

    Returns:
        list[int]: a 1D list
    """
    assert len(array) == len(array[0]), 'Matrix must be square, with equal rows and columns.'
    
    return [item for row in array for item in row]

def image_to_2d_array(image: GreyScaleImage) -> GreyScaleImage:
    """
    Convert the pixels in an image from a 1D list to a 2D array

    Args:
        image (GreyScaleImage): an image with pixels represented as a 1D list

    Returns:
        GreyScaleImage: the same image with the pixels represented as a 2D array (a list of lists)
    """
    nrow, ncol, pix = get_height(image), get_width(image), get_pixels(image)
    
    pixels = list_to_2d_array(pix, nrow, ncol)
    
    return {HEIGHT: nrow, WIDTH: ncol, PIXELS: pixels}

def image_from_2d_array(array: list[int]) -> GreyScaleImage:
    """
    Create an image from pixels represented as a 2D array

    Args:
        array (list[int]): a 2D array represented as a nested list of lists

    Returns:
        GreyScaleImage: the resulting image after converting the 2D array to a 1D list
    """
    pixels = list_from_2d_array(array)
    
    return {HEIGHT: len(array), WIDTH: len(array[0]), PIXELS: pixels} 

def boundary_behavior_zero(row: int, col: int, nrow: int, ncol: int, image: GreyScaleImage) -> int:
    """
    Extract pixel color for specific row and column indices using "zero" boundary behavior.
    That is, if the indices are out of bounds, return a color value of 0.

    Args:
        row (int): the pixel's row index
        col (int): the pixel's column index
        nrow (int): the number of rows in the image
        ncol (int): the number of columns in the image
        image (GreyScaleImage): the image

    Returns:
        int: the value of the color at the pixel
    """
    if row <= nrow - 1 and row >= 0 and col <= ncol - 1 and col >= 0:
        return get_pixel(image, row, col)
    
    return 0

def boundary_behavior_extend(row: int, col: int, nrow: int, ncol: int, image: GreyScaleImage) -> int:
    """
    Extract pixel color for specific row and column indicies using "extend" boundary behavior.
    That is, if the indices are out of bounds, use the value of the pixel right before going out of bounds.

    Args:
        row (int): the pixel's row index
        col (int): the pixel's column index
        nrow (int): the number of rows in the image
        ncol (int): the number of columns in the image
        image (GreyScaleImage): the image

    Returns:
        int: the value of the color at the pixel
    """
    row_idx = min(max(row, 0), nrow - 1)
    col_idx = min(max(col, 0), ncol - 1)
    
    return get_pixel(image, row_idx, col_idx)

def boundary_behavior_wrap(row: int, col: int, nrow: int, ncol: int, image: GreyScaleImage) -> int:
    """
    Extract pixel color for specific row and column indicies using "wrap" boundary behavior.
    That is, if the indices are out of bounds, wrap around to the other side of the image to get back in bounds.

    Args:
        row (int): the pixel's row index
        col (int): the pixel's column index
        nrow (int): the number of rows in the image
        ncol (int): the number of columns in the image
        image (GreyScaleImage): the image

    Returns:
        int: the value of the color at the pixel
    """
    while row < 0:
        row += nrow
    while row > 0:
        row -= nrow
    
    while col < 0:
        col += ncol
    while col > 0:
        col -= ncol
    
    return get_pixel(image, row, col)

def correlate(image: GreyScaleImage, kernel: Kernel, boundary_behavior: str) -> GreyScaleImage:
    """
    Compute the result of correlating the given image with the given kernel.
    `boundary_behavior` will one of the strings "zero", "extend", or "wrap",
    and this function will treat out-of-bounds pixels as having the value zero,
    the value of the nearest edge, or the value wrapped around the other edge
    of the image, respectively.

    if boundary_behavior is not one of "zero", "extend", or "wrap", return
    None.

    Otherwise, the output of this function should have the same form as a 6.101
    image (a dictionary with "height", "width", and "pixels" keys), but its
    pixel values do not necessarily need to be in the range [0,255], nor do
    they need to be integers (they should not be clipped or rounded at all).

    This process should not mutate the input image; rather, it should create a
    separate structure to represent the output.

    The kernel representation is the same as the image representation. The kernel is a
    dictionary with keys 'height', 'width', and 'pixels'. The height and width are
    integers dictating the height and width of the kernel in number of pixels. The pixels
    are the individual weights of the kernels represented as a 1D list.
    
    Args:
        image (GreyScaleImage): the image to be correlated
        kernel (Kernel): the kernel representation
        boundary_behavior (str): the boundary behavior to use, one of 'zero', 'extend', or 'wrap'

    Returns:
        GreyScaleImage: the image with the kernel applied
    """
    boundary_funcs = {
        'zero': boundary_behavior_zero, 
        'extend': boundary_behavior_extend,
        'wrap': boundary_behavior_wrap
    }
    
    if boundary_behavior not in boundary_funcs.keys():
        print("Argument boundary_behavior must be one of 'zero', 'extend', or 'wrap'.")
        
        return None
    
    boundary_func = boundary_funcs.get(boundary_behavior)
    
    nrow, ncol = get_height(image), get_width(image)
    offset_row = int((get_height(kernel) - 1) / 2)
    offset_col = int((get_width(kernel) - 1) / 2)
    
    subsets = []
    for row in range(nrow):
        for col in range(ncol):
            
            subset = []
            for r in range(row - offset_row, row + offset_row + 1):
                for c in range(col - offset_col, col + offset_col + 1):
                    subset.append(boundary_func(r, c, nrow, ncol, image))
            
            subsets.append(subset)
    
    correlations = []
    for subset in subsets:
        correlations.append(sum([p * k for p,k in zip(subset, get_pixels(kernel))]))
    
    new_image = {HEIGHT: nrow, WIDTH: ncol, PIXELS: correlations}
    
    return new_image

def round_and_clip_image(image: GreyScaleImage) -> GreyScaleImage:
    """
    Given a dictionary, ensure that the values in the "pixels" list are all
    integers in the range [0, 255].

    All values should be converted to integers using Python's `round` function.

    Any locations with values higher than 255 in the input should have value
    255 in the output; and any locations with values lower than 0 in the input
    should have value 0 in the output.
    
    Args:
        image (GreyScaleImage): an image that may or may not have valid pixel values

    Returns:
        GreyScaleImage: an image with valid pixel values
    """
    return apply_per_pixel(image, lambda pixel: max(0, min(255, round(pixel))))


# FILTERS

def make_box_blur_kernel(n: int) -> Kernel:
    """Creat a box blur kernel

    Args:
        n (int): the size of the kernel (the kernel will have n x n pixels)

    Returns:
        Kernel: a kernel representation
    """
    weight = 1.0 / (n * n)
    weights = [weight for _ in range(n * n)]
    
    return {HEIGHT: n, WIDTH: n, PIXELS: weights}

def blurred(image: GreyScaleImage, kernel_size: int, boundary_behavior: str = 'extend') -> GreyScaleImage:
    """
    Return a new image representing the result of applying a box blur (with the
    given kernel size) to the given input image.

    This process should not mutate the input image; rather, it should create a
    separate structure to represent the output.
    
    Args:
        image (GreyScaleImage): the image
        n (int): the size of the kernel (the kernel will be n x n pixels)
        boundary_behavior (str, optional): the type of boundary behavior to apply. Defaults to 'extend'.

    Returns:
        GreyScaleImage: the new image after applying the unsharp mask
    """
    kernel = make_box_blur_kernel(n=kernel_size)
    corr = correlate(image, kernel, boundary_behavior=boundary_behavior)
    
    return round_and_clip_image(corr)

def sharpened(image: GreyScaleImage, n: int) -> GreyScaleImage:
    """
    Return a new image representing the result of applying an unsharp mask (with the
    given kernel size) to the given input image.

    Args:
        image (GreyScaleImage): the image
        n (int): the size of the kernel (the kernel will be n x n pixels)

    Returns:
        GreyScaleImage: the new image after applying the unsharp mask
    """
    blurred_image = blurred(image, kernel_size=n, boundary_behavior='extend')
    old_pixels = [pixel for pixel in get_pixels(image)]
    blurred_pixels = [pixel for pixel in get_pixels(blurred_image)]
    
    new_pixels = [(2 * img_pixel) - blur_pixel for img_pixel, blur_pixel in zip(old_pixels, blurred_pixels)]
    new_image = {HEIGHT: get_height(image), WIDTH: get_width(image), PIXELS: new_pixels}
    
    return round_and_clip_image(new_image)

def edges(image: GreyScaleImage) -> GreyScaleImage:
    """
    Return a new image representing the result of applying a Sobel operator to detect edges

    Args:
        image (GreyScaleImage): an image

    Returns:
        GreyScaleImage: a new image highlighting the edges of objects in the original image
    """
    kern_1 = {HEIGHT: 3, WIDTH: 3, PIXELS: [-1, 0, 1, -2, 0, 2, -1, 0, 1]}
    kern_2 = {HEIGHT: 3, WIDTH: 3, PIXELS: [-1, -2, -1, 0, 0, 0, 1, 2, 1]}
    
    O1 = correlate(image, kern_1, boundary_behavior='extend')
    O2 = correlate(image, kern_2, boundary_behavior='extend')
    
    pix_O1 = get_pixels(O1)
    pix_02 = get_pixels(O2)
    pix_edges = [round(math.sqrt(math.pow(x, 2) + math.pow(y, 2))) for x,y in zip(pix_O1, pix_02)]
    
    edge_img = {HEIGHT: get_height(image), WIDTH: get_width(image), PIXELS: pix_edges}
    
    return round_and_clip_image(edge_img)


# HELPER FUNCTIONS FOR LOADING AND SAVING IMAGES

def load_greyscale_image(filename):
    """
    Loads an image from the given file and returns a dictionary
    representing that image.  This also performs conversion to greyscale.

    Invoked as, for example:
       i = load_greyscale_image("test_images/cat.png")
    """
    with open(filename, "rb") as img_handle:
        img = Image.open(img_handle)
        img_data = img.getdata()
        if img.mode.startswith("RGB"):
            pixels = [round(.299 * p[0] + .587 * p[1] + .114 * p[2])
                      for p in img_data]
        elif img.mode == "LA":
            pixels = [p[0] for p in img_data]
        elif img.mode == "L":
            pixels = list(img_data)
        else:
            raise ValueError(f"Unsupported image mode: {img.mode}")
        width, height = img.size
        return {"height": height, "width": width, "pixels": pixels}


def save_greyscale_image(image, filename, mode="PNG"):
    """
    Saves the given image to disk or to a file-like object.  If filename is
    given as a string, the file type will be inferred from the given name.  If
    filename is given as a file-like object, the file type will be determined
    by the "mode" parameter.
    """
    out = Image.new(mode="L", size=(image["width"], image["height"]))
    out.putdata(image["pixels"])
    if isinstance(filename, str):
        out.save(filename)
    else:
        out.save(filename, mode)
    out.close()


if __name__ == "__main__":
    # code in this block will only be run when you explicitly run your script,
    # and not when the tests are being run.  this is a good place for
    # generating images, etc.
    
    # # 3. Image Filtering via Per-Pixel Transformations
    # bluegill = load_greyscale_image('test_images/bluegill.png')
    # bluegill_inverted = inverted(bluegill)
    
    # save_greyscale_image(bluegill_inverted, 'bluegill-inverted.png')
    
    # # 4. Image Filtering via Correlation
    # kernel = {
    #     HEIGHT: 13, 
    #     WIDTH: 13, 
    #     PIXELS: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    #              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    #              1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    #              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    #              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    #              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    #              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    #              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    #              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    #              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    #              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    #              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    #              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # }
    
    # pig_bird = load_greyscale_image('test_images/pigbird.png')
    # pig_bird_zero = correlate(pig_bird, kernel, boundary_behavior='zero')
    # pig_bird_extend = correlate(pig_bird, kernel, boundary_behavior='extend')
    # pig_bird_wrap = correlate(pig_bird, kernel, boundary_behavior='wrap')
    
    # save_greyscale_image(pig_bird_zero, 'pig_bird_zero.png')
    # save_greyscale_image(pig_bird_extend, 'pig_bird_extend.png')
    # save_greyscale_image(pig_bird_wrap, 'pig_bird_wrap.png')
    
    # # 5. Blurring and Sharpening
    
    # ## 5.1 Blurring
    # cat = load_greyscale_image('test_images/cat.png')
    
    # cat_blurred = blurred(cat, kernel_size=13)
    # cat_blurred_zero = blurred(cat, kernel_size=13, boundary_behavior='zero')
    # cat_blurred_wrap = blurred(cat, kernel_size=13, boundary_behavior='wrap')
    
    # save_greyscale_image(cat_blurred, 'cat_blurred.png')
    # save_greyscale_image(cat_blurred_zero, 'cat_blurred_zero.png')
    # save_greyscale_image(cat_blurred_wrap, 'cat_blurred_wrap.png')
    
    # ## 5.2 Sharpening
    # python = load_greyscale_image('test_images/python.png')
    # python_sharp = sharpened(python, n=11)
    
    # save_greyscale_image(python_sharp, 'python_sharpened.png')
    
    # 6. Edge Detection
    
    construct = load_greyscale_image('test_images/construct.png')
    construct_edges = edges(construct)
    
    save_greyscale_image(construct_edges, 'construct-edges.png')
    
    im = load_greyscale_image('test_images/centered_pixel.png')
    im_edges = edges(im)
    
    save_greyscale_image(im_edges, 'centered_pixel_edges.png')