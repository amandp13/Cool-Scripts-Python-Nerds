
n=int(input())
for x in reversed(range(1, n+1)):
    for y in range(1, n+1):
        if y>x:
            break
        print("*", sep="", end="")
    i = int(x)
    i = ((n - i) * int(2)) + int(1)
    while i!=0:
        print(" ", sep="", end="")
        i=i-1
    for y in range(1 ,n+1):
        if y>x:
            break
        print("*", sep="", end="")
    print("\n" ,end="")

i=int(0)

for x in range(2,n+1):
    for y in range(1,n+1):
        if y>x:
            break
        print("*", sep="", end="")
    i = int(x)
    i = ((n - i) * int(2)) + int(1)
    while i!=0:
        print(" ", sep="", end="")
        i=i-1
    for y in range(1,n+1):
        if y>x:
            break
        print("*", sep="", end="")
    print("\n", end="")

