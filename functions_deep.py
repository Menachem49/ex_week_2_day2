#ex_5
def add_item(item, cart=[]):
    cart.append(item)
    return cart
print(add_item("milk"))
print(add_item("bread"))

# ['milk', 'bread']
# מכיון שרשמו לפונקציה כברירת מחדל מילון ריק הוא חושב שיש צורך בלשמור את הערכים שיש בו

def add_item(item, cart= None):
    cart = []
    cart.append(item)
    return cart
print(add_item("milk"))
print(add_item("bread"))