s1={1,2,3,'A','B','C'}
s2={1,'A','B'}

print(1 in s1)
print('X' not in s2)

print(s2.issubset(s1))
print(s1.issuperset(s2))

s3=s1.intersection(s2)
s4=s1.union(s2)
s5=s1.difference(s2)
s6=s1.symmetric_difference(s2)
#Explore this in real time use