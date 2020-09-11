friends = ["William", "Huang", "Michael", "Jordan"]

for friend in friends:
    # how to create in same line
    print(friend, end="")
print()

# range
for i in range(10):
    print(i, end="")
print()

# include first
for x in range(1, 5):
    print(x, end=" ")
print()

# step
for y in range(1, 100, 10):
    print(y, end=" ")
print()

for z in range(200, 1, -20):
    print(z, end=" ")
print()

for m in range(19):
    print(m, end="  ")
print()

print(sum(range(1, 100, 21)))
# 57