"""
შევამოწმოთ ბალანსზე არის თუ არა თანხა
- თუ არის ტანზაქცია წარმატებულია
- თუ არა ტრანზაქცია უარყოფილია
"""
balance = 50
cocktail_price = 14

if balance < cocktail_price:
    print("Transaction Failure, Inssufficient funds!")
else:
    print("Transaction Success!")
