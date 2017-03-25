#!/bin/python3

import sys

count = 0
received = input().strip()
expected = 'SOS' * len(received)

for i in range(len(received)):
    if received[i] != expected[i]:
        count = count + 1

print (count)
