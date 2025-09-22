# Problem 2: a no. of odd values
a=int(input('enter a value: '))
res=[]
i=0
while len(res)!=a:
    if i%2==1:
        res.append(i)
    i+=1
print(res)