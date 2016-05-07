
import os, sys
sys.path.append(os.getcwd())

from solution import PowerModulo
from random import randint

from resource import getrusage as resource_usage, RUSAGE_SELF
from time import time as timestamp

import signal

def signal_handler(signum, frame):
    raise Exception("Exceeded total execution time: 5s!")
signal.signal(signal.SIGALRM, signal_handler)
signal.alarm(5)

slow=False

def PowerModuloT(a,b,c):
  global slow
  r1 = resource_usage(RUSAGE_SELF)
  ret = PowerModulo(a,b,c)
  r2 = resource_usage(RUSAGE_SELF)
  t = r2.ru_utime - r1.ru_utime
  if (t > 0.001):
    print "PowerModulo(%d,%d,%d) is slow! %.4fs" % (a,b,c,t)
    slow=True
  return ret
                                                                        
print "Testing PowerModulo ..."
n = randint(20,50)
p1 = [PowerModuloT(2, i, n) for i in range(15)]
p2 = [(2**i) % n for i in range(15)]
if not all([ i==j for i,j in zip(p1,p2)]):
  sys.exit("Wrong powers of 2 in PowerModuloT")

n = randint(3000,4000)
a = randint(1,n-1)
b = randint(3000,5000)
c = randint(3000,5000)

abc1 = PowerModuloT(PowerModuloT(a, b, n), c, n)
abc2 = PowerModuloT(a, c*b, n)
abc3 = PowerModuloT(PowerModuloT(a, c, n), b, n)
if not abc1 == abc2 == abc3:
  sys.exit("a^(c*b) != (a^b)^c")

abc1 = ( PowerModuloT(a,c,n) * PowerModuloT(a, b, n) ) % n
abc2 = PowerModuloT(a, c+b, n)
if not abc1 == abc2:
  sys.exit("a^(b+c) != a^b * a^c")

if slow:
  sys.exit("PowerModulo passed tests, but is too slow!")

