#!/usr/bin/env python3

import fileinput
import re

moons = []
i = 0
for line in fileinput.input():
    p = re.compile('[^0-9,-]')
    moon = {}
    moon['pos'] = [ int(n) for n in p.sub('', line).split(",") ]
    moon['vel'] = [ 0, 0, 0 ]
    moons.append(moon)

attemps = 1000
total = 0
for i in range(0, attemps):
    for moon in moons:
        for next_moon in moons:
            if moon != next_moon:
                for c in range( 0, len( moon['pos'] ) ):
                    if moon['pos'][c] < next_moon['pos'][c]:
                        moon['vel'][c] += 1
                    elif moon['pos'][c] > next_moon['pos'][c]:
                        moon['vel'][c] -= 1

    for moon in moons:
        for c in range( 0, len( moon['pos'] ) ):
            moon['pos'][c] += moon['vel'][c]

for moon in moons:
    pot = kin = 0
    for c in range( 0, len( moon['pos'] ) ):
        pot += abs( moon['pos'][c] )
        kin += abs( moon['vel'][c] )
    total += pot * kin

print("A: ", total)