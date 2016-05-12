

def Newton(n,m):
    dwun = 1
    for i in range(m+1):
        if i==0:
            pass
        else:
            if m==0 or m==n:
                dwun = 1
            else:
                dwun=dwun*(n-i+1)/i


    return dwun

def Pascal(n):
    l=[]
    for i in range(n):
        if i==0:
            l.insert(i,[1])
        else:
            l.insert(i,[Newton(i,j) for j in range(i+1)])


    return l

def LotsOfHash(n):
    import sys
    l=Pascal(n)
    for i in range(n):
        for j in range(i+1):
            if Newton(i,j)%2==0:
                (l[i])[j]=' '
            else:
                (l[i])[j]='#'

            sys.stdout.write((l[i])[j])
        sys.stdout.write('\n')




