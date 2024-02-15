n = int(input())
lengths = list(map(int, input().split()))
lengths.sort(reverse=True)
for i in range(n - 2):
    a = lengths[i]
    b = lengths[i + 1]
    c = lengths[i + 2]
    if a < b + c:
        holat = True
        javob = [c, b, a]
        break
else:
    holat = False

if holat:
    print(*javob)
else:
    print(-1)