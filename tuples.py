
cart = ('John',["milk","Bread","Eggs"])

print("Initial Cart")
print(cart)

cart[1].append("Apples")
print("\nAfter Adding Apples")
print(cart)

cart[1].remove("Bread")
print("\nAfter Removing Bread")
print(cart)

cart[1][1] = "Cheese"
print("\nAfter Replacing Eggs With Cheese")
print(cart)

print("\nFinal Cart Summary")
print("Owner: ", cart[0])
print("Items: ", cart[1])