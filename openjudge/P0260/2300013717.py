n=int(input())
def skip(i):
    if i<=0:
        return 0
    if i==1:
        return 1
    if i==2:
        return 2
    else:
        return skip(i-1)+skip(i-2)
print(skip(n))
