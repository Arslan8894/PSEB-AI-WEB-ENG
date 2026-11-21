number = int(input("Enter a number : "))
if number < 0 :
    number = "Negative"
elif number == 0 :
    number = "Zero"
else :  
    number = "Positive"
print("The number is " + number)