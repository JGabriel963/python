word = str(input("Digite algo: "))
firstWord = word[0].lower()

new = word.replace(firstWord, "$")
print(f"{firstWord + new[1:]}")

str1 = "abc"
str2 = "xyz"

new_1 = str1[:2] + str2[2:]
new_2 = str2[:2] + str1[2:]

print(f"{new_1} {new_2}")
