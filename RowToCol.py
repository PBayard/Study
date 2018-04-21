l1 = ['a', 'b', 'c']
l2 = ['1', '2', '3']
l3 = ['x', 'y', 'z']
for row in zip(l1, l2, l3):
    print(' '.join(row))
print(' ')

l = [[1, 3, 4], [2, 5, 7]]
for s in l:
    print(*s)