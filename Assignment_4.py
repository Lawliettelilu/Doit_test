# 1. დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს და აბრუნებს სტრიქონის UTF-8 დაშიფრულ ვერსიას.
txt= input("შეიყვანეთ ტექსტი: ")
print(txt.encode('utf-8'))

# 2. დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს.
# ჩამოაშორეთ ზედმეტი ინტერვალები.
# ყველა სიმბოლო გადაიყვანეთ პატარა ასოებში და
# დაუმატეთ ქვესტრიქონი 'Python'.
# თუ შეყვანილ სტრიქონში არსებობს სიტყვა "python", ჩაანაცვლეთ "Python"-ით.

# მინიშნება: ზედმეტი ინტერვალების ჩამოსაშორებელი მეთოდია `.strip()`.

# მაგ.: "  Python is funny     ".strip()   ====>  "Python is funny"

str = input("შეიყვანეთ ტექსტი: ")
str = str.strip().lower()
str = str + ' Python'
if 'python' in str:
    str = str.replace('python', 'Python')   
print(str)  

# 3. დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს.
# პროგრამამ უნდა დააბრუნოს ახალი სტრიქონი,
# რომელიც შედგება შეყვანილი სტრიქონის პირველი ნახევრისაგან.

str = input("შეიყვანეთ ტექსტი: ")
half_length = len(str) // 2  
new_string = str[:half_length]
print(new_string) 


# 4. დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს.
# string მოდულის გამოყენებით დაწერეთ შემოწმება.
# სტრიქონი ვალიდურია მაშინ, როდესაც ის შეიცავს მინიმუმ ერთ ლათინურ ასოსა და
# მინიმუმ ერთ ციფრს და ამავე დროს არ შეიცავს დამატებით სიმბოლოებს: '!', '~', '#', '$' და ა.შ.

import string
str = input("შეიყვანეთ ტექსტი: ")
has_letter = any(char.isalpha() for char in str)
has_digit = any(char.isdigit() for char in str)
special_characters = set(string.punctuation)
has_special = any(char in special_characters for char in str)
if has_letter and has_digit and not has_special:
    print("ვალიდურია.")
else:
    print("არ არის ვალიდური.")


# 5. დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს,
# სტრიქონი გადაყავს ბაიტებში, ბეჭდავს მნიშვნელობას და შემდეგ კი
# გადაყავს ბაიტებიდან სტრიქონში და ბეჭდავს სტრიქონს.

str = input("შეიყვანეთ ტექსტი: ")
byte_str = str.encode('utf-8')  
print("ბაიტებში:", byte_str)
decoded_str = byte_str.decode('utf-8')
print("სტრიქონში:", decoded_str)