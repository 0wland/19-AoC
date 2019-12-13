#!/usr/bin/env python3

import fileinput


log = {}
for row in fileinput.input():
    planet, orbit = row.strip().split(")")
    log[orbit] = planet

resA = 0
for orbit, planet in log.items():
    while True:
        resA += 1
        if ( planet == 'COM' ):
            break
        planet = log[planet]

print("A: ", resA )

resB = 0
distance = 0
you = san = {}
planet = log['YOU']
while True:
    you[planet] = distance
    planet = log[planet]
    distance += 1
    if ( planet == 'COM' ):
        break

distance = 0
planet = log['SAN']
while True:
    san[planet] = distance
    planet = log[planet]
    distance += 1
    if ( planet == 'COM' or planet in you ):
        break    

print( "B: ", you[planet] + distance )