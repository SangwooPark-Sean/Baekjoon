from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

d = deque([])

for i in range(n):
    a = input().rstrip()

    if a[0:2] == "pu" :
        d.append(int(a.split()[1]))
        continue

    elif a == "pop":
        if len(d) == 0:
            print(-1)
            continue
        else:
            print(d.popleft())
            continue
    
    elif a == 'size':
        print(len(d))
        continue
    
    elif a == 'empty':
        if len(d) == 0:
            print(1)
            continue
        else:
            print(0)
            continue
    
    elif a == 'front':
        if len(d) == 0:
            print(-1)
            continue
        else:
            print(d[0])
            continue

    elif a == 'back':
        if len(d) == 0:
            print(-1)
            continue
        else:
            print(d[-1])
            continue

