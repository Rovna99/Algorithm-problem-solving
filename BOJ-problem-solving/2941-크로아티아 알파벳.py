n = input()

data = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in data:
    n = n.replace(i, '*')
print(len(n))

