prices = [100,200,300,400,500]
discount = 10
new_prices = []

for i in prices:
  new_price = i - (i * discount/100)
  new_prices.append(new_price)
print(new_prices)