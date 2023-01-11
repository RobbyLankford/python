# Packages
from functools import cmp_to_key


# Import Data
with open("day-13.txt", "r") as file:
    packet_pairs = file.read().strip()


# Function
def compare_packets(left, right):
    """Compare left and right packets

    Args:
        left (int or list): the packet on the left
        right (int or list): the packet on the right

    Returns:
        int: 
            -1 if left packet is less than right packet (correct order)
            +1 if left packet is greater than right packet (incorrect order)
            0 if the packets are equal (need to check next part of the packet)
    """
    
    #> Case 1: both values are integers
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return -1
        elif left == right:
            return 0
        else:
            return 1
    
    #> Case 2: left is integer, right is list
    if isinstance(left, int):
        left = [left]
    
    #> Case 3: left is list, right is integer
    if isinstance(right, int):
        right = [right]
    
    #> Recursively check each item in the two packets
    for a, b in zip(left, right):
        result = compare_packets(a, b)
        
        #> If ints are equal, check the next pair in the list
        if result == 0:
            continue
        else:
            return result

    #> Case 4: list lengths are not equal
    if len(left) < len(right):
        return -1
    elif len(left) > len(right):
        return 1
    else:
        return 0


# Question 1
ans1 = 0
for i, packet_pair in enumerate(packet_pairs.split("\n\n")):
    #> Can eval the input since it is in the format of a python list
    left, right = list(map(eval, packet_pair.split('\n')))
    
    #> Packets are in the correct order if result is -1
    if compare_packets(left, right) == -1:
        ans1 += i + 1

print(f"Answer 1: {ans1}")


# Question 2
packets = [eval(packet) for packet in packet_pairs.split("\n") if packet]
packets.extend([[[2]], [[6]]])
packets_sorted = sorted(packets, key=cmp_to_key(compare_packets))

ans2 = 1
for i, packet in enumerate(packets_sorted):
    if packet in [[[2]], [[6]]]:
        ans2 *= i + 1

print(f"Answer 2: {ans2}")