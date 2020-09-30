shopping_cart = ["chicken", "curry", "dumpling"]
healthy = ["curry", "vegetable", "fruits"]

if "chicken pie" not in shopping_cart:
    print("eating the pie")

if "chicken" in shopping_cart:
    shopping_cart.remove("chicken")

print(shopping_cart)
print(id(healthy))
healthy[:] = [item for item in healthy if item in shopping_cart]
healthy_shopping = []
for item in healthy:
    if item in shopping_cart:
        healthy_shopping.append(item)

print(id(healthy))
print(healthy_shopping)