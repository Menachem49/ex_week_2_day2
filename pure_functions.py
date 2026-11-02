#ex_2

def add_price(price, total):
    return total + price

total = 0
total = add_price(total, 10)
total = add_price(total, 10)
print(total)
print(add_price(0, 10))
print(add_price(0, 10))

#ex_3
TAX = 1.17

def apply_tax(prices):
    finali_prices = []
    for i in range(len(prices)):
        finali_prices.append(prices[i] * TAX)
    return finali_prices

prices = [100, 50]
with_tax = apply_tax(prices)
print(prices)
print(with_tax)