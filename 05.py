#!/usr/bin/env python3

import fileinput
from copy import deepcopy

code = [ int(x) for x in fileinput.input()[0].split(",") ]

def programA( code, input ):
    i = output = 0
    while i < len(code):
        instruction = int(code[i])
        opcode = instruction % 100
        mode1 = instruction % 1000
        mode2 = instruction % 10000
        
        if ( opcode == 1 ):
            param1 = int(code[i+1])
            param2 = int(code[i+2])
            param3 = int(code[i+3])
            a = int(code[param1]) if ( mode1 <  100 ) else param1
            b = int(code[param2]) if ( mode2 < 1000 ) else param2
            
            code[param3] = a + b
            i += 4
        elif ( opcode == 2 ):
            param1 = int(code[i+1])
            param2 = int(code[i+2])
            param3 = int(code[i+3])
            a = int(code[param1]) if ( mode1 <  100 ) else param1
            b = int(code[param2]) if ( mode2 < 1000 ) else param2
            
            code[param3] = a * b
            i += 4
        elif ( opcode == 3 ):
            param1 = int(code[i+1])

            code[param1] = input
            i += 2
        elif ( opcode == 4 ):
            param1 = int(code[i+1])
            a = int(code[param1]) if ( mode1 <  100 ) else param1

            output = a
            i += 2
        elif (opcode == 99 ):
            break
    return output

def programB( code, input ):
    i = output = 0
    while i < len(code):
        instruction = int(code[i])
        opcode = instruction % 100
        mode1 = instruction % 1000
        mode2 = instruction % 10000
        
        if opcode in ( 1, 2, 7, 8 ):
            param1 = int(code[i+1])
            param2 = int(code[i+2])
            param3 = int(code[i+3])
            a = int(code[param1]) if ( mode1 <  100 ) else param1
            b = int(code[param2]) if ( mode2 < 1000 ) else param2
            
            if opcode in (1, 2):
                code[param3] = a + b if opcode == 1 else a * b
            
            if opcode == 7:
               code[param3] = 1 if ( a < b ) else 0
            if opcode == 8:
               code[param3] = 1 if ( a == b ) else 0
            i += 4
        elif opcode == 3:
            param1 = int(code[i+1])

            code[param1] = input
            i += 2
        elif opcode == 4:
            param1 = int(code[i+1])
            a = int(code[param1]) if ( mode1 <  100 ) else param1

            output = a
            i += 2
        elif opcode in ( 5, 6 ):
            param1 = int(code[i+1])
            param2 = int(code[i+2])
            a = int(code[param1]) if ( mode1 <  100 ) else param1
            b = int(code[param2]) if ( mode2 < 1000 ) else param2

            if opcode == 5:
               i = b if ( a != 0 ) else i + 3
            if opcode == 6:
               i = b if ( a == 0 ) else i + 3
        elif (opcode == 99 ):
            break
    return output

print("A: ", programA( deepcopy(code), 1) )
print("B: ", programB( deepcopy(code), 5) )