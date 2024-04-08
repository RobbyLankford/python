# #> Function given that is buggy
# def subtract_lists(nums1, nums2):
#     """
#     Given lists of numbers nums1 and nums2, return a new list where each
#     position is the difference between that position in nums1 and in nums2.
#     """
#     output = []
    
#     for i in range(len(lst1)):
#         output.append(lst1[i] - lst2[i])
    
#     return output


#> Rewrite function
def subtract_lists(nums1, nums2):
    """
    Given lists of numbers nums1 and nums2, return a new list where each
    position is the difference between that position in nums1 and in nums2.
    """
    return [x - y for x, y in zip(nums1, nums2)]


#> Test case(s)
def test_subtract_lists():
    assert subtract_lists([1, 2], [3, 5]) == [-2, -3]
    assert subtract_lists([325, 64, 66], [1, 2, 3]) == [324, 62, 63]

def test_subtract_length():
    result_1 = subtract_lists([1, 2, 3], [4, 5])
    result_2 = subtract_lists([1, 2], [3, 4, 5])
    
    assert len(result_1) == 2
    assert len(result_2) == 2


#> What happens when nums1 is longer?
print(subtract_lists([1, 2, 3], [4, 5]))


#> What happens when nums2 is longer?
print(subtract_lists([1, 2], [3, 4, 5]))


#> Run test cases
if __name__ == "__main__":
    test_subtract_lists()
    test_subtract_length()
    print("done!")