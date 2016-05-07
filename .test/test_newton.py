
import os, sys
sys.path.append(os.getcwd())

from solution import Newton, Pascal, LotOfHash
from random import randint

print "Testing Newton ..."
n = randint(10,15)
x = [Newton(n, i) for i in range(n+1)]
if not sum(x) == 2**n :
    sys.exit("Wrong Newton sum for " + str(n));
n = randint(300,350)
if not Newton(n,2) == n*(n-1)/2:
    sys.exit("Wrong Newton("+str(n)+",2)");

print "Testing Pascal ..."
n = randint(30,40)
p = Pascal(n)
x = [randint(1,n-1) for i in range(10)]
y = [randint(0,x[i]-1) for i in range(10)]
if not all([Newton(i,j) == p[i][j] for i,j in zip(x,y) ]):
    sys.exit("Pascal != Newton in some places")

print "Testing LotOfHash ..."
n=randint(40,60)
stdout_ = sys.stdout
sys.stdout = open('_tmp.txt', 'w')
LotOfHash(n)
sys.stdout = stdout_
with open('_tmp.txt') as f:
    lines = f.readlines()
Hash = [ l.count("#") for l in lines ]
HashR = [ 2**bin(i).count("1") for i in range(n) ]
if not len(lines) == n:
    sys.exit("Lenght of output from LotOfHash(n) is not n lines")
if not all([i == j for i,j in zip(Hash,HashR)]):
    sys.exit("Wrong number of # in lines from LotOfHash")
