num= int(input())
res =0
def count(n):
    c=0
    while(n):
        k = n%2
        if(k==1):
            c+=1
        n = n//2
    return c

for i in range(1, num+1):
    res+=count(i)
print(res)
