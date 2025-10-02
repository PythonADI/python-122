word = input(">>> ")


for c in word:
    print(c)


vowels = "aeiou"

for vowel in vowels:
    vowel_count = word.lower().count(vowel)
    print(f"{vowel}: {vowel_count}")


# print(word.count("a"))
# print(word.count("e"))
# print(word.count("i"))
# print(word.count("o"))
# print(word.count("u"))

print(word[::-1])

