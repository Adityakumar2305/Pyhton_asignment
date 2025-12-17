text = input("Enter a string: ")
cleaned = text.lower()

if cleaned == cleaned[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
