poem = "Where am I"

# Learning Index
print(poem[3])

# Slicing - SubString
print(poem[5:])

# Not index for 4
print(poem[:4] + poem[4:])

print(poem[-1])

task = ["Not Yet"]
different = task
different[0] = "Hello"
print(different)
print(task)

print(len(task[0]))

print("Your message was" + str(len(task)) + " long")
print(id(task))
print(str(id(task)))