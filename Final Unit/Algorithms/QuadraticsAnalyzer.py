#!/usr/bin/env python3
#
# Quadratic Analyzer

import math

NewLineString = "\n---------------------------------------------------------------------------\n"

#-------------------
print(NewLineString)
#-------------------

#---------------------------------------------------------------------------
# Input
#---------------------------------------------------------------------------

#-------------------
print(NewLineString)
#-------------------

try:
    a = float(input("Tell me 'a':  "))
except:
    print("!!! Error:  Bad input.")
    exit()
    
print("")

try:
    b = float(input("Tell me 'b':  "))
except:
    print("!!! Error:  Bad input.")
    exit()

print("")

try:
    c = float(input("Tell me 'c':  "))
except:
    print("!!! Error:  Bad input.")
    exit()


#---------------------------------------------------------------------------
# Processing Input
#---------------------------------------------------------------------------

if (a==0):
    print("!!! Error:  a=0.  Not a parabola.")
    exit(0)

#---------------------------------------------------------------------------
# Analysis - Input function
#---------------------------------------------------------------------------

#-------------------
print(NewLineString)
#-------------------

eqn_str = "y = "

a_str = ""
if (a>0):
    a_str += "{:.5f}".format(a)
    a_str += " x^2"
elif (a<0):
    a_str += "- {:.5f}".format(abs(a))
    a_str += " x^2"

b_str = ""
if (b>0):
    b_str += " + "
    b_str += "{:.5f}".format(b)
    b_str += " x"
elif (b<0):
    b_str += " "
    b_str += "- {:.5f}".format(abs(b))
    b_str += " x"

c_str = ""
if (c>0):
    c_str += " + "
    c_str += "{:.5f}".format(c)
elif (c<0):
    c_str += " "
    c_str += "- {:.5f}".format(abs(c))

eqn_str += a_str
eqn_str += b_str
eqn_str += c_str

#---------------------------------------------------------------------------
# Analysis - Discriminant and Solution(s)
#---------------------------------------------------------------------------

print("Processing:               " + eqn_str)

D = b**2 - 4 * a * c

#-------------------
print(NewLineString)
#-------------------

print("Discriminant:             b^2 - 4ac = " + str(D))

if (D >= 0):
    if (D > 0):
        print("Two real solutions exist. ")
        print("First solution:           x = " + str((-b+math.sqrt(D))/2/a))
        print("Second solution:          x = " + str((-b-math.sqrt(D))/2/a))
    elif (D == 0):
        print("One real solution.        ")
        print("Solution:                 x = " + str((-b/2/a)))
elif (D < 0):
    print("No real solutions.  ")
    
#---------------------------------------------------------------------------
# Analysis - Extremum
#---------------------------------------------------------------------------

#-------------------
print(NewLineString)
#-------------------

h = -b/2/a
k = a*h*h + b*h + c
    
if (a > 0):
    print("Minimum exists.           ")
    print("                         ({:.5f},{:.5f})".format(h,k))
elif (a<0):
    print("Maximum exists.           ")
    print("                         ({:.5f},{:.5f})".format(h,k))
    
#-------------------
print(NewLineString)
#-------------------
