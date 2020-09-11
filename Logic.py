happy = True
nothappy = False

if not happy:
    print("Hello World")
else:
    print("So sad")

print("Whats your age")
age = int(input())
print(type(happy))
print(age < 23)

can_drink = age > 20
print(can_drink)

if 20 < age < 65:
    print("Welcome to our app!")
elif not age == 65:
    print("Wow!!!")
elif 65 < age < 78:
    print("Discount price")
else:
    print("Thanks for trying app")

# Indentation Error -> Tab vs Space

