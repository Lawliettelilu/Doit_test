# 1. შექმენით ვექტორის Vector კლასი, რომელიც წარმოადგენს 2D ვექტორს. კლასს უნდა ჰქონდეს ორი ატრიბუტი x და y.
#  კლასში დაამატეთ __add__ მეთოდი, რომ მოახდინოთ ვექტორების დამატება და __str__ მეთოდი, 
# რომელიც დააბრუნებს შემდეგი სახის სტრიქონს "(x, y)".

# მაგალითად:
# v1 = Vector(2, 3)
# v2 = Vector(3, 4)
# v3 = v1 + v2
# print(v3)  # Output: (5, 7)

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __str__(self):
        return f"({self.x}, {self.y})"

# ობიექტების შექმნა
v1 = Vector(2, 3)
v2 = Vector(3, 4)
v3 = v1 + v2
print(v3)  # Output: (5, 7)


# 2. შექმენით Book კლასი, რომელსაც ექნება ორი ატრიბუტი (სათაური, ავტორი). 
# კლასს შეუქმენით __eq__ მეთოდი რომელიც შეამოწმებს ორი წიგნის ტოლობას.
# ორი წიგნი ითვლება ტოლად თუ მათი სათაურები და ავტორები იდენტურია.

# მაგალითად:
# book1 = Book('1984', 'George Orwell')
# book2 = Book('1984', 'George Orwell')
# book3 = Book('Brave New World', 'Aldous Huxley')
# print(book1 == book2)  # Output: True
# print(book1 == book3)  # Output: False

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
# ობიექტების შექმნა
book1 = Book('1984', 'George Orwell')
book2 = Book('1984', 'George Orwell')
book3 = Book('Brave New World', 'Aldous Huxley')
print(book1 == book2)  
print(book1 == book3)  


# 3. დაწერეთ პითონის Car (ატრიბუტები: brand, model, year) კლასი და მოახდინეთ ამ კლასისთვის __new__ და __init__ მეთოდის გადაფარვა.

# Car კლასს დაუმატეთ  თითოეული ატრიბუტისთვის set და get თვისებები მათი ცვლილებებისთვის.

# დაამატეთ Car კლასის set ფუნქციებში, ვალიდაციები თითოეული ატრიბუტისთვის, მაგალითად year ატრიბუტი რომ იყოს ყოველთვის მთელი და ა.შ.

class Car:
    def __new__(cls, brand, model, year):
        if not isinstance(year, int):
            raise ValueError("Year must be an integer")
        return super().__new__(cls)
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def set_year(self, year):
        if not isinstance(year, int):
            raise ValueError("Year must be an integer")
        self.year = year
    def get_year(self):
        return self.year

# კოდის ტესტირება
car1 = Car("Toyota", "Corolla", 2018)
car2 = Car("Mercedes", "C-Class", 2022)
car1.year=2020
print(car1.get_year())