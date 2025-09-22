# Problem 3: Odd values based on integer a
a=int(input('enter a value1: '))
if a%2==1:
    res=[]
    i=0
    while len(res)!=a:
        if i%2==1:
            res.append(i)
        i+=1
    print(res)
elif a%2==0:
    res=[]
    i=0
    while len(res)!=a-1:
        if i%2==1:
            res.append(i)
        i+=1
    print(res)