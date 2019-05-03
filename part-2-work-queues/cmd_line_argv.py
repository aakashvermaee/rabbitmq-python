import sys
from collections import defaultdict

print(sys.argv)

argsdict = {}

for farg in sys.argv:
    if farg.startswith('--'):
        (arg, val) = farg.split('=')
        arg = arg[2:]

        if arg in argsdict:
            argsdict[arg].append(val)
        else:
            argsdict[arg] = [val]

print(argsdict)

# queue
queue = argsdict['queue'][0]

print(queue)
