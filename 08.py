#!/usr/bin/env python3

import fileinput

size = 25 * 6
zero_layer = size
resA = 0
pic = [None for j in range(size)]

code = fileinput.input()[0].strip()
chunks = [code[i:i+size] for i in range(0, len(code), size)]
a = 0
for layer in chunks:
    # A
    zero_count = layer.count('0')
    if ( zero_count < zero_layer ):
        resA = layer.count('1') * layer.count('2')
        zero_layer = zero_count
    a += 1

    # B 
    for v in range(0,len(layer)):
        value = int(layer[v])
        if ( pic[v] == None and value != 2 ):
            pic[v] = "#" if value == 1 else " "

print("A: ", resA )
print("B: ")
for i in range(0,len(pic)):
    if ( i % 25 == 0 and i != 0 ):
        print("")
    print( pic[i], end="" )
print("")