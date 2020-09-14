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

for i in range(len(friends)):
    print(i, friends[i], end=" ")
print()

for name in friends:
    if name == "William":
        print(name + " is searched")
        break
    else:
        print("Results not found")
else:
    # Wont display once loop is broke
    print("Loop is done")

# pass -> placeholder until have better solution -> otherwise failed
print("Whats value for i")
i = int(input())

while i < 10:
    print("Wow amazing")
    i += 1

numbers = [1, 52, 15, 88, 40, 22, 78, 11]

square = 500
while i < len(numbers):
    if numbers[i] ** 2 > square:
        print(numbers[i], "square is larger than ", square)
        break

    print(numbers[i], "square is not larger than", square)
    i += 1
else:
    print("none square are larger than", square)

i = 90
# do while loop
while i < 10:
    print(i)
    i += 1

while True:
    print(i)
    i += 1
    if i > 9:
        break

# indefinite loop
print("do you want to continue Y/N")
response = input()
while response.lower() == "y" or response.upper() == "Y":
    print("do you want to continue Y/N")
    response = input()

# lower and upper
# islower and isupper

# 74