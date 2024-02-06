#!/usr/bin/env python3
""" 
A program to output the values in a fibonacci sequence to a tex formatted table
"""

# return the nth number in a Fibonacci sequence
def fibSequence( n ):
    if( int(n) ==0):
        return 0.0
    fibOld = 0.0 # for speed, you should use floats for calculations 
    if( int(n) == 1):
        return 1.0
    fibCurr = 1.0
    for i in range(1,int(n)): # count in integers
        fibNext = fibCurr + fibOld
        fibOld = fibCurr
        fibCurr = fibNext
    return fibNext

# to write to file you will need a string
f = open('example-table.tex','w')
f.write("\\begin{tabular}{c|c} \n ")
f.write(" $i$ & $F_i$ \\\\ \n ")
f.write("\\hline \n ")
for i in range(0,11):
    # using a formatted string f"...."
    # we output the float variable fibSequence(i) using 
    # 10 spaces, and no digits after the decimal place i.e. 0
    # so write {fibSequence(i):20.0f}
    # can be adjusted depending on the output required
    str = f"{i} & {fibSequence(i):10.0f} \\\\ \n"
    f.write(str)
f.write("\\end{tabular} \n ")
f.close()