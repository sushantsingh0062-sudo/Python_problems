# Input two sets and print union, intersection, and difference.
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
difference_set = set1.difference(set2)
print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference (set1 - set2):", difference_set)