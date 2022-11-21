def ternary(n):
    if n==0:
        return '0'
    l=[]
    while n:
        n,r=divmod(n,3)
        l.append(str(r))
    return ''.join(reversed(l))
