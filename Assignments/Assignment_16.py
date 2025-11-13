# 1. შექმენით პითონის კლასი Car, ატრიბუტებით: ბრენდი, მოდელი და წელი. ასევე, შექმენით კლასის მეთოდი car_info(),
#  რომელიც დაბეჭდავს ატრიბუტების ინფორმაციას.

# 2. Car კლასში დაამატეთ მეთოდი age_of_car, რომელიც დაითვლის მანქანის ასაკს. ავტომობილის ასაკი დაბეჭდეთ car_info() მეთოდიდან.
# 3. შექმენით კლასი ElectricCar, რომელიც მემკვიდრეობით მიიღებს Car კლასს. დაამატეთ ახალი ატრიბუტი battery_life 
# და მეთოდი battery_info(), რომელიც დაბეჭდავს შემდეგ სტრიქონს "ამ მანქანის ბატარეის ხანგრძლივობა არის [battery_life] საათი".
# 4. დაამატეთ Car კლასს ატრიბუტი number_of_cars, რომელიც დაითვლის მანქანების სრულ რაოდენობას.
# გაზარდეთ ეს ცვლადი ყოველ ჯერზე, მანქანის შექმნისას. 
# 5. Car კლასს დაამატეთ მეთოდი total_cars(), რომელიც გამოიტანს მანქანების მთლიან რაოდენობას.


class Car:
    number_of_cars = 0

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        Car.number_of_cars += 1

    def car_info(self):
        print(f"ბრენდი: {self.brand}, მოდელი: {self.model}, წელი: {self.year}")
        print(f"ავტომობილის ასაკი: {self.age_of_car()} წლები")

    def age_of_car(self):
        current_year = 2025  # ვვარაუდობთ რომ მიმდინარე წელია 2025
        return current_year - self.year
    
    @classmethod
    def total_cars(cls):
        print(f"სულ შექმნილია {cls.number_of_cars} მანქანა.")

#3. შვილობილი კლასი ElectricCar
class ElectricCar(Car):

    def __init__(self, brand, model, year, battery_life):
        super().__init__(brand, model, year)
        self.battery_life = battery_life

    def battery_info(self):
        print(f"ამ მანქანის ბატარეის ხანგრძლივობა არის {self.battery_life} საათი.")

# კოდის ტესტირება
car1 = Car("Toyota", "Corolla", 2018)
car2 = Car("BMW", "X5", 2020)
car3 = ElectricCar("Tesla", "Model 3", 2023, 12)

# ინფორმაციის დაბეჭდვა
car1.car_info()
car2.car_info()
car3.car_info()
car3.battery_info()

# საერთო რაოდენობის დაბეჭდვა
Car.total_cars()