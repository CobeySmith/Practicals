"""Random"""

import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

"""
1. 5 was the smallest, 20 was the largest
2. 3 was the smallest, 9 was the largest. Not able to produce 4.
3. 2.5 was the smallest, 5.5 was the largest.
"""

print(random.randint(1, 100))
