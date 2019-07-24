x = list(map(int, input("Enter multiple numbers: ").split()))

x=[2,2,2,2]

l=[]

for i in x:
    if i%2==0:
         l.append(i)


print(l)
