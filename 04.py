#!/usr/bin/env python3

import fileinput

start, end = [ int(x) for x in (fileinput.input())[0].split("-") ]

countA = countB = 0
for n in range(start, end):
    password = [int(d) for d in str(n)]
    adjacent = []
    i = count = maximum = 1
    current = password[0]
    while i < len(password):
        if( current < password[i] ):
            adjacent.append(count)
            count = 1
            current = password[i]
        elif( current == password[i] ):
            maximum += 1
            count += 1
        else:
            break
        i += 1
        if( i == len(password) ):
            adjacent.append(count)

    if ( i == len(password) ):
        if ( maximum > 1 ):
            countA +=1
        
        if ( 2 in adjacent ):
            countB += 1

# A
print( "A: ", countA )

# B
print( "B: ", countB )