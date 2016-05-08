import os, sys
sys.path.append(os.getcwd())

from solution import Intersect
from random import randint, uniform

import signal
def signal_handler(signum, frame):
    raise Exception("Exceeded total execution time: 5s!")
signal.signal(signal.SIGALRM, signal_handler)
signal.alarm(5)

print "Testing Intersect ..."

n = randint(8,15)*2
ret = [Intersect( (0,0,k), (0,n,k) ) for k in range(1,n)]

retl = [len(i) for i in ret]
if not retl[n/2-1] == 1:
  sys.exit("Intersect: did not return one point")
if not all([ i == 0 for i in retl[:(n/2-1)] ]):
  sys.exit("Intersect: did not return no point")
if not all([i == 2 for i in retl[(n/2):]]):
  sys.exit("Intersect: did not return two point")

rr = [i for j in ret for i in j]

if not all([ isinstance(i,tuple) for i in rr ]):
  sys.exit("Not all returnet points are tuples")
if not all([ len(i) == 2 for i in rr ]):
  sys.exit("Not all returnet points have two coordinates")


r1 = uniform(2,5)
r2 = uniform(2,5)
d = uniform(abs(r1-r2)+0.1,r1+r2-0.1)
C = [(0,0,r1), (0,d,r2)]
P = Intersect( C[0],C[1] )
if not len(P) == 2:
  sys.exit("Wrong number of intersections for a random set of points")

ds = [ (p[0] - c[0])**2 + (p[1] - c[1])**2 - c[2]**2 for p in P for c in C ]
if not all([ abs(d) < 1e-8 for d in ds ]):
  sys.exit("Wrong distances for a random set of points")
