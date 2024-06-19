import sys
input = sys.stdin.readline

monkey, dog = map(int, input().split())
d = dog - monkey
if d == 0:
    print(0)
elif d == 1:
    print(1)
elif d == 2:
    print(2)
else:
    for i in range(2, 2**16):
        if (i-1)**2 < d <= ((i-1)**2 + i**2)//2:
            print(2*i-2)
            break
        elif ((i-1)**2 + i**2)//2 < d <= i**2:
            print(2*i-1)
            break
'''
1: 1            => 1일
2: 1 1          => 2일
3: 1 1 1
4: 1 2 1        => 3일 (2*2-1)
5: 1 2 1 1
6: 1 2 2 1      => 4일 ()
7: 1 2 2 1 1
8: 1 2 2 2 1
9: 1 2 3 2 1    => 5일 (2*3-1)
10: 1 2 3 2 1 1
11: 1 2 3 2 2 1
12: 1 2 3 3 2 1
13: 
14:
15:
16: 1 2 3 4 3 2 1   => 7일 (2*4-1)

20:

25:
제곱 수 기준으로 나눠짐

'''