N = int(input())

sieve = [False, False] + [True]*(N-1)
for i in range(2, int(N**0.5)+1):
    if sieve[i]:
        for j in range(2*i, N+1, i):
            sieve[j] = False

_sosu = [i for i in range(2, N+1) if sieve[i]==True]

while True:
    for i in _sosu:
        if N%i==0:
            print(i)
            N = N//i
            break
    if N==1:
        break
