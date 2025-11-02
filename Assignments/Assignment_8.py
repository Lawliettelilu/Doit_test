# 1. დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად n, და გამოიტანს ფიბონაჩის n რაოდენობის მიმდევრობას.


def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)
    return fib_sequence[:n]


# 2. დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად ორ სტრიქონს და შეამოწმებს არის თუ არა სტრიქონები ანაგრამები (ანაგრამი არის სიტყვა ან შესიტყვება, რომელიც წარმოიქმნება სხვა სიტყვის ან შესიტყვების ასოების გადაადგილებით). მაგ.: race და care ანაგრამებია.

def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2) 
print(are_anagrams(input("შეიყვანეთ პირველი სიტყვა: "), input("შეიყვანეთ მეორე სიტყვა: ")))


# 3. დაწერეთ პითონის ფუნქცია რომელიც მიიღებს n რიცხვს და დააბრუნებს მის ფაქტორიალს.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(int(input("შეიყვანეთ რიცხვი: "))))


# 4. დაწერეთ პითნის ფუნქცია რომელიც მიიღებს  ორ პარამეტრს, პირველს სტრიქონს და მეორეს სიმბოლოს. ფუნქციამ უნდა მოძებნოს სტრიქონში რამდენჯერ მეორდება პარამეტრად მიღებული სიმბოლო და დააბრუნოს  მისი რაოდენობა.

def count_character(string, char):
    return string.count(char)
print(count_character(input("შეიყვანეთ სტრიქონი: "), input("შეიყვანეთ სიმბოლო: ")))

