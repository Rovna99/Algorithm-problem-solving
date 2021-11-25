S = input()

a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in a:
    S = S.replace(i, '*')

print(len(S))
