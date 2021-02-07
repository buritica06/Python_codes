#!/bin/python3

import math
import os
import random
import re
import sys

def pares(n):
    n_even = n%2
    if n_even != 0:
        print("Weird")
    elif n_even ==0 and n >=6 and n<=20:
           print("Weird")
    else:
        print("Not Weird")

if __name__ == '__main__':
    n = int(input().strip())
    pares(n)