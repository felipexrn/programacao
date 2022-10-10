n = int(input())
b = list(map(int, input().split()))
f = []
f.append(b[0])
end = 0
for i in range(len(b) - 1):
    if b[i] - b[i + 1] == 1:
      b[i] = 0
print(*b)