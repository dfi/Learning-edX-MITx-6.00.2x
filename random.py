# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random

def rollDie():
    """returns a random int between 1 and 6"""
    return random.choice([1,2,3,4,5,6])
def testRoll(n = 10):
    result = ''
    for i in range(n):
        result = result + str(rollDie())
    print(result)
    

def genEven():
    l = random.randrange(0, 100, 2)
    return l
    

# Mersenne Twister
def _int32(x):
    # Get the 32 least significant bits.
    return int(0xFFFFFFFF & x)

class MT19937:
    def __init__(self, seed):
        # Initialize the index to 0
        self.index = 624
        self.mt = [0] * 624
        self.mt[0] = seed # Initialize the initial state to the seed
        for i in range(1, 624):
            self.mt[i] = _int32(
                    1812433253 * (self.mt[i - 1] ^ self.mt[i - 1] >> 30) + i)

    def extract_number(self):
        if self.index >= 624:
            self.twist()
        
        y = self.mt[self.index]
        
        # Right shift by 11 bits
        y = y ^ y >> 11
        # Shift y left by 7 and take the bitwise and of 2636928640
        y = y ^ y << 7 & 2636928640
        # Shift y left by 15 and take the bitwise and of y and 4022730752
        y = y ^ y << 15 & 4022730752
        # Right shift by 18 bits
        y = y ^ y >> 18
        
        self.index = self.index + 1
        
        return _int32(y)
    
    def twist(self):
        for i in range(624):
            # Get the most significant bit and add it to the less significant
            # bits of the next number
            y = _int32((self.mt[i] & 0x80000000) +
                       (self.mt[(i + 1) % 624] & 0x7fffffff))
            self.mt[i] = self.mt[(i + 397) % 624] ^ y >> 1
            
            if y % 2 != 0:
                self.mt[i] = self.mt[i] ^ 0x9908b0df
            self.index = 0
            #test
            
# 2 tosses of four-sided dice

def diff_sum_of_rolls(numTrials):
    """
    不含重复
    """
    result = []
    for i in range(numTrials):
        m = random.randrange(1, 5)
        n = random.randrange(1, 5)
        if m+n not in result:
            result.append(m+n)
    return result

def diff_sum_of_rolls_v2():
    result = []
    for i in range(1, 5):
        for j in range(1, 5):
            result.append(i+j)
    return result

def p_sum_of_rolls_is_even():
    r = diff_sum_of_rolls_v2()
    even_sum_count = 0
    for s in r:
        if s % 2 == 0:
            even_sum_count += 1
    return even_sum_count / len(r)

def p_sum_of_rolls_is_odd():
    r = diff_sum_of_rolls_v2()
    odd_sum_count = 0
    for s in r:
        if s % 2 != 0:
            odd_sum_count += 1
    return odd_sum_count / len(r)

def diff_pairs(numTrials):
    result = []
    for i in range(numTrials):
        m = random.randrange(1, 5)
        n = random.randrange(1, 5)
        if ([m,n] not in result) and ([n,m] not in result):
            result.append([m,n])
    return result

def print_diff_pairs_sum(numTrials):
    r = diff_pairs(numTrials)
    for p in r:
        print(p, sum(p))

def sum_of_rolls_is_even(numTrials):
    result = 0
    for i in range(numTrials):
        if (random.randrange(1, 5) + random.randrange(1, 5)) % 2 == 0:
            result += 1
    return result / numTrials

def sum_of_rolls_is_odd(numTrials):
    result = 0
    for i in range(numTrials):
        if (random.randint(1, 4) + random.randint(1, 4)) % 2 != 0:
            result += 1
    return result / numTrials

# first roll equal to second roll
#print(random.randint(1, 4), random.randint(1, 4))

def first_roll_larger_than_second_roll_four_sided_dice(numTrials):
    result = 0
    for i in range(numTrials):
        if random.randrange(1, 5) > random.randrange(1, 5):
            result += 1
    return result / numTrials

def at_least_one_is_four(numTrials):
    result = 0
    for i in range(numTrials):
        if random.randint(1, 4) == 4 or random.randint(1, 4) == 4:
            result += 1
    return result / numTrials

"""
roll 2 ten sided dice.
"""
def two_followed_by_three(nt):
    result = 0
    for i in range(nt):
        if random.randint(1, 10) == 2 and random.randint(1, 10) == 3:
            result += 1
    return result / nt

def first_roll_larger_than_second_roll_ten_sided_dice(nt):
    result = 0
    for i in range(nt):
        if random.randint(1, 10) > random.randint(1, 10):
            result += 1
    return result / nt

# roll 3 eight sided dice
def all_three_rolls_equal(nt):
    result = 0
    for i in range(nt):
        l = random.randint(1, 8)
        m = random.randint(1, 8)
        n = random.randint(1, 8)
        if l == m and m == n:
            result += 1
    return result / nt

# 2 Deck of cards
suits = ['♠️','♥️','♣️','♦️']
ranks = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

def random_card():
    suit_index = random.randrange(4)
    rank_index = random.randrange(13)
    return suits[suit_index] + ranks[rank_index]

def same_suit_of_two_cards(nt):
    result = 0
    for i in range(nt):
        if random_card()[0] == random_card()[0]:
            result += 1
    return result / nt

# 3 red and 3 green balls, replace after picking
def num_of_r_greater_than_or_equal_g(seq_count, nt):
    result = 0
    for j in range(nt):
        r_c = 0 # red count
        g_c = 0 # green count
        for i in range(seq_count):
            t = random.randrange(2)
            if t == 0:
                r_c += 1
            elif t == 1:
                g_c += 1
        if r_c >= g_c:
            result += 1
    return result / nt
    