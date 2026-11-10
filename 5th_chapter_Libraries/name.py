#import sys
#try:
#
#    print("hello, my name is" ,  sys.argv[1])
#
#except IndexError:
#    print("Too few arguments")


#check for eroors

#import sys

#if len(sys.argv) <2:
#    sys.exit("too few arguments")
#
#elif len(sys.argv) > 2: 
#    sys.exit("too many arguments")
#
#print name tags
#print("hello my name is", sys.argv[1])


#taking too many input in the command 

import sys

if len (sys.argv) < 2: 
    print("too few value")

for name in sys.argv[1:]:
    print("Hello , my name is ", name)