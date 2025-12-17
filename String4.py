
text = input("Enter a string: ").lower()  
for ch in set(text):
    print(f"'{ch}': {text.count(ch)}")
