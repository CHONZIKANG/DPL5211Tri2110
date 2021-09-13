# Student ID: 1201200750
# Student Name: Chon Zi Kang

BANANA = 1.50

GRAPE = 5.60

print("Invoice for Fruits Purchase")
print("--------------------------------")

banana_qty = int(input("Enter the quantity (comb) of bananas bought: "))

grape_kg = float(input("Enter the amount (kg) of grapes bought:"))

banana_price = (banana_qty * BANANA) 
grape_price = (grape_kg * GRAPE)
total = banana_price + grape_price

print("Item                  Qty         Price       Total")
print("Banana (combs)         {}        RM{:.2f}     RM{:.2f}".format(banana_qty, BANANA, banana_price))
print("Grapes (kg)            {}        RM{:.2f}     RM{:.2f}".format(grape_kg, GRAPE, grape_price))

print("Total: RM {:.2f}" .format(total))
