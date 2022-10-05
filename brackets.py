BRACKETS = {'(': (0, 1), ')': (0, -1), '[': (1, 1), ']': (1, -1), '{': (2, 1), '}': (2, -1)}
counters = [0, 0, 0]

for bracket in input():
    b = BRACKETS[bracket]
    counters[b[0]] += b[1]
    if any(map(lambda x: x < 0, counters)):
        break
print(all(map(lambda x: x == 0, counters)))
