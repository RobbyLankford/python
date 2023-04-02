# Problem Set 4A

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    perms = []
    
    #> Base Case 1: a single-letter sequence
    if len(sequence) == 1:
        return [sequence]
    
    #> Base Case 2: a double-letter sequence, just reverse it
    elif len(sequence) == 2:
        forwards = [sequence[0], sequence[1]]
        backwards = [sequence[1], sequence[0]]
        
        return [''.join(forwards), ''.join(backwards)]
    
    #> All other cases
    else:
        for letter in sequence:
            ##> Hold out each letter, one at a time, and permute the remaining letters
            subset = sequence.replace(letter, '', 1)
            recursive = get_permutations(subset)
            
            ##> Place held-out letter at the start and append each permutation
            for seq in recursive:
                perms.append(''.join([letter, seq]))
        
        unique = list(set(perms))
        
        return sorted(unique)

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)
    example_input = 'a'
    print(f"Input: {example_input}")
    print("Expected Output: ['a']")
    print(f"Actual Output: {get_permutations(example_input)}")
    print("----------")
    
    example_input = 'ab'
    print(f"Input: {example_input}")
    print("Expected Output: ['ab', 'ba']")
    print(f"Actual Output: {get_permutations(example_input)}")
    print("----------")
    
    example_input = 'abb'
    print(f"Input: {example_input}")
    print("Expected Output: ['abb', 'bab', 'bba']")
    print(f"Actual Output: {get_permutations(example_input)}")
    print("----------")
    
    example_input = 'abc'
    print(f"Input: {example_input}")
    print("Expected Output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']")
    print(f"Actual Output: {get_permutations(example_input)}")
    print("----------")
    
    example_input = 'aaa'
    print(f"Input: {example_input}")
    print("Expected Output: ['aaa']")
    print(f"Actual Output: {get_permutations(example_input)}")
