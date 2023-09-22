#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()
    count = {}

    for char in s:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    # x[0] is necessary for half of test cases
    sorted_chars = sorted(count.items(), key=lambda x: (-x[1], x[0]))

    for i in range(min(3, len(sorted_chars))):
        char, count = sorted_chars[i]
        print(char, count)
