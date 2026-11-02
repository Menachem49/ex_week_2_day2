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

#ex_4
def show_total(prices):
    print(f"Total: {calculate_total(prices)}")

def calculate_total(prices):
    total = 0
    for price in prices:
        total = total + price
    return total

show_total([10, 20, 30])

#ex_5
scores = [70, 95, 88, 60, 99]

def top_three(scores):
    top = sorted(scores, reverse=True)[:3]
    return top


print(top_three(scores))
print(scores)