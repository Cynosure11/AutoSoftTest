l = ["Bob", "Rolf", "Anne"] # List
t = ("Bob", "Rolf", "Anne") # Tuples. You can't modify and replace names
s = {"Bob", "Rolf", "Anne"} # Set.
print(l[0]) # Index
l[0] = "Smith"
print(l)

print(t[1])

l.append("Smith2") # Append will add 4 name on the list
print(l)

l.remove("Anne")
print(l)

s.add("Carol")
print(s)
"""
Notice that it's add, and not append.
That's because append means
'add at the end', but sets dont have
an 'end' since they dont have order
"""






