friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

# Difference - will check differences
local_friends = friends.difference(abroad)
print(local_friends)

# Union - will add
local = {"Rolf"}
abroad = {"Bob", "Anne"}
friends = local.union(abroad)
print(friends)

# Inersection - return similar between two or more sets
art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}
one_subject = art.difference(science)
print(f"{one_subject} are studying one subject only")
both = art.intersection(science)
print(both)


