# COPY OR NOT

a = [1, 2, 3]
b = a
print(b)

a.append(4)
print(b)

# THIS WILL MAKE A SHALLOW COPY OF THE LIST. IF WE CHANGE THE VALUE OF A, IT WILL ALSO CHANGE THE VALUE OF B.

a = [1, 2, 3]
b = a.copy()
print(b)

a.append(4)
print(a)
print(b)
# THIS WILL MAKE A DEEP COPY OF THE LIST. IF WE CHANGE THE VALUE OF A, IT WILL NOT CHANGE THE VALUE OF B.


# Table of 7 
for i in range(1, 11):
    print("7 x", i, "=", 7 * i)


# ShoppingCart
cart = ["Egg", "Butter", "Milk", "Cheese", "Bread", "Juice", "Cereal", "Rice", "Pasta", "Chicken"]
cart.append("CURD")
print(cart)
cart.insert(1, "Sugar")
print(cart)
cart.pop(5)
print(cart)
cart.remove("Rice")
print(cart)