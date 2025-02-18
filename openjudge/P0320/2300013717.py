n=int(input())
def skip(i):
    if i<=0:
        return 0
    if i==1:
        return 1
    if i==3:
        return 2
    if i==5:
        return 5
    else:
        return skip(i-1)+skip(i-3)+skip(i-5)
print(skip(n))
