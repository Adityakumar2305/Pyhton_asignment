
text = "Vodafone"
print("Original string:", text)

try:
    text[0] = 'B' 
except TypeError:
    print("Strings are immutable! Cannot change characters directly.")
