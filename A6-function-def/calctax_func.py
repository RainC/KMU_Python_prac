def calcTax(price,tax_rate):
	total = price+ (price * tax_rate)
	return total

my_price = float(input("input a price: " ))

totalPrice = calcTax(my_price, 0.06)

print("price = ", my_price, "Total = " , totalPrice) 
