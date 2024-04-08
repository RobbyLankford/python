# #> Fix the buggy code below
# def sum_lists(lists):
#     """
#     Given a list of lists of numbers, return a new list where each list
#     is replaced by the sum of its elements without modifying the input list.
#     """
#     output = [0] * len(lists)
    
#     for i in range(len(lists)):
#         total = 0
        
#         for i in lists[i]:
#             total += i
        
#         output[i] = total
    
#     return output

def sum_lists(lists):
    """
    Given a list of lists of numbers, return a new list where each list
    is replaced by the sum of its elements without modifying the input list.
    """
    return [sum(item) for item in lists]

inp = [[1, 2, 3], [4, 5, 6, 7], [8, 9, 0]]

print(inp)
print(sum_lists(inp))
print(inp)