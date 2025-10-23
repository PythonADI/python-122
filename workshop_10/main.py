text = "Hello"
print(text[0], type(text[0]))
print(text[1:4])
print(text[::2])

text_slice = ""

for i in range(1, 4):
    text_slice += text[i]

print(text_slice)
