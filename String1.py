def count_categories(s: str):
    vowels = set("aeiouAEIOU")
    v = c = d = sc = 0
    for ch in s:
        if ch in vowels:
            v += 1
        elif ch.isalpha():
            c += 1
        elif ch.isdigit():
            d += 1
        else:
            sc += 1
    return v, c, d, sc


if __name__ == "__main__":
    text = input("Enter a string: ")
    v, c, d, sc = count_categories(text)
    print(f"Vowels: {v}")
    print(f"Consonants: {c}")
    print(f"Digits: {d}")
    print(f"Special: {sc}")

