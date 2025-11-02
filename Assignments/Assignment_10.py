# 1. დაწერეთ პითონის ფუნქცია, რომელიც იღებს პარამეტრად ერთიდაიგივე ზომის სიას (list) 
# და zip ფუნქციის გამოყენებით დააჯგუფეთ სიების ელემენტები.

# params: [1, 2, 3], ['a', 'b', 'c']  
# outputs: ["(1, 'a')", "(2, 'b')", "(3, 'c')"]



list1=[1, 2, 3]
list2=['a', 'b', 'c']

def Function1(x, y):
    return [str(item) for item in zip(x, y)]

print(Function1(list1, list2))


# 2. დაწერეთ პითონის ფუნქცია, რომელიც პარამეტრად იღებს რიცხვების სიას და აბრუნებს ელემენტების ნამრავლს.
#  ფუნქციაში გაითვალისწინეთ გამონაკლისები (Exceptions), თუ მიიღეთ არასწორი ტიპის პარამეტრს (TypeError).
# ფუქნციის დასაწერად გამოიყენეთ lambda და  functools-ის reduce მეთოდი.  

# params:[1, 2, 3, 4, 5] 
# output: 120

from functools import reduce

def function2(numbers):
    try:
        if type(numbers) != list:
            raise TypeError("პარამეტრი უნდა იყოს სია (list).")
        
        result = reduce(lambda x, y: x * y, numbers)
        return result

    except TypeError as te:
        print(f"ტიპის შეცდომა: {te}")
        return None
    except Exception as e:
        print(f"გაუთვალისწინებელი შეცდომა: {e}")
        return None



# 3. დაწერეთ lambda ფუნქცია რომელიც იღებს მთელი რიცხვების სიას (list) და აბრუნებს მხოლოდ სიის კენტ ელემენტებს.

# params: [1, 2, 3, 4, 5, 6, 7]
# outputs: [1, 3, 5, 7]

filter_odd = lambda lst: list(filter(lambda x: x % 2 != 0, lst))
print(filter_odd([1, 2, 3, 4, 5, 6, 7]))


# 4. დაწერეთ პითნის ფუნქცია, რომელიც იღებს ორ პარამეტრს, სტრიქონების სიასა და სტრიქონს (ending). 
# დააბრუნეთ მხოლოდ სიის ის ელემენტები რომელიც მთავრდება, მეორე პარამეტრად მიწოდებული სტრიქონით. გამოიყენეთ lambda და filter ფუნქცია.
#  გაითვალისწინეთ გამონაკლისები (TypeError), თუ სხვა გამონაკლისიც აღმოჩნდა ისიც გაითვალისწინეთ.

# მინიშნება: გადაავლეთ თვალი string მეთოდებს, მონახეთ ისეთი მეთოდი, რომელიც აბრუნებს სიტყვას, რომელიც მთავრდება რაღაც სიმბოლოებით...

# params: ['hello', 'world', 'coding', 'nod'], 'ing'  
# outputs: ['coding']

def function4(string_list, ending):
    try:
        if type(string_list) != list:
            raise TypeError("პირველი არგუმენტი უნდა იყოს სია (list).")
        if type(ending) != str:
            raise TypeError("მეორე არგუმენტი უნდა იყოს სტრიქონი (string).")
        
        result = list(filter(lambda s: type(s) == str and s.endswith(ending), string_list))
        return result

    except TypeError as te:
        print(f"ტიპის შეცდომა: {te}")
        return []
    except Exception as e:
        print(f"გაუთვალისწინებელი შეცდომა: {e}")
        return []
print(function4(['hello', 'world', 'coding', 'nod'], 'ing'))



