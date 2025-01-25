def isVowel(a:chr)->str:
    return f"'{a}' is a vowel" if a in ['a','e','i','o','u', 'A', 'E', 'I', 'O', 'U'] else f"'{a}' is a consonant."

print(isVowel(input("Enter a character : ")[0]))