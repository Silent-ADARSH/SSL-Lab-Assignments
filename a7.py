n = int(input())
a = range(n)
for i in range(n):
    if a[i] % 2 == 0:
        print(a[i],"is even")
    else:
        print(a[i],"is odd")
    i += 1
