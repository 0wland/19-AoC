#!/usr/bin/env python3

import fileinput
import copy
import math
from cmath import polar, phase

a = {}
y = 0
for row in fileinput.input():
    row = row.strip()
    x = 0
    for col in row:
        a[(x,y)] = 1 if col == '#' else 0
        x += 1
    y += 1

resA = 0
final = []
station = []
for x, y in a.keys():
    if a[(x,y)] == 1:
        angles = {}
        for m, n in a.keys():
            if (m,n) != (x, y):
                if a[(m,n)] == 1:
                    r, phi = polar((complex(m, n)-complex(x, y))/ 1j)
                    if phi not in angles:
                        angles[phi] = {}
                    angles[phi][r] = [m,n]
        if len(angles) > resA:
            resA = len(angles)
            final = copy.deepcopy(angles)
            station = [x,y]
print( "A: ", resA )

t = 200
while True:
    for phi in sorted(final.keys()):
        r = sorted(final[phi].keys())[0]
        t -= 1
        if t <= 0:
            x, y = final[phi][r]
            print( "B: ", x*100+y)
            break

        del final[phi][r]
        if len(final[phi]) == 0:
            del final[phi]

    if t <= 0 or len(final) == 0:
        break