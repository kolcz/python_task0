# Python Excercises (Task 0)

Create a file `solution.py` with the described functions and a file `test.py` that will evaluate them for a selected set of inputs (your choice).

## Excercise 1

Create a function `Newton(n,m)` which for integers `n` and `m` will return an integer equal to the the [binomial coefficient](https://en.wikipedia.org/wiki/Binomial_coefficient) n over m. Which is equal to:

![n over m](https://latex.codecogs.com/gif.latex?\\left(\\begin{matrix}n\\\\m\\end{matrix}\\right)%3D\\frac{n!}{m!(n-m)!})

Do it so that the result will be still good for **high values of `n`**, for example:
```python
> Newton(200,2)
19900
```

## Excercise 2

Create a function `Pascal(n)` which will return a list of `n` rows of elements of the [Pascal triangle](https://en.wikipedia.org/wiki/Pascal's_triangle). The result should be a list of length `n`. The elements of this list should be also lists, of increasing length (from 1 to `n`). For example:
```python
> Pascal(4)
[ [1], [1,1], [1,2,1], [1,3,3,1] ]
```

## Excercise 3

Create a function `LotOfHash(n)` which will print one line for each row of the Pascal Triangle, in which all the odd numbers will be printed as `#`. For example:
```python
> LotOfHash(6)
#
##
# #
####
#   #
##  ##
```
Consider how to do it for high values of `n`

## Excercise 4

Write a function `PowerModulo(a,b,n)` which will calculate the [reminder](https://en.wikipedia.org/wiki/Remainder) of `a^b` with respect to division by `n`:

![a^b mod n](https://latex.codecogs.com/gif.latex?a^b\\quad\\text{mod }n)

For example:
```
> PowerModulo(2,3,10) # 8 mod 10 = 8
8
> PowerModulo(2,4,10) # 16 mod 10 = 6
6
> PowerModulo(2,5,10) # 32 mod 10 = 2
2
```

Implement is so that the value can be calculated for **very high numbers (including `b`)**, for example:
```
> PowerModulo(2,200,100)
76
```

Clue: *To calculate `a^(2^k)~ you need only `k` multiplications*

## Excercise 5

Write a function `Intersect(a,b)` that for two tuples `a=[x1,y1,r1]` and `b=[x2,y2,r1]` will return a list of points of intersection of two circles, one with center at (`x1`,`y1`) and radious `r1` and the other at (`x2`,`y2`) and radious `r2`. For example:
```
> Intersect( (0,0,5), (6,0,5) )
[ (3, 4), (3,-4) ]
> Intersect( (0,0,5), (10,0,5) )
[ (5, 0) ]
> Intersect( (0,0,5), (15,0,5) )
[ ]
```
