###########################
# 6.0002 Problem Set 1a: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    cows_dict = {}
    
    with open(filename, "r") as file:
        for line in file:
            name, weight = line.split(",")
            cows_dict[name] = int(weight)
    
    return cows_dict


# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    out_list = []
    used_list = []
    counter_int = 0
    
    #> Order cows by their weights from greatest to least
    cows_ordered_dict = dict(sorted(cows.items(), reverse=True, key=lambda item: item[1]))
    
    #> While there are still cows available, see if they can be added to the trip
    while counter_int < len(cows_ordered_dict.keys()):
        temp_list = []
        total_weight_int = 0
        
        ##> If adding the next heaviest cow is still under the weight limit, add it and flag it as already being used
        for name, weight in cows_ordered_dict.items():
            if (name not in used_list) and (total_weight_int + weight <= limit):
                temp_list.append(name)
                used_list.append(name)
                
                total_weight_int += weight
                counter_int += 1
                    
        out_list.append(temp_list)

    return out_list


# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    valid_partition_list = []
    
    #> For each combination of trips...
    for partition in get_partitions(cows):
        ##> Want the number of valid trips (total weight less than weight limit) is equal to the number of trips in the partition
        num_trips_int = len(partition)
        valid_trip_int = 0
        
        ##> Check each trip in the list of trips for the partition
        for trip in partition:
            weight_int = 0
            
            for cow in trip:
                weight_int += cows[cow]
            
            ###> If the weight is less than the limit, the trip is valid
            if weight_int <= limit:
                valid_trip_int += 1
        
        ##> If every trip in the partition is valid (less than weight limit) the partition is valid
        if valid_trip_int == num_trips_int:
            valid_partition_list.append(partition)
    
    num_trips_int = len(cows)
    return_list = []
    
    #> Select whichever valid partition contains the fewest number of trips
    for item in valid_partition_list:
        if len(item) < num_trips_int:
            num_trips_int = len(item)
            return_list = item
    
    return return_list

        
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    cows = load_cows("ps1_cow_data.txt")
    
    #> Run and time the greedy algorithm
    start_greedy = time.time()
    greedy_cows_trips_int = len(greedy_cow_transport(cows))
    end_greedy = time.time()
    
    #> Run and time the brute force algorithm
    start_brute = time.time()
    brute_force_cows_trips_int = len(brute_force_cow_transport(cows))
    end_brute = time.time()
    
    print("Greedy Algorithm")
    print("Trip:", greedy_cows_trips_int)
    print("Time (s):", end_greedy - start_greedy)
    print()
    print("Brute Force Algorithm")
    print("Trip:", brute_force_cows_trips_int)
    print("Time (s):", end_brute - start_brute)

compare_cow_transport_algorithms()