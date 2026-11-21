char = input("Enter a character : ")

if char.isdigit():
    print("The character is a digit.")
elif char.isalpha():
    print("The character is an alphabet.")
elif char.islower():
    print("The character is a lowercase alphabet.")
elif char.isvowel():
    print("The character is a vowel.")
else:
    print("The character is a special character.")