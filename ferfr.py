import re
import operator

def something():
    ops = { "+": operator.add, "-": operator.sub } 

    d = "regreg 5  + - freg 56"

    words = d.split()

    for x in words:
        if  (re.match('^\d*$',x)):
            print(x)
        
        if (re.match('\+',x)):
            print("works")


something()


print('{} add {} '.format(1,3))


