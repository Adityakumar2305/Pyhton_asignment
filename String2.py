
text = input("Enter a sentence: ")
words = text.split()
reversed_words = [word[::-1] for word in words]
result = " ".join(reversed_words)

print("Input:", text)
print("Output:", result)
