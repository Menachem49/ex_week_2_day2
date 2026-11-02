#ex_1
def format_receipt(items):
    def line(name, price):
        return name.ljust(10) + str(price)
    lines = []
    for name, price in items:
        lines.append(line(name, price))
    return "\n".join(lines)
print(format_receipt([("Milk", 6), ("Bread", 9)]))

#ex_2
def make_greeter(greeting):
    def get_name(name):
        return greeting+" ,"+name
    return get_name

hello = make_greeter("Hello")
shalom = make_greeter("Shalom")
print(hello("Dana"))
print(shalom("Avi"))