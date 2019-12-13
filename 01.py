#!/usr/bin/env python3

import sys
import os
import re
import csv

def main():
    filename = re.sub( r'.py','.txt', os.path.basename(__file__) )
    
    # A
    print( "A: ", run_programA( filename ) )
    # B
    print( "B: ", run_programB( filename ) )

def run_programA( filename ):
    f = open( filename, "r" )
    sum = 0
    for row in csv.reader( f, delimiter = '\n' ):
        i = 0
        while i < len(row):
            sum += calc_fuel( row[i] )
            i += 1
    f.close
    return sum

def run_programB( filename ):
    f = open( filename, "r" )
    total = 0
    for row in csv.reader( f, delimiter = '\n' ):
        i = 0
        while i < len(row):
            sum = 0
            res = row[i]
            while True:
                res = calc_fuel( res )
                if( res <= 0 ):
                    break
                else:
                    sum += res
            total += sum
            i += 1
    f.close
    return total

def calc_fuel( fuel ):
    return int( float(fuel) / 3 ) - 2

if __name__ == '__main__':
    main()