###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

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

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that
       will fit to the trip
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
    c = cows.copy()
    trips = [[]]
    
    def largest(d):
        assert len(d) > 0, 'd is an empty sequence'
        return max(iter(d), key=lambda x: d[x])
    
    def trip_can_fit_cow(trip, cow, trip_limit):
        on_weight = 0
        for on_cow in trip:
            on_weight += cows[on_cow]
        if on_weight >= trip_limit:
            return False
        elif on_weight + cows[cow] > trip_limit:
            return False
        return True 
    
    while len(c) > 0:
        i = 0
        while i < len(trips):
            if trip_can_fit_cow(trips[i], largest(c), limit):
                trips[i].append(largest(c))
                del c[largest(c)]
                i = 0
            else:
                i += 1
            if len(c) == 0:
                break
        if len(c) == 0:
            break
        # 以上两个 len(c) == 0 的判断，可以怎么去掉？
        
        if cows[largest(c)] <= limit:
            trips.append([largest(c)])
            del c[largest(c)]
    return trips 
                            


# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
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
    min_num_trips = []
    for cow in cows:
        min_num_trips.append([cow])
    for test_trips in get_partitions(cows):
        for trip in test_trips:
            on_weight = 0
            for cow in trip:
                on_weight += cows[cow]
            if on_weight > limit:
                break
        else:
            if len(test_trips) < len(min_num_trips):
                min_num_trips = test_trips
    return min_num_trips
        
# Problem 3
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
    greedy_start = time.time()
    greedy_cow_transport(cows, limit)
    greedy_end = time.time()
    print('greedy cow transport made ' + str(len(greedy_cow_transport(cows, limit))) + ' trips.')
    print('greedy cow transport took ' + str(greedy_end-greedy_start) + ' seconds.')
    
    brute_start = time.time()
    brute_force_cow_transport(cows, limit)
    brute_end = time.time()
    print('brute force cow transport made ' + str(len(brute_force_cow_transport(cows, limit))) + ' trips.')
    print('brute force cow transport took ' + str(brute_end-brute_start) + ' seconds.')

"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
#cows = {'Muscles':    65, 
#        'Miss Bella': 15,
#        'Horns':      50, 
#        'Patches':    60,
#        'MooMoo':     85, 
#        'Polaris':    20, 
#        'Milkshake':  75, 
#        'Clover':      5, 
#        'Louis':      45, 
#        'Lotus':      10}
limit=10
#print(cows)

print('greedy result:', greedy_cow_transport(cows, limit))
print('brute result:', brute_force_cow_transport(cows, limit))

compare_cow_transport_algorithms()
