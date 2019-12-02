#!/usr/bin/env python3

import sys
import os
import re
import csv

def main():
    filenameA = re.sub( r'.py','a.txt', os.path.basename(__file__) )
    filenameB = re.sub( r'.py','b.txt', os.path.basename(__file__) )
    
    # A
    print( "A: ", run_program( filenameA, 12, 2 ) )
    
    # B
    for noun in range( 0, 99 ):
        for verb in range( 0, 99 ):
            if ( run_program( filenameB, noun, verb ) == 19690720 ):
                print( "B: ", 100 * noun + verb )
                return

def run_program( filename, noun, verb ):
    f = open( filename, "r" )
    for row in csv.reader( f, delimiter = ',' ):
        row[1] = noun
        row[2] = verb
        i = 0                
        while i < len(row):
            opcode = int(row[i])
            a = int(row[i+1])
            b = int(row[i+2])
            p = int(row[i+3])

            if ( opcode == 1 ):
                row[p] = int(row[a]) + int(row[b])
                i += 4
            elif ( opcode == 2 ):
                row[p] = int(row[a]) * int(row[b])
                i += 4
            elif (opcode == 99 ):
                i += 1
                break
    f.close
    return row[0]

if __name__ == '__main__':
    main()