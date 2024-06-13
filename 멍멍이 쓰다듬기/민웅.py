# 1669_멍멍이 쓰다듬기_petting a puppy
import sys
input = sys.stdin.readline

monkey, puppy = map(int, input().split())

goal = puppy - monkey

if goal == 0:
    print(0)
else:
    day = int(goal ** (1/2))
    # print(goal ** (1/2), day)
    if day**2 == goal:
        ans = day*2 - 1
    elif day**2 < goal <= day**2 + day:
        ans = day*2
    else:
        ans = day*2 + 1

    print(ans)

# 1 2 1 - 4
# 1 2 1 1 - 5
# 1 2 2 1 - 6
# 1 2 2 1 1 - 7
# 1 2 2 2 1 - 8
# 1 2 3 2 1 - 9
# 1 1 2 3 2 1 - 10
# 1 2 2 3 2 1 - 11
# 1 2 3 3 2 1 - 12
# 1 2 3 3 2 1 1 - 13
# 1 2 2 3 3 2 1 - 14
# 1 2 3 3 3 2 1 - 15
# 1 2 3 4 3 2 1 - 16