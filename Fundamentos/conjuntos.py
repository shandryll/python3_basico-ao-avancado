conjunto = {1, 2, 3}
print(type(conjunto))

conjunto = set('cod3333r')
print(conjunto)
print({1, 2, 3} == {3, 2, 1, 2})

c1 = {1, 2}
c2 = {2, 3}
print(c1.union(c2))
print(c1.intersection(c2))
print(c1.update(c2))

print(c2 <= c1)
print(c1 <= c2)

print({1, 2, 3} - {2})
print(c1 - c2)
