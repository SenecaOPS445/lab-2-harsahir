#!/usr/bin/env python3
# Author: Harsahir Singh
# Author ID: 165357187
# Date Created: 2024/05/21

import sys

# Check if command line argument is provided
if len(sys.argv) > 1:
    # If argument provided, assign its integer value to timer
    timer = int(sys.argv[1])
else:
    # If no argument provided, assign default value of 3 to timer
    timer = 3

# While loop to repeat until (and not including when) timer equals 0
while timer > 0:
    print(timer)
    timer -= 1

print("blast off!")

