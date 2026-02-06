n = int(input())
f = set()

for i in range(1, n + 1):
    s = input()
    if s not in s:
        f.add(s)
        
for s in sorted(first_index):
    print(s, first_index[s])
