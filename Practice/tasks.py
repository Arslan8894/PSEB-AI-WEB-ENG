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



# COPY OR NOT

a = [1, 2, 3]
b = a
print(b)

a.append(4)
print(b)

# THIS WILL MAKE A SHALLOW COPY OF THE LIST. IF WE CHANGE THE VALUE OF A, IT WILL ALSO CHANGE THE VALUE OF B.
# When we assign a list to another variable, it does not create a new copy of the list. Instead, both variables point to the same list in memory. Therefore, any changes made to the original list will also affect the copied variable.

a = [1, 2, 3]
b = a.copy()
print(b)

a.append(4)
print(a)
print(b)
# THIS WILL MAKE A DEEP COPY OF THE LIST. IF WE CHANGE THE VALUE OF A, IT WILL NOT CHANGE THE VALUE OF B.
# When we use the copy() method, it creates a new copy of the list in memory. Therefore, any changes made to the original list will not affect the copied variable.


# Table of 7 
for i in range(1, 11):
    print("7 x", i, "=", 7 * i)


# Student Record
StudentRecord =("S23BSEEN1M01136", "ARSLAN SARWAR", "3.64/4.00")
print(f"Student ID: {StudentRecord[0]}")
print(f"Name: {StudentRecord[1]}")
print(f"CGPA: {StudentRecord[2]}")
