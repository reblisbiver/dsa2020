def count(m,n):
    if m<=1 or n==1:
        return 1
    if m<n:
        return count(m,m)
    else:
        return count(m,n-1)+count(m-n,n)
for _ in range(int(input())):
    m,n=map(int,input().split())
    print(count(m,n))
