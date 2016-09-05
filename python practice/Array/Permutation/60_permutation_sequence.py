n = 3
k = 2

factorial = [None] * 10

factorial[0] = 0
factorial[1] = 1
for i in range(2,10):
    factorial[i] = factorial[i-1] * i

per = [None] * n
for i in range(n, 0, -1):
    m = (k - 1) / factorial[n-1] + 1
    k = k - m
    per[i-1] = m

print("".join(per.reverse()))
