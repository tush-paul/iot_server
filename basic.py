b=[]
while True:
    a=int(input("Enter a number or press -1 to quit: "))
    if a == -1:
        break
    b.append(a)
a=[]
for i in b:
    if i%2==0:
        a.append(i**2)
print(a)