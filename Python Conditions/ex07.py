bill = int(input("Enter the bill amount : "))

if bill>= 5000:
    discount = bill * 0.1
    print(bill-discount,"is the final bill amount after 10% discount.")
elif bill >=2000:
    discount = bill * 0.05
    print(bill-discount,"is the final bill amount after 5% discount.")
else:
    print(bill,"is the final bill amount. No discount applicable.")