a = {1,4,6,9,2,20,43}
b = {3,4,6,2,89}

print(a.union(b))

print(a.intersection(b))

print({1,9,2}.issubset(a)) #{1,9,2} subset of a
print({2,8,78}.issubset(b))

print(a.issuperset({1,4,6,43})) #a is superset of {1,4,6,43}
print(b.issuperset({3,4,6,2}))
