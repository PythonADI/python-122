# here I create a list of strings
products = ["Keyboard", "Mouse", "Adapter", "Monitor", "Speaker", "Webcam"]


print(products[0])

# ბევრი ვარიანტია, რომ ბოლო ელემენტი ავიღოთ, მგრამ ყველაზე კარგი ვარიანტი არის პირდაპირ -1 ის გამოყენება

# ამ შემთვევაში ზომა შეიძლება შეიცვალოს ამიტომ ეს არ ვარგა
# print(products[4])
# ეს თვალისთვის ლამაზი არ არის
# print(products[len(products) - 1])
# ეს უფრო ლამაზია თვალისთვის
print(products[-1])

# აქ ვამატებთ ლისტში ელემენტს
products.append("Headphones")
print(products)

for product in products:
    print(product.upper())


print(len(products) )

print(products[:3])

# first_three_products = products[:3]
# print(first_three_products)
for product in products[:3]:
    print(product)


products.sort()
print(products)