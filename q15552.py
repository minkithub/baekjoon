import sys

num = int(sys.stdin.readline())

for i in range(num):
    p, q = map(int, sys.stdin.readline().split())
    print(p + q)