#ex_1
def apply_to_all(numbers, action):
    pass

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