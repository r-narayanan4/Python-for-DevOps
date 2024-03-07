# Program to calculate discount based on purchase amount using nested if-else statements

purchase_amount = 150

if purchase_amount >= 100:
    if purchase_amount < 200:  # Check if purchase amount is between 100 and 199
        discount = 10
    elif purchase_amount < 500:  # Check if purchase amount is between 200 and 499
        discount = 20
    else:  # If purchase amount is 500 or more
        discount = 30
    final_amount = purchase_amount - (purchase_amount * discount / 100)
    print("Discount applied:", discount, "%")
    print("Final amount after discount:", final_amount)
else:  # If purchase amount is less than 100
    print("No discount applied. Final amount:", purchase_amount)
