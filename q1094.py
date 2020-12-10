X = int(input())
X = bin(X)[2:]
print(f'X : {X}')
print(f'len(X) : {len(X)}')
a = 0
for i in range(len(X)):
    a += int(X[i])
print(a)