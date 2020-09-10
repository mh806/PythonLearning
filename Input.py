# interaction: input and output
print("Hey whats your name?")
name = input()
print("Hello, "+name)

print("Whats your favourite number")
fav_num = int(input())
fav_num2 = int(input())
print(fav_num+fav_num2)

# How to convert string to hunumbers - Type casting
print(type(str(5.6)))
print(str(fav_num) + "+" + str(fav_num2) + "=" + str(fav_num+fav_num2))