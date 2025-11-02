# 1. კონსოლიდან შეიტანეთ მიმდევრობა. დაბეჭდეთ უნიკალური მონაცემებიანი სიმრავლე (set).

myset = set(input("შეიყვანეთ მონაცემები: "))
print(myset)

# 2. პირობა იგივეა, რაც პირველ დავალებაში, ოღონდ დაბეჭდეთ უნიკალური მონაცემებიანი სიმრავლე, რომლის შეცვლაც შეუძლებელი იქნება (frozenset).
myfrozenset = frozenset(input("შეიყვანეთ მონაცემები: "))
print(myfrozenset)
print(type(myfrozenset))

# 3. აიღეთ set ტიპის ორი მონაცემი. ელემენტები თავად განსაზღვრეთ. დაბეჭდეთ გაერთიანებული მონაცემები კორტეჟის სახით (tuple).
set1 = {'a', 'b', 'c', 'd'}
set2 = {'c', 'd', 'e', 'f'}
union_set = set1.union(set2)
print(tuple(union_set))
print(type(tuple(union_set)))

# 4. კონსოლიდან შევიტანოთ რიცხვების მიმდევრობა როგორც კორტეჟი (tuple). დავბეჭდოთ მხოლოდ უნიკალური ელემენტები სიის სახით (list).
mytuple = tuple(input("შეიყვანეთ რიცხვები: "))
mylist = list(mytuple)
print(mylist)   


# 5. მოცემულია სია, რომლის ელემენტები წარმოადგენენ კორტეჟს:
# [("Gega", 24), ("Gaga", 21), ("Goga", 19), ("Giga", 27), ("Gagi", 11)]

# დაბეჭდეთ შემდეგი ფორმატით:

# Name: Gega, Age: 24
# Name: Gaga, Age: 21
# Name: Goga, Age: 19
# Name: Giga, Age: 27
# Name: Gagi, Age: 11

users = [("Gega", 24), ("Gaga", 21), ("Goga", 19), ("Giga", 27), ("Gagi", 11)]
for name, age in users:
    print(f"Name: {name}, Age: {age}")


# 6. მოცემულია მომხმარებლების სია: ["Irakli", "Giorgi", "Nona", "Oto"].
# ასევე გვაქვს სხვა მომხმარებლებიც: ["Kato", "Levani", "Nino", "Dato", "Irakli", "Nemo"]
# დავბეჭდოთ თანხვედრა.
users1 = {"Irakli", "Giorgi", "Nona", "Oto"}
users2 = {"Kato", "Levani", "Nino", "Dato", "Irakli", "Nemo"}
common_users = users1.intersection(users2)  
print(common_users)
