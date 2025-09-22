# Problem 4: factors of list of elements
n=list(map(int, input("enter numbers separated by space: ").split()))
dct={}
for i in range(1,10):
    r=0
    dct[i]=0
    for j in n:
        if j%i==0:
            r+=1
    dct[i]=r
print(dct)