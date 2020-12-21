# sets
my_set = {1,2,3,4,5,6}
print(my_set)

my_set.add(7)
print(my_set)

# sets
my_set = {1,2,3,4,5,6}
your_set = {4,5,6,7,8,9}

# difference
print(my_set.difference(your_set))

# discard
my_set.discard(3)
print(my_set)

# dfference update
my_set.difference_update(your_set)
print(my_set)

# intersection
print(my_set.intersection(your_set))

# is disjoint
print(my_set.isdisjoint(your_set))

# is subset
print(my_set.issubset(your_set))
# is super set
print(my_set.issuperset(your_set))
# union
print(my_set.union(your_set))