#ex_1
def welcome(name):
    message = "Welcome " + name
    return message  

print(welcome("Dana"))
# print(message) NameError

print(welcome("Dana"))

#ex_2
count = 0
def add_one():
    count = count + 1
add_one()
# UnboundLocalError

count = 0
def add_one(count):
    return count + 1
    
add_one(count)


