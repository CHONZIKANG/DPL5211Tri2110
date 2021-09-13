# Student ID: 1201200750
# Student Name: Chon Zi Kang

WATER_LITRE = 0.15

print("Natural Mineral Water Dispenser")
print("---------------------------------")

litres = int(input("Enter amount of litres: "))

total = WATER_LITRE * litres

print("Price per litre = RM {}" .format(WATER_LITRE))
print("Number of liters = {}" .format(litres))
print("Total: RM {:.2f}" .format(total))