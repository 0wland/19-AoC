#!/usr/bin/env python3

import sys
import os
import re
import csv

def main():
    filenameA = re.sub( r'.py','a.txt', os.path.basename(__file__) )
    
    # A
    wires = run_program( filenameA )
    intersections = intersection( wires[0], wires[1] )
    i = 0
    closest = []
    while i < len( intersections ):
        closest.append( get_distance( intersections[i] ) )
        i += 1
    print( "A: ", min( closest ) )
    
    # B
    shortest = {}
    for x in wires:
        position = 0
        while position < len(x):
            i = 0
            while i < len( intersections ):
                if ( x[position] == intersections[i] ):
                    key = get_distance(x[position])
                    if ( key in shortest):
                        shortest[key] += position + 1
                    else:
                        shortest[key] = position + 1
                i += 1
            position += 1
    print( "B: ", shortest[min(shortest, key=shortest.get)] )

def run_program( filename ):
    f = open( filename, "r" )

    wires = []
    for row in csv.reader( f, delimiter = ',' ):
        r = 0
        x = 0
        y = 0
        wire = []
        while r < len(row):
            path = row[r]
            direction = path[:1]
            length = int(path[1:])

            if ( direction == 'R' ):
                for i in range( length ):
                    x += 1
                    wire.append([x,y])
            elif ( direction == 'L' ):
                for i in range( length ):
                    x -= 1
                    wire.append([x,y])        
            elif ( direction == 'U' ):
                for i in range( length ):
                    y += 1
                    wire.append([x,y])       
            elif ( direction == 'D' ):
                for i in range( length ):
                    y -= 1
                    wire.append([x,y])       
            else:
                break
            r += 1
        wires.append(wire)
    f.close
    return wires

def intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3

def get_distance(lst):
    return abs(0-lst[0])+abs(0-lst[1])

if __name__ == '__main__':
    main()