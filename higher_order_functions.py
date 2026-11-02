#ex_1
def apply_to_all(numbers, action):
    new_list = []
    for number in numbers:
        new_list.append(action(number))
    return new_list

def double(number):
    return number * 2

print(apply_to_all([1, 2, 3], double))
print(apply_to_all([1, 2, 3], lambda n: n * n))
print(apply_to_all([1.6, 2.4], round))

#ex_2
prices = [20, 75, 120, 45, 90]

exspensive = list(filter(lambda p : p > 50, prices))

plus_ten = list(map(lambda p: p + 10, exspensive))

print(exspensive)

print(plus_ten)

#ex_3
words = ["banana", "fig", "cherry", "kiwi"]
students = [("Dana", 92), ("Avi", 78), ("Noa", 85)]

sorted_words = sorted(words, key=len)

print(sorted_words)

word_whit_the_max_lev = max(words, key=len)

print(word_whit_the_max_lev)

best_grede = map(lambda student : student[0], sorted(students, key= lambda s: s[1], reverse= True))
print("\n".join(list(best_grede)))
# for student in best_grede:
#     print(student[1])

#ex_4
def make_discount(percent):
    def cal(price):
        return price * (100 - percent) / 100
    return cal

ten_off = make_discount(10)
half_price = make_discount(50)
print(ten_off(200))
print(half_price(200))