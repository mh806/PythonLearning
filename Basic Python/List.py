import copy

age = [12, 16, 15]
people = ["William", "Huang", "Mengjia"]
my_favorite_things = ["working", "netflix", ["amazon", "Hly"]]

my_favorite_things[0] = "Walking"
print(my_favorite_things)

copyList = my_favorite_things[:]
print(len(my_favorite_things))
# mutable -> create data without create new memory

copyList[0] = "MyFault"
# Two ways to copy lists
print(copyList)
print(my_favorite_things.copy())

TwoArray = ["1", "2", ["3", "4"]]
print(TwoArray[2][1])

# Shallow Copy and Deep Copy
c = copy.deepcopy(my_favorite_things)
c[2][0] = "Hulu"

my_least_favorite_things = ["coffee", "football", ["basketball", "finance"]]
print(my_favorite_things, c)

my_least_favorite_things = my_least_favorite_things + ["Editing"]
print(my_least_favorite_things)