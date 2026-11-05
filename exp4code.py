num = [50, 20, 30, 10, 40, 20]
print("Original list", num)
print("Length of list", len(num))

num.append(60)
print("After append (60)", num)

num.insert(2, 25)
print("After insert (2,25)", num)

num.remove(20)
print("After removing (20)", num)
print("Count of 20", num.count(20))

num.sort()
print("After sorting():", num)

num.reverse()
print("After reverse():", num)

new_list = num.copy()
print("Copied list:", new_list)

num.extend([70, 80])
print("After extend():", num)

print("Maximum Value:", max(num))
print("Minimum value:", min(num))
print("Sum of values:", sum(num))
